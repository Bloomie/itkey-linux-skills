import pymongo
from pymongo import MongoClient

import generate_docs

client = MongoClient('localhost', 27017)
db = client['test']

DOC_NUMBER = 1000
CHUNK_SIZE = 10000

for chunk in xrange CHUNK_SIZE:
	posts = []
	for i in xrange(0, DOC_NUMBER):
		doc = generate_docs.generate_doc()
		doc['_id'] = i
		posts.append(doc)
		db.testcol.insert_many(posts)

# print 'searching', doc['name']
# for post in db.testcol.find({"name": doc['name']}):
# 	print post