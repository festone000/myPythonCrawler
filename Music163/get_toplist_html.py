import urllib
from urllib import request


def get_toplist_html():
    top_list_url = "http://music.163.com/discover/toplist";
    req = urllib.request.urlopen(top_list_url).read().decode("UTF-8")
    return req
