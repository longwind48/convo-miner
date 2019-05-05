import pickle
import os
dirname = os.path.dirname("__file__")

def save_as_pickle(myObject, target_filename):
    with open(os.path.join(dirname, "{}.pkl".format(target_filename)), "wb") as pickle_out:
        pickle.dump(myObject, pickle_out)
    print('{} saved!'.format(target_filename))

def load_from_pickle(src_filename):
    with open(os.path.join(dirname, "{}.pkl".format(mylistnsrc_filenameame)), "rb") as pickle_out:
        mylist = pickle.load(pickle_out)
        print('{} loaded!'.format(src_filename))
    return mylist

def get_link_title_author_from_booklist(book_index):
    raw_html_dict = dict()
    f = open("../data/raw/html-book-list", "r")
    for x in f:
        line_details = [j.replace(' ', '-') for j in x.lower().strip().split(',')]
        index = line_details[0]
        raw_html_dict[index] = dict(
                                link=line_details[1],
                                title=line_details[2],
                                author=line_details[3])
    return raw_html_dict[str(book_index)]
