#cloudy-ngram/utility.py
#start with scraping google for number of results return for a typical query
#step1: visit google search url with the query string
import urllib2
import re
import math

def doc_frequency(ngram):
    words = ngram.split()
    query = '+'.join(words)
    #https://www.google.co.in/search?q=a&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-GB:official&client=firefox-a
    request = urllib2.Request('https://www.google.co.in/search?q="%s"&ie=utf-8&oe=utf-8&aq=t&rls=org.mozilla:en-GB:official&client=firefox-a'%query)
    request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:15.0) Gecko/20100101 Firefox/15.0.1')
    #more headers may be set, like gzip deflate etc.
    response = urllib2.urlopen(request)
    doc = response.read()
    #f = open("dump.html","w")
    #f.write(doc)
    
    #structure to scrape
    #<div id=resultStats>About 554,000,000 results<nobr>  (0.17 seconds)&nbsp;</nobr></div>
    regex = r'<div id=resultStats>About (.*?) results'
    match = re.search(regex,doc)
    result = match.group(1)
    result = result.replace(',','')
    return float(result)

#print doc_frequency("the")



def ngram_IDF(ngram):
    """
    calculates the Inverse Document Frequency of a ngram in the Web corpus
    relevancy = term frequency * log (1 / document frequency)
    This function returns log (1 / document frequency)
    """
    total_no_of_web_pages = 25270000000.0#number of pages returned by searching for "the" or "a"
    return math.log(total_no_of_web_pages/doc_frequency(ngram),10)
    

print ngram_IDF("ancient polymath")
