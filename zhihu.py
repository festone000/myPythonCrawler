from Tools.cookie import getOpener
from Tools.gzip import ungzip
from Tools.file import save_file
from Tools.xsrf import getXSRF
import urllib

header = {
    'Connection': 'Keep-Alive',
    'Accept': 'text/html, application/xhtml+xml, */*',
    'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Accept-Encoding': 'gzip, deflate',
    'Host': 'www.zhihu.com',
    'DNT': '1'
}

url = "http://www.zhihu.com/"
opener = getOpener(header)
op = opener.open(url)
data = op.read()
data = ungzip(data)
_xsrf = getXSRF(data.decode())

url += 'login'
id = 'zhaosen2017'
password = 'zhaosenpassword'
postDict = {
    '_xsrf':_xsrf,
    'email':id,
    'password':password,
    'rememberme':'y'
}

postData = urllib.parse.urlencode(postDict).encode()
op = opener.open(url,postData)
data = op.read()
data = ungzip(data)

print(data.decode())
