# -*- coding: utf-8 -*-
"""
This generates a localhost web app for demo
"""
# from __future__ import print_function
# import sys
from flask import Flask, render_template, request
from scripts.present_result import iob_to_html_tags

app = Flask(__name__)
pride_prejudice_link = "http://www.gutenberg.org/files/1342/1342-h/1342-h.htm"

@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')
    global pride_prejudice_link
    webpage = iob_to_html_tags(pride_prejudice_link)
    return render_template('result_page.html', webpage1=webpage, webpage2=webpage)

@app.route('/result_frame.html')
def result_frame():
    global pride_prejudice_link
    webpage = iob_to_html_tags(pride_prejudice_link)
    return render_template('result_frame.html', webpage1=webpage, webpage2=webpage)

@app.route('/start_demo', methods=['GET'])
def get_user_id():
    return render_template('result_page.html')


from bs4 import BeautifulSoup
import requests

def get_body(http_link):
    """get web page content"""
    page = requests.get(http_link)
    encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(page.content, features="html.parser", from_encoding=encoding)

    body = soup.find("body")
    body.name = "div"
    # body['id'] = 'webpage'
    return body


if __name__ == '__main__':
    app.run(debug = True)
