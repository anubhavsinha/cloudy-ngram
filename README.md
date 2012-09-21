cloudy-ngram
============

cloudy-ngram: is a REST service which provides you the IDF of Unigrams, Bigrams..Ngrams upro N = 5.   
The service will be helpful for applications in the NLP domain, for eg. text-summarization, computational advertising etc.  
    
As of now, to get the IDF value taking all of the web as your corpus, your only bet is the Google N-gram corpus  
which is a 25Gb size corpus and needs heavy distributed processing (MapReduce etc) to get the IDF.  

Cloudy-ngram makes it easy for everyone to have a free, fast IDF lookup on the cloud.    
It will cache the IDF values eventually with use.  


###tf-idf approach from information theory perspective