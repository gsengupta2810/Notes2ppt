#changeTopicHere. Has been used as a symbol for denoting the end of a topic 
def find_topic(data):
	# determine the topic name of the subject in concern 
	topics=[]
	for x in xrange(0,len(data)):
		i=0
		while data[x].split('\n')[i]=="":
			i+=1
		else:
			topics.append(data[x].split('\n')[i])
			temp=data[x].split('\n')
			temp.remove(data[x].split('\n')[i])
			data[x]="".join(temp)
	return topics,data

import nltk.data
def split_sentences_nltk(file): #returns the topcs separated into sentenses and topic titles
	try:
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	except:	
		nltk.download('punkt') # needed only for the first time 
		tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
	data = file.read() 
	data_1=data.split("changeTopicHere.")
	topics,data_1=find_topic(data_1)
	topics_data=[]
	i=0
	for x in xrange(0,len(data_1)):
		topics_data.append("\n".join(tokenizer.tokenize(data_1[x])))
	return topics,topics_data

if __name__ == '__main__':
	file=open('./test_extracted_data_for_ppt.txt','r')
	topics,topic_data=split_sentences_nltk(file)
	print topics[0]+"\n"+topic_data[0]

	
