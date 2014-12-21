import os, sys, json, shutil
from pprint import pprint

try:
	shutil.rmtree('reviews_dump')
except:
	pass

try:
	shutil.rmtree('ratings_dump')
except:
	pass

if not os.path.exists('reviews_dump'):
	os.makedirs('reviews_dump')

if not os.path.exists('ratings_dump'):
	os.makedirs('ratings_dump')

reviewDataset = open('yelp_academic_dataset_review.json', 'r')
businessDataset = open('yelp_academic_dataset_business.json', 'r')
reviewDatasetTest = open('yelp_academic_dataset_review_test.json', 'r')
businessDatasetTest = open('yelp_academic_dataset_business_test.json', 'r')

businessNameDict = {}
businessCount = {}


def filterSlash(string):
	for i in range(0, len(string)):
		if string[i] == '/':
			string = string[:i] +  ':' + string[i+1:]
	return string


for line in businessDataset:
	temp = json.loads(line)
	businessID = temp["business_id"]
	name = temp["name"]
	businessNameDict[businessID] = name



for line in reviewDataset:
	temp = json.loads(line)
	businessID = temp["business_id"]
	name = businessNameDict[businessID]
	rating = temp["stars"]
	review = temp["text"]
	
	try:
		businessCount[name] += 1
	except:
		businessCount[name] = 1

	reviewFolderPath = 'reviews_dump/' + name
	reviewID = name + '_' + str(businessCount[name])
	reviewOutputName = reviewID + '.txt'
	

	reviewFolderPath = 'reviews_dump/' + filterSlash(name)
	reviewOutputPath = reviewFolderPath + '/' + filterSlash(reviewOutputName)
	
	ratingOutputPath = 'ratings_dump/' + filterSlash(name) + '.txt'

	if not os.path.exists(reviewFolderPath):
		os.makedirs(reviewFolderPath)
	
	reviewOutput = open(reviewOutputPath, 'w')
	reviewOutput.write(review.encode('utf8'))
	reviewOutput.close()

	ratingOutput = open(ratingOutputPath, 'a')
	ratingOutputString = reviewID + ':' + str(rating) + '\n' 
	ratingOutput.write(ratingOutputString.encode('utf8'))
	ratingOutput.close()


reviewDataset.close()
businessDataset.close()
reviewDatasetTest.close()
businessDatasetTest.close()
