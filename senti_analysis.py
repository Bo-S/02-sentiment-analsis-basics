# -*- coding: utf-8 -*-



from os.path import os,join,dirname
from dotenv import load_dotenv
import tweepy


senti_dict = {}

with open('AFINN/AFINN-111.txt', 'r') as fhand:
    for line in fhand:
        k, v = line.strip().split('\t')
        senti_dict[k] = v

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

auth = tweepy.OAuthHandler(os.environ['consumer_key'], os.environ['consumer_secret'])
auth.set_access_token(os.environ['access_token'], os.environ['access_token_secret'])

client = tweepy.API(auth)
# print client

results = client.search(q='hilary clinton', lang='en')
# print results


for result in results:
    sentence = result.text.encode('utf-8')
    # print result.text
    senti_score = 0
    for (k,v) in senti_dict.items():
        if k in sentence.lower():
            senti_score += int(v)
    print sentence, senti_score



'''

senti_dict = {}

fhand = open('AFINN/AFINN-111.txt', 'r')
for line in fhand:
    line = line.strip()
    columns = line.split('\t')
    senti_dict[columns[0]] = columns[1]
#print senti_dict

sentence = raw_input('Enter text: ')
sentence_lowered = sentence.lower()

senti_score = 0
for (k,v) in senti_dict.items():
    if k in sentence_lowered:
        senti_score = senti_score + int(v)

print 'The sentiment score of %s is: %d' % (sentence, senti_score)

'''
