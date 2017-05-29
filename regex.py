import re
import urllib.request
import urllib
from collections import deque

queue = deque()
visited = set()

url = "http://news.dbanotes.net";

queue.append(url)
cnt = 0;

while queue:
    url = queue.popleft()
    visited |= {url}

    print("已抓取: " + str(cnt) + "  正在抓取 " + url)
    cnt += 1
    urlop = urllib.request.urlopen(url)
    if 'html' not in urlop.getheader('Content-Type'):
        continue

    #为避免程序异常终止，用try catch
    try:
        data = urlop.read().decode("UTF-8")
    except:
        continue

    #正则表达式提取页面中所有队列，并判断是否已经访问过，未方位过则加入待爬队列
    linkre = re.compile('href=\"(.+?)\"')
    for x in linkre.findall(data):
        if 'http' in x and x not in visited:
            queue.append(x)
            print("队列新增： " + x)



