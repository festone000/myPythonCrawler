import urllib.request

url="http://www.baidu.com"
data = urllib.request.urlopen(url).read()
data2 = urllib.request.urlopen(url)
data = data.decode("UTF-8")
print(data)