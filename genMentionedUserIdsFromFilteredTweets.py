def main() :
	inputFile = open("Agnivo/Filtered_Tweets.txt","r")
	outputFile = open("mentionedUserIdsFromFilteredTweets.json","w")
	user_ids = set()
	i = 0
	for line in inputFile :
		line = line.strip('\n').strip()
		i += 1
		if(i % 10000 == 0) :
			print (i / 10000), "done"
		try :
			if len(line) > 0 :
				mydict = eval(line)
				tweet_id = mydict['id']
				user_id = mydict['user']['id']
				user_ids.add(user_id)
				
				if 'retweeted_status' in mydict : 
					orig_user_id = mydict['retweeted_status']['user']['id']
					for user_mention in mydict['entities']['user_mentions'] :
						user_id = user_mention['id']
						user_ids.add(user_id)

		except Exception as e :	
			continue

		
	outputFile.write( str(list(user_ids)) + '\n' ) 

	inputFile.close()
	outputFile.close()

if __name__ == "__main__" :
	main()