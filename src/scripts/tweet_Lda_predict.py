import sys
import re
import lda
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np
from sklearn.externals import joblib

def main():
	
	#cleanTweets = []
	#cleanTweetIds = []
	predictCleanTweets = []
	predictCleanTweetIds = []
       	topic_word = []
	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				tweetParts = line.strip('\n').strip().split(' ', 1)
				tweetId = tweetParts[0]
				tweetprob = [float(x) for x in tweetParts[1:]]
				topic_word.append(tweetprob)
				#cleanTweets.append(tweetText)
				#cleanTweetIds.append(tweetId)
			except Exception as e:
				#continue
				exit()
	
	#vectorizer = CountVectorizer(analyzer = "word",   \
        #                     tokenizer = None,    \
        #                     preprocessor = None, \
        #                     stop_words = None,   \
        #                     max_features = 300) 

	# fit_transform() does two functions: First, it fits the model
	# and learns the vocabulary; second, it transforms our training data
	# into feature vectors. The input to fit_transform should be a list of 
	# strings.
	#tweetDataFeatures = vectorizer.fit_transform(cleanTweets)

	# Numpy arrays are easy to work with, so convert the result to an 
	# array
	#tweetDataFeatures = tweetDataFeatures.toarray()
	#print tweetDataFeatures.shape
	# outFile = open(sys.argv[2], 'w') 
	# outFile.close()
	vectorizer = joblib.load(sys.argv[2])
	#vocab = vectorizer.get_feature_names()

	#loglikelihood = []
	#for numTopics in np.arange(5, 10, 5):
	#	model = lda.LDA(n_topics=numTopics, n_iter=100, random_state=1)
	#	model.fit(tweetDataFeatures)  # model.fit_transform(X) is also available
	#	loglikelihood.append(model.loglikelihood())


	
	#numTopics = 100 #5 + 5*np.argmax(loglikelihood) 
	#model = lda.LDA(n_topics=numTopics, n_iter=20, random_state=1)
	#model.fit(tweetDataFeatures)  # model.fit_transform(X) is also available
	#loglikelihood.append(model.loglikelihood())
	#docTopicFile = open(sys.argv[2], 'w')
	#docTopic = model.doc_topic_
	#for i in xrange(0,len(cleanTweets)):
	#	out = str(cleanTweetIds[i])
	#	for j in docTopic[i]:
	#		out += ' ' + str(j)
	#	docTopicFile.write(out + '\n')
	#docTopicFile.close()	

	#termTopicFile = open(sys.argv[3], 'w')
	#topic_word = model.topic_word_  # model.components_ also works
	#n_top_words = int(sys.argv[4])
	#for i, topic_dist in enumerate(topic_word):
	#	topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
	#	topic_words_prob = np.array(np.sort(topic_dist)[:-n_top_words:-1])
	#	out = str(i)
	#	for k in xrange(0,len(topic_words)):
	#		out += '#' + topic_words[k] + ' ' + str(topic_words_prob[k])
	#	termTopicFile.write(out + '\n')
	#termTopicFile.close()
	
	with open(sys.argv[3], 'r') as f:
		for line in f:
			try:
				tweetParts = line.strip('\n').strip().split(' ', 1)
				tweetId = tweetParts[0]
				tweetText = tweetParts[1]
				predictCleanTweets.append(tweetText)
				predictCleanTweetIds.append(tweetId)
			except Exception as e:
				continue

	tweetPredictDataFeatures = vectorizer.transform(predictCleanTweets)
	tweetPredictDataFeatures = tweetPredictDataFeatures.toarray()
	print tweetPredictDataFeatures.shape
	print tweetPredictDataFeatures[0]
	#a = model.predict(tweetPredictDataFeatures)
	#print a
	f = open(sys.argv[4], 'w')
	for i in xrange(0, len(predictCleanTweets)):
		topic_pred = []
		cumsum = 0.0
		for topic_dist in topic_word:
			sum = 0.0
			for p in xrange(0,len(topic_dist)):
				sum += topic_dist[p]*tweetPredictDataFeatures[i][p]	
			#sumArray = topic_dist*tweetPredictDataFeatures[i]
			#sum = 0.0
			#for j in sumArray:
			#	sum += j
			cumsum += sum
			topic_pred.append(sum)
			#print sum
		#print topic_pred
		#print cumsum
		for i in xrange(0, len(topic_pred)):
			topic_pred[i] /= cumsum
		#print topic_pred 		
		#break
		tempDict = {}
		tempDict[int(predictCleanTweetIds[i])] = topic_pred
		f.write(str(tempDict) + '\n')	
	f.close()



if __name__ == '__main__':
	main()
