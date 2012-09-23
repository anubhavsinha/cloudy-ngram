import urllib2
import nltk
import lxml.html.clean as lhc

def text_from_url(url):
    #url = 'http://en.wikipedia.org/wiki/Memcached'
    request = urllib2.Request(url)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')
    response = urllib2.urlopen(request)
    doc = response.read()
    doc = unicode(doc,'utf-8')#alex martelli said this
    cleaned_html = lhc.clean_html(doc)
    only_text = nltk.clean_html(cleaned_html)
    text = only_text.encode('utf-8')#alex martelli..
    #print text
    #f = open('text.txt','w')
    #f.write(text)
    #f.close()

url = 'http://en.wikipedia.org/wiki/.NET_Framework'
text_from_url(url)
