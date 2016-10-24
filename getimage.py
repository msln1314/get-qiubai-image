# -*- confing:utf-8 -*-
import re,urllib.request,time,random
import requests


def gethtml(weburl):
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
	page = urllib.request.Request(url=url,headers=headers)

	webpage = urllib.request.urlopen(page).read()
	webpage = webpage.decode('gb2312')
	return webpage
x=32
headerdd={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11','Upgrade-Insecure-Requests':'1'}
def getimg(page):
	imgre = re.compile(r'src="(.*?)" style')
	imglist = re.findall(imgre,page)
	
	for imgurl in imglist:
		print (imgurl)
		global x
		r=requests.get(imgurl,headers=headerdd)
		with open('d:\\糗百\%d%d.jpg' % (x,x),'wb')as f:
			f.write(r.content)
		x +=1
		time.sleep(random.randint(10,15))
		print("正在下载第%d"%x)
		
for i in range(16,26):
	url='http://www.qiubaichengren.com/%d.html'%i
	page=gethtml(url)
	time.sleep(random.randint(5,10))
	print("正在打开第%d"%i)
	getimg(page)
