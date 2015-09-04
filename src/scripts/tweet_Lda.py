import sys
import re
import lda
from sklearn.feature_extraction.text import CountVectorizer
import numpy as np


def main():
	
	cleanTweets = []
	cleanTweetIds = []

	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				tweetParts = line.strip('\n').strip().split(' ', 1)
				tweetId = tweetParts[0]
				tweetText = tweetParts[1]
				cleanTweets.append(tweetText)
				cleanTweetIds.append(tweetId)
			except Exception as e:
				continue
	
	vectorizer = CountVectorizer(analyzer = "word",   \
                             tokenizer = None,    \
                             preprocessor = None, \
                             stop_words = None,   \
                             max_features = 300) 

	# fit_transform() does two functions: First, it fits the model
	# and learns the vocabulary; second, it transforms our training data
	# into feature vectors. The input to fit_transform should be a list of 
	# strings.
	tweetDataFeatures = vectorizer.fit_transform(cleanTweets)

	# Numpy arrays are easy to work with, so convert the result to an 
	# array
	tweetDataFeatures = tweetDataFeatures.toarray()
	print tweetDataFeatures.shape
	# outFile = open(sys.argv[2], 'w') 
	# outFile.close()

	vocab = vectorizer.get_feature_names()

	#loglikelihood = []
	#for numTopics in np.arange(5, 10, 5):
	#	model = lda.LDA(n_topics=numTopics, n_iter=100, random_state=1)
	#	model.fit(tweetDataFeatures)  # model.fit_transform(X) is also available
	#	loglikelihood.append(model.loglikelihood())


	
	numTopics = 100 #5 + 5*np.argmax(loglikelihood) 
	model = lda.LDA(n_topics=numTopics, n_iter=100, random_state=1)
	model.fit(tweetDataFeatures)  # model.fit_transform(X) is also available
	#loglikelihood.append(model.loglikelihood())
	docTopicFile = open(sys.argv[2], 'w')
	docTopic = model.doc_topic_
	for i in xrange(0,len(cleanTweets)):
		out = str(cleanTweetIds[i])
		for j in docTopic[i]:
			out += ' ' + str(j)
		docTopicFile.write(out + '\n')
	docTopicFile.close()	

	termTopicFile = open(sys.argv[3], 'w')
	topic_word = model.topic_word_  # model.components_ also works
	n_top_words = int(sys.argv[4])
	for i, topic_dist in enumerate(topic_word):
		topic_words = np.array(vocab)[np.argsort(topic_dist)][:-n_top_words:-1]
		topic_words_prob = np.array(np.sort(topic_dist)[:-n_top_words:-1])
		out = str(i)
		for k in xrange(0,len(topic_words)):
			out += '#' + topic_words[k] + ' ' + str(topic_words_prob[k])
		termTopicFile.write(out + '\n')
	termTopicFile.close()
	




if __name__ == '__main__':
	main()
