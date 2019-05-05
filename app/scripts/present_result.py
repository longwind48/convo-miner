from bs4 import BeautifulSoup
import requests
import re
import pandas as pd


def preprocess(text):
    text = text.replace('\r\n', ' ')
    text = text.replace('“', '"')
    text = text.replace('”', '"')
    text = text.strip()
    text = remove_period_from_honorifics(text)
    return text

def remove_period_from_honorifics(para):
    regex = '(Miss.|Mrs.|Mr.|Ms.)'
    for i in re.findall(regex, para, flags=re.IGNORECASE):
        para = para.replace(i, i[:-1])
    return para

def has_text(each_soup_select):
    text = each_soup_select.get_text()
    text = preprocess(text)
    return True if text else False

def find_word_position(sentence, target_str):
    """
    fine position of target_str in the sentence regardless of special characters
    """
    positions = []
    pat = r'(^|\W)(' + re.escape(target_str) + ')(\W|$)'
    for m in re.finditer(pat, sentence):
        word = m.group()
        if word[0] != target_str[0]:
            start_pos = m.start() + 1
        else:
            start_pos = m.start()
        if word[-1] != target_str[-1]:
            end_pos = m.end() - 1
        else:
            end_pos = m.end()
        positions.append({"start_pos": start_pos, "end_pos": end_pos})
    if positions and len(positions) == 1:
        return positions[0]["start_pos"], positions[0]["end_pos"]


def iob_to_html_tags(http):
    df = pd.read_csv("../data/parsed-n-labeled-data/iob-labeled-sent-final-020519.csv")

    # pride & prejudice
    page = requests.get(http)
    # soup = BeautifulSoup(page.content, 'html.parser')
    encoding = page.encoding if 'charset' in page.headers.get('content-type', '').lower() else None
    soup = BeautifulSoup(page.content, from_encoding=encoding)
    # print(soup.prettify())
    for tag in soup.find_all('blockquote'):
        tag.replaceWith('')

    cnt = 0
    div = soup.new_tag("div")
    for select in soup.findAll(['p', 'h2']):
        if has_text(select):
            #         print(select)
            match_df = df[df["para_index"] == cnt].reset_index()
            if match_df.shape[0] <= 0:
                raise Exception("nothing found?", select)
            #         elif match_df.shape[0]==1:
            else:
                # print("before", select)
                #             print(match_df.shape)
                text = preprocess(select.get_text())
                prev_end = 0

                select.clear()
                select.append("\r\n")

                for idx, row in match_df.iterrows():
                    tokenized_sent = row["sent"]
                    labl = row["label"]
                    #                 print("tokenized:",tokenized_sent)
                    #                 print("full sent:",text)
                    pos = find_word_position(text, tokenized_sent)
                    #                 print(pos)
                    if pos:
                        start = pos[0]
                        end = pos[1]
                        # append non-labeled text before current label
                        if start > prev_end:
                            select.append(text[prev_end:start])
                        # append current label
                        if labl == "O":
                            select.append(text[start:end])
                        else:
                            mark = soup.new_tag("mark")
                            mark["data-entity"] = labl
                            mark.append(text[start:end])
                            select.append(mark)
                        prev_end = end
                # append non-labeled text after current label
                if prev_end < match_df.shape[0]:
                    select.append(text[prev_end:])
                select.append("\r\n")

                # print("after", select)
                cnt += 1
            div.append(select)
    print(div)
    return div

# iob_to_html_tags("http://www.gutenberg.org/files/1342/1342-h/1342-h.htm")