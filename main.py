#not really fix utf8 problem
#!/usr/bin/env python
# -*- coding: utf-8 -*-

#import library
import requests
from lxml import html

#not really fix utf8 problem
import sys
reload(sys)
sys.setdefaultencoding('utf8')

#get html source
url = 'http://rate.bot.com.tw/Pages/Static/UIP003.zh-TW.htm'
r = requests.get(url)
#requests.setCharacterEncoding("UTF-8");
#r.text.encode("utf-8")
#print r.text

#save to file
data = open('data.html', 'w')
data.write(r.text)
data.close()

#Parse Pages
#tree = html.fromstring(r.text)
tree = html.fromstring(r.content)

#for table in tree.xpath('//table[2]'):
#for table in tree.xpath('//table[1]'):
#table = tree.xpath('//table[2]')
#print table
#fail
#for tr in table.xpath('//tbody/tr'):
#fail
#for tr in tree.xpath('//table[2]/tbody/tr'):
#for tr in tree.xpath('//table[2]/tr'):
#ok
#for tr in tree.xpath('//table[1]/tr'):
#ok
print "==================================="
currency_name = tree.xpath('//table[2]/tr/td[@class="titleLeft"]/text()')
#print td_name
for i in range(0, len(currency_name), 1):
    print currency_name[i]
    #for td in tr.xpath('//td[@class="titleLeft"]'):
    #    print "============================="
    #    print td.text
        #for img in td.xpath('//img[@class="paddingLeft16"]'):
        #	print img.text
    #    print "============================="
    currency_value = tree.xpath('//table[2]/tr/td[@class="decimal"]/text()')
    print currency_value[i*4]
    print currency_value[i*4+1]
    print currency_value[i*4+2]
    print currency_value[i*4+3]
    	#for td in tr.xpath('//td[@class="decimal"]'):
     	#    print "*****************************"
    	#    print td.text
    	#    print "*****************************"


