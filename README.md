# MentionMe
A mention Recommendation System for Twitter.

## References

* [Modeling Adoption of Competing Products and Conventions in Social Media](http://arxiv.org/pdf/1406.0516v2.pdf)
* [Retweets—but Not Just Retweets: Quantifying and Predicting Influence on Twitter](http://www.eecs.harvard.edu/econcs/pubs/Rosenman_thesis.pdf)

## Todos

#### Clean Tweets
* Remove re-tweets whose original tweet is not present.

#### Make graphs

* Make re-tweet graph
* Make mention graph
* Make follower graph

#### Get user data
* Crawl user tweets.
* Find user interests.
* Get followers/following to construct network.

#### Mention Ranking
* Find a mention success score evaluation function.
* Learn the parameters.
* Function to recommend top k mentions given a tweet.

#### Web Interface
* Create a web interface for online prediction of mentions given a tweet

#### LDA
* run ```python genCleanTweets.py validTweets.txt tempFileForCleanTweets.txt```. This will clean the tweets and generate in the follwing format ```<TweetId><space><Cleaned Tweet Text>```
* run ```python tweet_Lda.py tempFileForCleanTweets.txt docTopicFile.txt topicTermFile.txt numTopics```. This will generate the topics in the following format.:
  *  ```docTopicFile.txt : <docId><space><topic0 prob><space><topic1 prob>...```
  *  ```topicTermFile.txt : <topicId>#<term1><space><prob>#<term2><space><prob>...```
  
#### Feature Extraction
* run ```python extractFeatures.py ValidTweets.txt friendList_main.txt w_score```. This will print the features dictionary which is a dictionary of list of features indexed by tweet Id in ```Features.txt```. w_score is for the ageing factor. friendListmain.txt should be of the format present in the algeria folder.
