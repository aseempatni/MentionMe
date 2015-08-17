def main() :
	in_file = open("Tweets.txt","r")
	output_file = open("All_Tweet_IDs.txt","w")
	data = in_file.read()
	lines = data.split("\n")
	tweet_ids = set()
	i = 0
	for line in lines :
		i += 1
		if i % 10000 == 0 :
			print (i/10000), "done"
		try :
			if len(line) > 0 :
				mydict = eval(line)
				tweet_ids.add(mydict['id'])
		except Exception :		
			continue	

	for tweetId in tweet_ids :
		output_file.write(str(tweetId) + '\n')

if __name__ == "__main__" :
	main()
