#cloudy-ngram/utility.py
#start with scraping google for number of results return for a typical query
#step1: visit google search url with the query string
import urllib2
import re

def doc_frequency(ngram):
    words = ngram.split()
    query = '+'.join(words)
    request = urllib2.Request("http://google.com/search?q="+'"'+query+'"')
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')
    #more headers to set, to fool google
    response = urllib2.urlopen(request)
    doc = response.read()
    f = open("dump.html","w")
    f.write(doc)
    #structure to scrape
    #<div id=resultStats>About 554,000,000 results<nobr>  (0.17 seconds)&nbsp;</nobr></div>
    regex = r'<div id=resultStats>About (.*?) results'
    match = re.search(regex,doc)
    result = match.group(1)
    result = result.replace(',','')
    return float(result)

print doc_frequency("the")

def ngram_IDF(ngram):
    """calculates the Inverse Document Frequency of a ngram in the Web corpus"""
    total_no_of_web_pages = 25270000000.0#number of pages returned by searching for "the"
    return doc_frequency(ngram)/total_no_of_web_pages
    

print ngram_IDF("the")
