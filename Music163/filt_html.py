from pyquery import PyQuery as pq
from lxml import html

top_list_array = []


# d = pq("<html></html>")
# d = pq(etree.fromstring("<html></html>"))
# d = pq(url='https://google.com/')
# d = pq(url='http://google.com/', opener=lambda url, **kw: urllib.urlopen(url).read())
# d = pq(filename=path_to_html_file)

def filter_html(html_str):
    html_document = html.document_fromstring(html_str)
    doc = pq(html_document)
    ul_html = doc.find("ul.f-hide")
    lis = pq(html.fromstring(ul_html.outer_html())).children()
    for li in lis:
        # print(pq(li).html())
        top_list_array.append(pq(li).html())
    return top_list_array
