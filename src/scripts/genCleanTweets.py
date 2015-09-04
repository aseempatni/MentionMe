import lda
from sklearn.feature_extraction.text import CountVectorizer
import sys
from bs4 import BeautifulSoup 
import re
import nltk
from nltk.corpus import stopwords
stop = stopwords.words('english')

days = ['Monday','Tuesday','Wednesday','Thurday','Friday','Saturday','Sunday']
months = ['January','February','March','April','May','June','July','August','September','October','November','December']

def main():
	outFile = open(sys.argv[2], 'w') 
	with open(sys.argv[1], 'r') as f:
		for line in f:
			try:
				mydict = eval(line)
				tweetId = mydict['id']
				text = BeautifulSoup(mydict['text']).get_text()
				text = re.sub('http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+', ' HYPERLINK ', text)
				text = re.sub('%', ' PERCENTAGE ', text)
				text = re.sub('\$', ' DOLLAR ', text)
				text = re.sub('@\w+', ' ', text)
				text = re.sub('\d+:\d+', ' TIME ', text)
				text = re.sub('(^\d+)|( \d+ )|(\d+$)', ' NUMBER ', text)
				for day in days:
					text = text.replace(day,' DAY ')	
				for month in months:
					text = text.replace(month,' MONTH ')	
				text = re.sub('\W+', ' ', text) 
				text = text.strip()
				text = text.lower()
				textWords = text.split()
				filteredText = ''
				for textWord in textWords:
					if len(textWord)>3 and textWord not in stop:	
						filteredText += ' ' + textWord
				filteredText = filteredText.strip()		
				if len(filteredText) > 0:
					outFile.write(str(tweetId) + ' ' + filteredText + '\n')
			except Exception as e:
				continue 
	outFile.close()

if __name__ == '__main__':
	main()