import requests
import re

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; intel Mac OS X 10_11_4) AppleWebKit/537.36 (KHTML, Like Gecko) '
                  'Chrome/52.0.2743.116 Safari/537.36'
}
r = requests.get("http://jandan.net/treehole", headers=headers)
pattern = re.compile('</a></span><p>(.*?)</p>', re.S)
groups = re.findall(pattern, r.text)
print(type(groups))
for text in groups:
    print(text)
    print('===========================')


