#   ____                    _       
#  / ___|_ __ __ ___      _| |_   _ 
# | |   | '__/ _` \ \ /\ / / | | | |
# | |___| | | (_| |\ V  V /| | |_| |
#  \____|_|  \__,_| \_/\_/ |_|\__, |
#                             |___/ 
#
# Scripted By Atlas Lion Version 0.2

# Search Engine Crawler : [Link, Text, Images, Videos, Email, Books, Documents]
# example : crawly -e bing -p 10 -k "site:fr @outlook.com 2019" --email --unique --valide 
#           crawly -e bing -p 20 -k "site:fr shop php id" --link --unique --valide
#		    crawly shell --nolog
#           crawly -d "https://crawly.io/" --map 

# to do list
			# keyword match & rotation & maping
			# authentication
			# captcha solving
			# mail checker 
			# database
			# threading
			# dashboard
			# cms detection
			# image recognition
			# metadata
			# ip rotation

import requests
import random
import lxml.html
import re
import sys
from lxml import etree


# config
url      = 'https://www.bing.com/search?q='
log_file = 'log.txt'
dex_file = 'desc.txt'
index    = 9
ind 	 = "&go=Submit+Query&qs=ds&first="
dex      = "&FORM=PERE1"
# choice   = input('choice > ')
# keyword  = input('search > ')
string   = ''
engine   = 'bing'
ran      = 40
site_out = "output.txt"
desc_out = "desc.txt"
choice   = "1"
# keyword  = str("ip" +"%3a" +"198.71.53.226")
keyword  = "ip:191.53.12.14"

country  = 'site:fr'

keywords = ['@outlook.com',
			'@hotmail.fr',
			'@hotmail.com',
			'@outlook.fr',
			'@gmail.com',
			'@yahoo.com',
			'@aol.fr'
			'sfr.fr'
			]


years     = ['2017', '2018', '2019']


user_agent_list = [
   #Chrome
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 5.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36',
    'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/44.0.2403.157 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    #Firefox
    'Mozilla/4.0 (compatible; MSIE 9.0; Windows NT 6.1)',
    'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; WOW64; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 6.2; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (Windows NT 10.0; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)',
    'Mozilla/5.0 (Windows NT 6.1; Win64; x64; Trident/7.0; rv:11.0) like Gecko',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; WOW64; Trident/6.0)',
    'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.1; Trident/6.0)',
    'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)'
]





# get websites
def get_sites(url):
	user_agent = random.choice(user_agent_list)
	headers = {'User-Agent': user_agent}
	response = requests.get(url, headers=headers)
	html = response.content
	# parser = etree.ETCompatXMLParser()
	htmltree = lxml.html.fromstring(html)
	reg = "http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+"
	try: 
		for input_el in htmltree.xpath('//a'):
		    name = input_el.attrib['href']
		    if (re.match(reg, name)):
		    	site = name.split("//")[-1].split("/")[0].split('?')[0]
		    	with open("log.txt", "a") as myfile:
				    myfile.write(site + "\n")
	except:
		print("Get Sits !")

# get description
def get_description(url):
	user_agent = random.choice(user_agent_list)
	headers = {'User-Agent': user_agent}
	response = requests.get(url, headers=headers)
	html = response.content
	htmltree = lxml.html.fromstring(html)
	reg = "^[a-zA-Z0-9.!#$%&'*+/=?^_`{|}~-]+@[A-Z0-9.-]+\.[A-Z]{2,}$"
	try: 
		for tag in htmltree.xpath('//p'):
		    for p in tag:
		    	d = p.text_content()
		    	with open("desc.txt", "a") as myfile:
				    myfile.write(d + "\n")
	except:
		print("Get Description !")



def search(url, keyword, index):
	print("[*] Search Key %s Engine %s" % (keyword,engine))
	for x in range(ran):

		url += keyword + ind + str(index) + dex
		if (choice == '1'):
			
			get_sites(url)
			index += 10
			progress(x ,ran)

		if (choice == '2'):
			get_description(url)
			index += 10
			progress(x ,ran)

	print("\n[*] Saved to %s" % log_file)





def progress(count, total, suffix=''):
    bar_len = 60
    filled_len = int(round(bar_len * count / float(total)))
    percents = round(100.0 * count / float(total), 1)
    bar = '=' * filled_len + '-' * (bar_len - filled_len)
    sys.stdout.write('[%s] %s%s ...%s\r' % (bar, percents, '%', suffix))
    sys.stdout.flush()  # As suggested by Rom Ruben



search(url, keyword, index)


seen = set()
with open('log.txt') as infile:
	with open('output.txt', 'w') as outfile:
	    for line in infile:
	        if line not in seen:
	            outfile.write(line)
	            seen.add(line)



seen = set()
with open('desc.txt') as infile:
	with open('emails.txt', 'w') as outfile:
		for line in infile:
			if line not in seen:
				emails = re.findall("([a-zA-Z0-9_.-]+@[a-zA-Z0-9-]+\.[a-zA-Z]+)", line)
				if (emails):
					emails = '\n'.join(emails)
					outfile.write(emails+"\n")
					seen.add(line)




