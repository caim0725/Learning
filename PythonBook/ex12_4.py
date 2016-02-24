import urllib
from bs4 import BeautifulSoup

url = raw_input('URL: ')
try:
    html = urllib.urlopen(url).read()
    soup = BeautifulSoup(html,"html.parser")
    
except:
    print "Wrong URL!"
    exit()
tags =soup('p')
print len(tags)