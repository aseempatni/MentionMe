from sklearn import linear_model
import numpy as np
import sys
from extractFeatures import *
from sklearn import cross_validation

def main():

	UserTweetLinks = {}
	UserReTweetLinks = {}
	#tweetFeatures = getFeatures('../../data/algeria/ValidTweets.txt', '../friendList_main.txt', -0.000004, '../../data/algeria/CleanTweets.txt', '../../data/algeria/TweetDocTopic.txt')
	tweetFeatures = {}
	with open(sys.argv[1], 'r') as f:
		for line in f:
			mydict = eval(line.strip('\n'))
			for key,value in mydict.items():
				user_id,tweet_id = key
				if user_id not in tweetFeatures.keys():
					tweetFeatures[user_id] = {}
				tweetFeatures[user_id][tweet_id] = value
	
	with open(sys.argv[2], 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserTweetLinks[key] = set(value)


	with open(sys.argv[3], 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserReTweetLinks[key] = set(value)

	outfile = open(sys.argv[4], 'w')

	for user_id, tweetIDs in UserTweetLinks.items():
		if user_id not in tweetFeatures.keys():
			continue
		if user_id in UserReTweetLinks.keys():
			tweetIdNotRetweeted = tweetIDs - UserReTweetLinks[user_id]
			tweetVec = []
			tweetTarget = []
			for tweetId in tweetIdNotRetweeted:
				if str(tweetId) in tweetFeatures[user_id].keys():
					tweetVec.append(tweetFeatures[user_id][tweetId][1:])
					tweetTarget.append(-1)
			#print "Tweeted : ", tweetVec, tweetTarget
			if len(tweetVec) <= 0:
				continue
			tweetReVec = []
			tweetReTarget = []
			for tweetId in UserReTweetLinks[user_id]:
				if str(tweetId) in tweetFeatures[user_id].keys():
					tweetReVec.append(tweetFeatures[user_id][tweetId][1:])
					tweetReTarget.append(1)
			#print "Retweeted : ", tweetReVec, tweetTarget
			if len(tweetReVec) <= 0:
				continue
				
			tweetVec += tweetReVec
			tweetTarget += tweetReTarget
			
			try:		
				tempDict = {}
				#tempDict[user_id] = {}
				#tempDict[user_id]['meanSquare'] = []
				#tempDict[user_id]['variance'] = []
				#kf = cross_validation.KFold(len(tweetTarget), n_folds=5)
			
				#for train_index, test_index in kf:
				#	X_train, X_test = tweetVec[train_index], tweetVec[test_index]
				#	y_train, y_test = tweetTarget[train_index], tweetTarget[test_index]
				#	regr = linear_model.LinearRegression()
				#	regr.fit(X_train, y_train)
				#	tempDict[user_id]['meanSquare'].append(float(np.mean((regr.predict(X_test) - y_test) ** 2)))
				#	tempDict[user_id]['variance'].append(float(regr.score(X_test, y_test)))
				
				
				#tempDict[user_id]['averageMeanSquare'] = float(np.mean(tempDict[user_id]['meanSquare']))
				#tempDict[user_id]['averageVariance'] = float(np.mean(tempDict[user_id]['variance']))
				regr = linear_model.LinearRegression()
				regr.fit(tweetVec,tweetTarget)
				tempDict[user_id] = list(regr.coef_)
				outfile.write(str(tempDict)+'\n')
			
			except Exception as e:
				print e
				continue
			#break

	outfile.close()


if __name__ == '__main__':
	main()

# a = [[1,2],[2,1]]
# b = [1,2]
# regr = linear_model.LinearRegression()
# regr.fit(a, b)
# print('Coefficients: \n', regr.coef_)
# # The mean square error
# print("Residual sum of squares: %.2f"
#       % np.mean((regr.predict(X_test) - y_test) ** 2))
# # Explained variance score: 1 is perfect prediction
# print('Variance score: %.2f' % regr.score(X_test, y_test))
# array([ 0.5, -0.5])

# from sklearn import cross_validation
# >>> X = np.array([[1, 2], [3, 4], [1, 2], [3, 4]])
# >>> y = np.array([1, 2, 3, 4])
# >>> kf = cross_validation.KFold(4, n_folds=2)
# >>> len(kf)
# 2
# >>> print(kf)  
# sklearn.cross_validation.KFold(n=4, n_folds=2, shuffle=False,
#                                random_state=None)
# >>> for train_index, test_index in kf:
# ...    print("TRAIN:", train_index, "TEST:", test_index)
# ...    X_train, X_test = X[train_index], X[test_index]
# ...    y_train, y_test = y[train_index], y[test_index]
