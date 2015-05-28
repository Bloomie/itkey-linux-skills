import pymongo
from pymongo import MongoClient

import generate_docs

client = MongoClient('localhost', 27017)
db = client['test']

AGE = ""
NAME = ""

print 'searching: name = %(name)s ,age = %(age)s' % {'name': NAME, 'age': AGE}
for post in db.posts.find({"name": NAME, "age": AGE}):
	print post