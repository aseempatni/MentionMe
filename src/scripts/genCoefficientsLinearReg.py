from sklearn import linear_model
import numpy as np
import sys

def main():

	UserTweetLinks = {}
	UserReTweetLinks = {}
	tweetFeatures = eval(open(sys.argv[1], 'r').read().strip('\n')):

	with open(sys.argv[1], 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserTweetLinks[key] = set(value)


	with open(sys.argv[2], 'r') as f:
		for line in f:
			myDict = eval(line.strip('\n'))
			for key,value in myDict.items():
				UserReTweetLinks[key] = set(value)


	outfile = open(sys.argv[3], 'w')

	for user_id, tweetIDs in UserTweetLinks.items():
		if user_id in UserReTweetLinks.keys():
			tweetIdNotRetweeted = tweetIDs - UserReTweetLinks[user_id]
			tweetVec = []
			tweetTarget = []
			for tweetId in tweetIdNotRetweeted:
				if str(tweetId) in tweetFeatures.keys():
					tweetVec.append(tweetFeatures[str(tweetId)])
					tweetTarget.append(0)
			if len(tweetVec) > 0:
				continue
			tweetReVec = []
			tweetReTarget = []
			for tweetId in UserReTweetLinks[user_id]:
				if str(tweetId) in tweetFeatures.keys():
					tweetReVec.append(tweetFeatures[str(tweetId)])
					tweetReTarget.append(1)
			if len(tweetReVec) > 0:
				continue
				
			tweetVec += tweetReVec
			tweetTarget += tweetReTarget
					
			regr = linear_model.LinearRegression()
			regr.fit(a, b)
			tempDict = {}
			tempDict[user_id] = regr.coef_
			outfile.write(str(tempDict)+'\n')

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