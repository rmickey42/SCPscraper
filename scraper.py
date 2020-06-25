import urllib.request
from bs4 import BeautifulSoup
import sys
import os

def getText(i):
	url = urllib.request.urlopen("http://www.scp-wiki.net/scp-{:03d}".format(i))
	b = url.read()
	st = b.decode("UTF-8")
	soup = BeautifulSoup(st, 'lxml')
	pageCont = soup.find('div', id="page-content")
	divs = pageCont.find_all('div')
	for d in divs:
		d.extract()
	para = pageCont.find_all('p')
	str = ""
	for p in para:
		str += p.text.rstrip() + "\n\n"
	return str

if(len(sys.argv) > 1 and sys.argv[1] == "-s"):
	with open("scps.txt", "a", encoding="utf-8") as f:
		for i in range(1, 1000):
			f.write(getText(i))
else:
	for i in range(1, 1000):
		with open("scps/scp-{}.txt".format(i), "a", encoding="utf-8") as f:
			f.write(getText(i))
