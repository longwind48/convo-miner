from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import datetime
import os
import numpy as np

def get_soup(http_link):
    """get web page content"""
    page = requests.get(http_link)
    encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(page.content, features="html.parser", from_encoding=encoding)
    # print(soup.prettify())
    return soup


def get_tag_text(soup):
    texts = [i.get_text() for i in soup.findAll(['p', 'h2'])]
    return texts


def preprocess(text):
    text = text.replace('\r\n', ' ')
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.strip()
    return text


def tokenizer(paragraph):
    sents = tokenize_quoted_sentence(paragraph)


def tokenize_quoted_sentence(paragraph):
    pat = r'(("[^"]*")|([^"]*))'
    results = re.findall(pat, paragraph)
    results = [i[0] for i in results]
    return results


def get_num_quotes(sent):
    return sent.count('"')


def add_tag_to_dict(sent_index, sent, somedict, tag):
    global total_quotes_count
    num_utterance = int(get_num_quotes(sent) / 2)
    somedict[sent_index] = (tag, total_quotes_count, num_utterance)
    return somedict


def is_quote_start_of_sent(sent):
    # must have capitalized alphabet after quote
    return bool(re.match('^"[A-Z]', sent))


def is_quote_end_of_sent(sent):
    return bool(re.match('.*"$', sent))


def tag_dialogue(sent_index, sent):
    global total_quotes_count, sent_dia_dict, sent_list

    num_quotes = get_num_quotes(sent)

    if num_quotes == 0:
        add_tag_to_dict(sent_index, sent, sent_dia_dict, 'narrative')

    elif num_quotes == 1:
        total_quotes_count += 1
        add_tag_to_dict(sent_index, sent, sent_dia_dict, 'letter')  # letter-S


    elif num_quotes == 2:
        total_quotes_count += 2
        add_tag_to_dict(sent_index, sent, sent_dia_dict, 'utterance')


    elif num_quotes > 2:
        if (num_quotes % 2) == 0:
            total_quotes_count += num_quotes
            add_tag_to_dict(sent_index, sent, sent_dia_dict, 'utterance')
        else:
            total_quotes_count += num_quotes
            add_tag_to_dict(sent_index, sent, sent_dia_dict, 'letter')

    return sent_dia_dict


def find_utterances_raw(para):
    quotes = re.findall('"([^"]*)"', para)
    return ['"' + i + '"' for i in quotes]

def remove_period_from_honorifics(para):
    regex = '(Miss.|Mrs.|Mr.|Ms.)'
    for i in re.findall(regex, para, flags=re.IGNORECASE):
        para = para.replace(i, i[:-1])
    return para

def replace_narrative_w_mark(sent_list):
    new_sent_list = []
    for sent in sent_list:
        if ((get_num_quotes(sent))%2==0) & ((get_num_quotes(sent)!=0)):
            new_sent_list.append(sent)
        else:
            new_sent_list.append('[N]')
    return ' '.join(new_sent_list)

def tokenize_para(para):
    para = remove_period_from_honorifics(para)
#     regex = '((?![.\s])[^."]*(?:"[^"]*[^".]"[^."]*)*(?:"[^"]+\."|\.))'
#     regex = '((?![.\s])[^."]*(?:"[^"]*[^".]"[^."]*)*(?:"[^"]+\."|\.|"[^"]+\?"|"[^"]+\!"))'
    regex = r'(("[^"]*")|([^"]*))'
    results = [i[0] for i in re.findall(regex, para)]
    tag_texts = [i for i in results if i]
    output_string = replace_narrative_w_mark(tag_texts)
    return output_string

def get_fiction_sentences(http_link):
    soup = get_soup(http_link)
    tag_texts = get_tag_text(soup)
    tag_texts = [preprocess(i) for i in tag_texts]
    tag_texts = [i for i in tag_texts if i]
    return tag_texts



if __name__ == "__main__":
    sentences = get_fiction_sentences("http://www.gutenberg.org/files/1342/1342-h/1342-h.htm")

    doc = sentences

    total_quotes_count = 0
    sent_dia_dict = dict()
    for sent_index, sent in enumerate(doc):
        sent_dia_dict = tag_dialogue(sent_index, sent)

    df = pd.DataFrame(list(sent_dia_dict.items()), columns=['para_index', 'tag'])
    df['para'] = doc
    df['num_quotes_up_to_para'] = df['tag'].apply(lambda x: x[1])
    df['num_utterances'] = df['tag'].apply(lambda x: x[2])
    df['tag'] = df['tag'].apply(lambda x: x[0])

    df['raw_utter_list'] = df['para'].apply(lambda x: find_utterances_raw(x))
    df['tokenized_sent'] = df['para'].apply(lambda x: tokenize_para(x))
    df['tokenized_sent_clean'] = df['tokenized_sent'].apply(lambda x: re.sub('"', '', x))

    # Save as csv
    dirname = os.path.dirname('__file__')
    output_path = os.path.join(dirname, '../output/')
    csv_name = 'html_parse_{}.csv'.format(str(datetime.datetime.now())[0:10])
    df.to_csv(output_path + csv_name)
