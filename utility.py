#cloudy-ngram/utility.py

import urllib2
import re
import math

memcached = {}# this to be replaced with an actual memcached server

def doc_frequency(ngram):
    """
    returns the number of documents from the web, which contains a particular ngram
    """
    if ngram in memcached:
        return memcached.get(ngram)
    
    words = ngram.split()
    query = '+'.join(words)
    #https://www.google.co.in/search?q=a&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-GB:official&client=firefox-a
    request = urllib2.Request('https://www.google.co.in/search?q="%s"&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-GB:official&client=firefox-a'%query)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')
    response = urllib2.urlopen(request)
    doc = response.read()
    
    #structure to scrape
    #<div id=resultStats>About 554,000,000 results<nobr>  (0.17 seconds)&nbsp;</nobr></div>
    regex = r'<div id=resultStats>About (.*?) results'
    match = re.search(regex,doc)
    result = match.group(1)
    result = float(result.replace(',',''))
    
    memcached[ngram] = result
    return result

def ngram_IDF(ngram):
    """
    computes the Inverse Document Frequency of a ngram in the Web corpus
    relevancy = term frequency * log (1 / document frequency)#TF-IDF
    This function returns log (1 / document frequency)
    """
    total_no_of_web_pages = 25270000000.0 # number of pages returned by searching for "the" or "a"
    return math.log(total_no_of_web_pages/doc_frequency(ngram),10)
    

print ngram_IDF("ancient polymath")# cold from google
print ngram_IDF("ancient polymath")# hot from cache

#to-do
#explore octopy map-reduce implementation
#write two functions , one for get and one for post, for general purpose scraping
#will use for seagator
#also, explore twisted..
#goodnight!
