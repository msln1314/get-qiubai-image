# -*- confing:utf-8 -*-
import re,urllib.request,time



def gethtml():
	url='http://nb.meituan.com/shop/799778?acm=UwunyailsW14099491663443770976.799778.1&mtt=1.index%2Fdefault%2Fpoi.pz.1.itjsm7e3&cks=17457#bdw'
	user_agent = 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
	
	headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
    'Accept-Encoding': 'none',
    'Accept-Language': 'en-US,en;q=0.8',
    'Connection': 'keep-alive'}
	page = urllib.request.Request(url=url,headers=headers)

	webpage = urllib.request.urlopen(page).read()
	
	imgre = re.compile(r'src="(.*?)" style')
	imglist = re.findall(imgre,webpage)
	
	for imgurl in imglist:
		print (imgurl)
		
		urllib.request.urlretrieve(imgurl,'d:\\糗百\%d.jpg'%x)
		
		x +=1
		time.sleep(5)
		print("正在下载第%d"%x)
		
gethtml()
	

