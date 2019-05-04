from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import os
from argparse import ArgumentParser

import sys
sys.path.append('./src')
from utils import get_link_title_author_from_booklist



def get_soup(http_link):
    """get web page content"""
    page = requests.get(http_link)
    encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(page.content, features="html.parser", from_encoding=encoding)
    # print(soup.prettify())
    return soup

def get_tag_text(soup):
    """
    Get texts between tags p and h2ß
    :param soup:
    :return texts: list of strings
    """
    texts = [i.get_text() for i in soup.findAll(['p', 'h2'])]
    return texts

def preprocess(text):
    """ Replace funny tokens with normal ones """
    text = text.replace('\r\n', ' ')
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.strip()
    return text

def remove_period_from_honorifics(para):
    """ Remove period from honorifics """
    regex = '(Miss.|Mrs.|Mr.|Ms.)'
    for i in re.findall(regex, para, flags=re.IGNORECASE):
        para = para.replace(i, i[:-1])
    return para

def get_num_quotes(sent):
    return sent.count('"')

def is_utterance(sent):
    return ((get_num_quotes(sent)%2==0) & (get_num_quotes(sent)!=0))

def add_tag_to_dict(sent_index, sent, somedict, tag):
    """ Insert tuple to dictionary """
    global total_quotes_count
    num_utterance = int(get_num_quotes(sent) / 2)
    somedict[sent_index] = (tag, total_quotes_count, num_utterance)
    return somedict

def tag_dialogue(sent_index, sent):
    """
    Creates a dictionary object with key=sentence_index and value=tuple(tag, total_quote_count, num_utterance)
    :param sent_index: sentence index
    :param sent: a sentence of type string
    :return sent_dia_dict:
    """
    global total_quotes_count, sent_dia_dict, sent_list

    num_quotes = get_num_quotes(sent)

    if num_quotes == 0:
        add_tag_to_dict(sent_index, sent, sent_dia_dict, 'narrative')

    elif num_quotes == 1:
        total_quotes_count += 1
        add_tag_to_dict(sent_index, sent, sent_dia_dict, 'single_quote')  # letter-S


    elif num_quotes == 2:
        total_quotes_count += 2
        add_tag_to_dict(sent_index, sent, sent_dia_dict, 'utterance')


    elif num_quotes > 2:
        if (num_quotes % 2) == 0:
            total_quotes_count += num_quotes
            add_tag_to_dict(sent_index, sent, sent_dia_dict, 'utterance')
        else:
            total_quotes_count += num_quotes
            add_tag_to_dict(sent_index, sent, sent_dia_dict, 'single_quote')

    return sent_dia_dict

def find_utterances_raw(para):
    """ Find all sentences that contains quotes, and return a list of them"""
    quotes = re.findall('"([^"]*)"', para)
    return ['"' + i + '"' for i in quotes]

def replace_narrative_w_mark(sent_list):
    """
    Replace narrative in utterances with character '_'
    e.g. <"Hi, there," said Tom, "Can you help me?"> --> <"Hi, there," _ "Can you help me?">
    Uncomment 'continue' to remove narratives in utterance.
    e.g. <"Hi, there," said Tom, "Can you help me?"> --> <"Hi, there," "Can you help me?">
    :param sent_list: list of tokenized sentences
    :return new_sent_list: list of sentences with modifications
    """
    new_sent_list = []
    for i, sent in enumerate(sent_list):
        if i == 0:
            new_sent_list.append(sent) if is_utterance(sent) else new_sent_list.append(sent)
        elif i == len(sent_list)-1:
            new_sent_list.append(sent) if is_utterance(sent) else new_sent_list.append(sent)
        else:
            if is_utterance(sent) == False:
                if is_utterance(sent_list[i-1]) & is_utterance(sent_list[i+1]):
                    continue
                    # new_sent_list.append('_')
                else:
                    new_sent_list.append(sent)
            else:
                new_sent_list.append(sent)
    return new_sent_list

def custom_tokenize_quotes(para):
    """ Custom tokenizer to tokenize paragraph into list of sentences, separated by utterances and narratives """
    regex = r'(("[^"]*")|([^"]*))'
    results = [i[0] for i in re.findall(regex, para)]
    tag_texts = [i for i in results if i]
    new_sent_list = replace_narrative_w_mark(tag_texts)
    return new_sent_list

def get_fiction_sentences(http_link):
    soup = get_soup(http_link)
    tag_texts = get_tag_text(soup)
    tag_texts = [preprocess(i) for i in tag_texts]
    tag_texts = [i for i in tag_texts if i]
    return tag_texts

if __name__ == "__main__":
    # Request filepath as arguement
    parser = ArgumentParser("Converts input .pdf file to rawtext.")
    parser.add_argument("-i", "--index", dest="input", required=False,
                        help="\n Specify index from data/raw/html-book-list", type=str)

    args = parser.parse_args()

    # Get input from argparser
    book_index = args.input
    if args.input is None:
        book_index = 1

    input_dict = get_link_title_author_from_booklist(book_index)

    link = input_dict['link']
    title = input_dict['title']
    author = input_dict['author']

    sentences = get_fiction_sentences(link)

    total_quotes_count = 0
    sent_dia_dict = dict()
    for sent_index, sent in enumerate(sentences):
        sent_dia_dict = tag_dialogue(sent_index, sent)

    df = pd.DataFrame(list(sent_dia_dict.items()), columns=['para_index', 'tag'])
    df['para'] = sentences
    df['num_utterances'] = df['tag'].apply(lambda x: x[2])
    df['tag'] = df['tag'].apply(lambda x: x[0])

    df['raw_utter_list'] = df['para'].apply(lambda x: find_utterances_raw(x))
    df['tokenized_sent'] = df['para'].apply(lambda x: custom_tokenize_quotes(x))

    # Save as csv
    dirname = os.path.dirname('__file__')
    output_path = os.path.join(dirname, '../data/parser_output/')
    current_year = str(datetime.datetime.now())[0:10]
    csv_name = 'parser-output-{}-{}-{}.csv'.format(title, author, current_year)
    df.to_csv(output_path + csv_name)
