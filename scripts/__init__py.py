from subprocess import check_output
import re


out = check_output(['../phantomjs/phantomjs', '--ssl-protocol=any', \
    '--web-security=false', 'sniff.js', 'https://goodsports.com/'])

out = out.decode("utf-8")

urls = re.findall('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', out)
# print("Original string: ",text)

for url in urls:
    print(url)

#print("Urls: ",urls)
