import ast
from collections import defaultdict
import re, math
from collections import Counter

WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

filename = "Tweets.txt"

fp = open(filename,'r')

originalTweets = []

for line in fp:
	line = line.rstrip()
	try:
		myDict = ast.literal_eval(line)
	except:
		continue
	
	retweetedStatus = False
	try:
		retweet = myDict['retweeted_status']
		retweetedStatus = True
	except:
		pass
	
	if not retweetedStatus:
		try:
			hashtags = [str(x['text']) for x in myDict['entities']['hashtags']]
			mentions = [x['id'] for x in myDict['entities']['user_mentions']]
			text = str(myDict['text'])
			originalTweets.append((text,hashtags,mentions))
		except:
			pass

originalTweetCount = len(originalTweets)

for index1 in range(originalTweetCount-1):
	for index2 in range(index1+1,originalTweetCount):
		text1 = originalTweets[index1][0]
		text2 = originalTweets[index2][0]
	  
		hashtag1 = originalTweets[index1][1]
		hashtag2 = originalTweets[index2][1]

		mention1 = originalTweets[index1][2]
		mention2 = originalTweets[index2][2]

                vector1 = text_to_vector(text1)
                vector2 = text_to_vector(text2)
		
		cosine = get_cosine(vector1, vector2)
		print cosine, hashtag1,hashtag2,mention1,mention2

		 		
