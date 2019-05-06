# -*- coding: utf-8 -*-
"""
This generates a localhost web app for demo
"""
# from __future__ import print_function
# import sys
from flask import Flask, render_template, request
from scripts.present_result import iob_to_html_tags

app = Flask(__name__)
http_link = None

@app.route('/')
# @app.route('/base.html')
@app.route('/index.html')
def home():
    # return render_template('base.html')
    return render_template('index.html')

@app.route('/result_frame.html')
def result_frame():
    global http_link
    webpage = iob_to_html_tags(http_link)
    # webpage = get_body(http_link)
    return render_template('result_frame.html', webpage=webpage)

@app.route('/select_fiction_book', methods=['GET', 'POST'])
def get_user_id():
    global http_link
    if request.method == 'POST':
        http_link = request.form['data']
        if http_link == '':
            error = 'html page is keyed in'
            return render_template('result_page.html', error1=error)
        if http_link:
            return render_template('result_page.html')
#        if data:
#            result = analyze_user(data)
#            return render_template('index.html', table = table)

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

# @app.route('/')
# def analyze_user():
#     model = Model(selected_user)
#     result1 = model.analyze_recommend1()
#     result2 = model.analyze_recommend2()
#     # print("result", type(result), file=sys.stderr)
#     # print("result glimpse", result.head, file=sys.stderr)
#
#     table1 = re.sub(' order_table', '" id="RC_table', result1.to_html(classes='table table-bordered table-striped table-hover text-left order_table', index=False))
#     table2 = re.sub(' order_table', '" id="RC_table', result2.to_html(classes='table table-bordered table-striped table-hover text-left order_table', index=False))
#     tables = [table1, table2]
#     return tables

if __name__ == '__main__':
    app.run(debug = True)
