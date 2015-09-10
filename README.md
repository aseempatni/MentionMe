# MentionMe

A mention recommendation system for Twitter.

In Twitter, mentioning (or tagging) users can be considered as an effective way of spreading an information beyond the reach of the followers. In this work, we want to devise a mention-recommendation system for popularizing tweets. We have done some works to figure out the key-driving factors which should be considered while choosing the users to be mentioned. Now, we are working on finding the best way to combine these factors so that we can rank the set of users to be mentioned. We also have to compare the accuracy & time-complexity of our system with state-of-the-art recommender systems.

## References

* [Modeling Adoption of Competing Products and Conventions in Social Media](http://arxiv.org/pdf/1406.0516v2.pdf)
* [Retweets—but Not Just Retweets: Quantifying and Predicting Influence on Twitter](http://www.eecs.harvard.edu/econcs/pubs/Rosenman_thesis.pdf)

## Instructions to use

#### LDA
* run ```python genCleanTweets.py validTweets.txt tempFileForCleanTweets.txt```. This will clean the tweets and generate in the follwing format ```<TweetId><space><Cleaned Tweet Text>```
* run ```python tweet_Lda.py tempFileForCleanTweets.txt docTopicFile.txt topicTermFile.txt numTopics```. This will generate the topics in the following format.:
  *  ```docTopicFile.txt : <docId><space><topic0 prob><space><topic1 prob>...```
  *  ```topicTermFile.txt : <topicId>#<term1><space><prob>#<term2><space><prob>...```
  
#### Feature Extraction
* run ```python extractFeatures.py ../data/algeria/ValidTweets.txt friendList_main.txt w_score ../data/algeria/CleanTweets.txt```. This will print the features dictionary which is a dictionary of list of features indexed by tweet Id in ```Features.txt```. w_score is for the ageing factor. friendListmain.txt should be of the format present in the algeria folder.

#### Linear Regression
* run ```python genCoefficientsLinearReg.py ../../data/algeria/Features.txt ../../data/algeria/UserTweetLinks.txt ../../data/algeria/UserReTweetLinks.txt ../../data/algeria/UserLinearRegCoeff.txt``` The output will be generated in the ```../../data/algeria/UserLinearRegCoeff.txt```.

#### fastCrawler

##### Prerequisite
* Put all the app keys in `config.json`
* List of user ids in `all_user_ids.json`

Now we are ready to start the crawler.
```
python main.py
```
All the user friends will be crawled and saved in `../../data/friend_id/`. It will automatically take care of following
* If the user's data is already present, it will be ignored.
* If data is absent, it will be crawled.
* TODO: If incomplete, then remaining data will be queried.
