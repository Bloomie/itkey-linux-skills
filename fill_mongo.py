import pymongo
from pymongo import MongoClient
import os
from threading import Thread
from time import sleep

import generate_docs

client = MongoClient('localhost', 27017)
db = client['testdb']

DOC_NUMBER = 1000
CHUNK_SIZE = 625

START_POINT = 0

search_data = []

def run(start_index):
    for chunk in xrange(0, CHUNK_SIZE):
        posts = []
        for i in xrange(0, DOC_NUMBER):
                doc = generate_docs.generate_doc()
                doc['_id'] = start_index + i + chunk * 1000
                posts.append(doc)
        db.testcol.insert_many(posts)
        print chunk
        search_data.append(posts[0])


processes = []

threads = []

for i in xrange(0, 4):
        t = Thread(target=run, args=(i * 2500000 + START_POINT,))
        threads.append(t)
        t.start()


for i in xrange(0, 4):
        threads[i].join()


with open("mongo_search_data", "w") as f:
    for item in search_data:
        f.write('%s\n' % item)
