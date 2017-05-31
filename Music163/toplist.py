from Music163.filt_html import filter_html
from Music163.get_toplist_html import get_toplist_html
from Music163.save import save_str
from lxml import html
from pyquery import PyQuery as pq

# 1.get html
req = get_toplist_html()

#2.filter html,using pyQuery
li_list = filter_html(req)

#3.
text_content = "";
for li in li_list:
    text = pq(html.fromstring(li)).text()
    href = pq(html.fromstring(li)).attr("href")
    id = (href.split("=",2))[1]
    text_content += text
    text_content += "\t\t" + id
    text_content +="\n"

print(text_content)
save_str(text_content)


