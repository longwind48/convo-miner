from bs4 import BeautifulSoup
import requests
import re

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

def get_fiction_sentences(http_link):
    soup = get_soup(http_link)
    tag_texts = get_tag_text(soup)
    tag_texts = [preprocess(i) for i in tag_texts]
    tag_texts = [i for i in tag_texts if i]
    sentences = [tokenizer(i) for i in tag_texts]
    # return sentences
    return tag_texts


if __name__ == "__main__":
    sentences = get_fiction_sentences("https://www.gutenberg.org/files/42671/42671-h/42671-h.htm")
    print(sentences[0:20])
