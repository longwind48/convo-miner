from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
import numpy as np

def isNaN(num):
    return num != num

def get_soup(http_link):
    """get web page content"""
    page = requests.get(http_link)
    encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(page.content, features="html.parser", from_encoding=encoding)
    # print(soup.prettify())
    return soup


def get_tag_text(soup):
    texts = [i.get_text() for i in soup.findAll(['p','h2'])]
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

def load_label():
    df_labeled = pd.read_csv(
        '../data/parsed-n-labeled-data/pnp-gutenberg-label-task-pride-and-prejudice-by-jane-austen.csv',
        index_col=[0])
    df_labeled = df_labeled.reset_index()
    df_labeled.columns = ['para_index', 'tag_old', 'para', 'position', 'speaker', 'type']
    return df_labeled

def is_out_of_entity_label(labl_str):
    if isNaN(labl_str):
        return True
    else:
        if labl_str.strip().lower() == 'n':
            return True
        else:
            return False

def is_in_entity_label(label_str):
    if label_str in ['3', '4', '2', '6', '5', '1']:
        return True
    else:
        return False

def get_fiction_sentences(http_link):
    labeled_data = load_label()
    soup = get_soup(http_link)
    tag_texts = get_tag_text(soup)
    tag_texts = [preprocess(i) for i in tag_texts]
    tag_texts = [i for i in tag_texts if i]
    labeled_paragraph = tag_texts[62:labeled_data.shape[0]+62]
    labeled_data['new_para'] = pd.Series(labeled_paragraph)
    print(labeled_data.head())
    labeled_data['iob_label'] = None
    # <class 'list'>: [nan, '3', '4', '2', '6', 'N', 'n', '5', '1']
    labeled_positions = list(set(labeled_data['position'].tolist()))
    prev_label = None
    for idx,row in labeled_data.iterrows():
        label = row['position']
        if is_out_of_entity_label(label):
            iob_labl = 'O'
        elif label in ['3', '4', '2', '6', '5', '1']:
            if is_out_of_entity_label(prev_label):
                iob_labl = 'B-DIALOG'
            elif is_in_entity_label(prev_label):
                if label==prev_label:
                    iob_labl = 'I-DIALOG'
                else:
                    iob_labl = 'B-DIALOG'
        else:
            raise ValueError(label+" not defined in iob label list")
        prev_label = label
        labeled_data.iloc[idx, 7] = iob_labl
    print(labeled_data.head())
    # sentences = [tokenizer(i) for i in tag_texts]
    # return sentences
    return tag_texts


if __name__ == "__main__":
    sentences = get_fiction_sentences("http://www.gutenberg.org/files/1342/1342-h/1342-h.htm")
    print(sentences[0:20])
