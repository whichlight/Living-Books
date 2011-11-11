'''
Living Books 

A script to pull text randomly from a book, and tweet it
This is part of an initiative to 'free' the data of books, and eventually make
them more interactive in the virtual public space. 

www.whichlight.com
@kawantum
github: whichlight

'''
import twitter
import math 
import random
import datetime
import time 

#globals
log = "log.txt"
book_file = "location_of_book.txt"

def validate():
	api = twitter.Api(consumer_key='', 
	consumer_secret = '', 
	access_token_key='',		
	access_token_secret= '')
	return api	
	
def openBook(book):
	file = open(book, 'r')
	text = file.read()
	return text

def getRandomPhrase(text):
	b=random.randint(0,(len(text)-140))
	sub = text[b:b+140]
	return sub

def logTweet(tweet):
	out = open(log,'wa')
	time = datetime.datetime.now()
	out.write(str(time)+'\t'+tweet+'\n')	
	out.close()
	print time
	print tweet 

def tweet_out():
	api = validate()
	text = openBook(name_of_book)		
	tweet = getRandomPhrase(text)
	#tweet = "testing"
	api.PostUpdate(tweet)		
	logTweet(tweet)
	


if __name__=="__main__":
	next_time = time.time()
	
	
	while True: 	
		tweet_out()
		
		#this determines the delay before the next tweet
		next_time+=random.randint(3600,7200) 
		while True:
			time.sleep(60)
			if (time.time()>next_time):
				next_time=time.time()
				break
