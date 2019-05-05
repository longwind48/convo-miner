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