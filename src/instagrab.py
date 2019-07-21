import requests
from bs4 import BeautifulSoup

def geturls(url):
	headers = {
	            'Content-Type': 'application/x-www-form-urlencoded',
	            'Origin': 'http://instagrab.ru',
	            'Upgrade-Insecure-Requests': '1',
	            'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:47.0) Gecko/20100101 Firefox/47.0',
	            'Accept': 'text/html,application/xhtml+xml'
	          }
        if not url[-1] == "/":
            url += "/"
	response = requests.post('http://instagrab.ru/', headers=headers, data={'url': url})

	soup = BeautifulSoup(response.text, 'html.parser')
	imglist = soup.find_all(class_='image-download')

	urllist = list()
	for x in imglist:
	    urllist.append(x['href'])
	if(len(urllist) == 0):
		return -1
	elif(len(urllist) == 1):
		return urllist[0].encode('ascii', 'ignore')
	else:
		return urllist
