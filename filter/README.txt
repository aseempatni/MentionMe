
************************************Important files*****************************************************************************************************


"Tweets.txt": This file contains all the tweets crawled from twitter (13,50,984)


"bachuUser_new.py": this file contains the python code extracting the tweet IDs of all tweets present in the file "Tweets.txt"

"All_tweetIDs.txt": This file contains the tweet IDs of all tweets in file "Tweets.txt". Output file of "bachuUser_new.py"

"selected_tweets.py": This file contains the python code for selecting the particular tweets that contain retweeted_status and the tweet id in this section is also present in the file named "All_tweetIDs.txt"

"original23_tweets.txt": This file contains the filtered tweets, generated as the output of file "selected_tweets.py".

"filter_user_id.py": This file contains the python code for generating the user ids of all filtered tweets contained in "original23_tweets.txt".

"filtered_user_id.txt": this file contains the output of the file "filter_user_id.py"

"filter_mention_id.py': this file contains the python code for extracting the mention ids from the filtered tweets contained in "original23_tweets.txt"

"tweet_mention_id23.txt": this file contain the output of the file "filter_mention_id.py"

"unique_user_ids.py": this python code will filter duplicate user and mention ids 

"unique_user2_ids.txt": this file contains a unique user id after removing duplicate user ids from the file "filtered_user_id.txt" (76,891 unique user ids)

*********************************************ENDS HERE***************************************************************************************************




*****************start final_egypt_friend_list directory*****************

below files are present inside the directory

"appDetail_accTok_modified_get_friends.txt": this file contains the consumer Key and consumer secret separated by comma

"My_API_Key.txt" This file contains the App Key and App details  from the above file that are currently working fine.

"modified_get_friends.py": this file contains the python code for crawlling the friend lists 

"modified_run_get_friends.sh": this is the shell file for running the above file for multiple users simultaneously. Before running this file make sure all the users are divided into 33 files

 "modified_get_friend_network.py": this file contains the python code for creating the friend network. It takes the output of the above file (out1,out2,out3,...) as its own inputs and generate its output files as friend_network1,friend_network2...

 "modified_run_get_friend_network.sh": this is the shell file that will run for above file for multiple users simultaneously

"function.py": this file is requied to create friend netork. this file must be present in the same directory as the above two files

"divide_user.py': this python code will automatically divides all users(whose friend list is to be crawled) into 33 files. 



*******************END fianl_egypt_friend_list directory*****************


