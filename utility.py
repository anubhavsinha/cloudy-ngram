#cloudy-ngram/utility.py
#start with scraping google for number of results return for a typical query
#step1: visit google search url with the query string
import urllib2

def doc_frequency(ngram):
    words = ngram.split()
    query = '+'.join(words)
    request = urllib2.Request("http://google.com/search?q="+'"'+query+'"')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')
    response = urllib2.urlopen(request)
    doc = response.read()
    dump = open('dump.html','w')
    dump.write(doc)
    #to do
    #extract <div id="resultStats"> contents

doc_frequency("who is there")

def ngram_IDF(ngram):
    """calculates the Inverse Document Frequency of a ngram in the Web corpus"""
    total_no_of_web_pages = 25270000000.0#number of pages returned by searching for "the"
    return doc_frequency(ngram)/total_no_of_web_pages
    

