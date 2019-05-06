# -*- coding: utf-8 -*-
"""
This generates a localhost web app for demo
"""
# from __future__ import print_function
# import sys
from flask import Flask, render_template, request
from present_result import iob_to_html_tags

app = Flask(__name__)
pride_prejudice_link = "http://www.gutenberg.org/files/1342/1342-h/1342-h.htm"


@app.route('/')
@app.route('/index.html')
def home():
    return render_template('index.html')


@app.route('/result_frame1.html')
def result_frame_seq():
    global pride_prejudice_link
    page_label = iob_to_html_tags(pride_prejudice_link,
                                  "../data/parsed-n-labeled-data/iob-labeled-sent-final-060519-v2.csv")
    page_pred = iob_to_html_tags(pride_prejudice_link,
                                 "../data/predicted/seq_label_ner-v4-pred.csv")

    return render_template('result_frame.html', webpage1=page_label, webpage2=page_pred)


@app.route('/result_frame2.html')
def result_frame_heuristic():
    global pride_prejudice_link
    page_label = iob_to_html_tags(pride_prejudice_link,
                                  "../data/parsed-n-labeled-data/iob-labeled-sent-final-060519-v2.csv")
    page_pred = iob_to_html_tags(pride_prejudice_link,
                                 "../data/predicted/heuristic_pred_v2.csv")

    return render_template('result_frame.html', webpage1=page_label, webpage2=page_pred)


@app.route('/start_demo', methods=['GET'])
def render_result():
    return render_template('result_page.html')


if __name__ == '__main__':
    app.run(debug=True)
