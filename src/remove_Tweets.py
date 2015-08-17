def main() :
	in_file = open("All_Tweet_IDs.txt","r")
	input_file = open("../Tweets.txt","r")
	output_file = open("Filtered_Tweets.txt","w")
	data = in_file.read()
	lines = data.split("\n")
	tweet_ids = set()
	print "Reading Tweet Ids"
	for line in lines :
		if(len(line) > 0) :	
			tweet_ids.add(str(line))

	print "Tweet IDs read", len(tweet_ids)
	# print tweet_ids
	data = input_file.read()
	lines = data.split('\n')
	i = 0
	for line in lines :
		i += 1
		if(i % 10000 == 0) :
			print (i / 10000), "done"
		try :
			if len(line) > 0 :
				mydict = eval(line)
				if 'retweeted_status' in mydict : 
					if 'id' in mydict['retweeted_status'] :
						# print mydict['retweeted_status']['id']
						if str(mydict['retweeted_status']['id']) in tweet_ids :
							#print str(mydict)
							output_file.write(str(mydict) + '\n')
				else :
					output_file.write(str(mydict) + '\n')
		except Exception :		
			continue

if __name__ == "__main__" :
	main()
