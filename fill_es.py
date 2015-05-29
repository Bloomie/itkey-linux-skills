import elasticsearch

from time import sleep
from threading import Thread

import generate_docs

CHUNK_SIZE = 1250
DOC_NUMBER = 1000

INDEX_NAME = 'test'
TYPE_NAME = 'document'

search_data = []

def run(start_index):
	es = elasticsearch.Elasticsearch([{'host': '10.2.55.145', 'port': 9200}])
	for chunk in xrange(0, CHUNK_SIZE):
		bulk_data = []
		for i in xrange(0, DOC_NUMBER):
			op_dict = {
		        "index": {
		        	"_index": INDEX_NAME, 
		        	"_type": TYPE_NAME, 
		        	"_id": start_index + i + chunk * 1000
		        }
		    }
			doc = generate_docs.generate_doc()
			bulk_data.append(op_dict)
			bulk_data.append(doc)
		try:
			es.bulk(index=INDEX_NAME, body=bulk_data, refresh=True)
		except:
			sleep(20)
			print "sleeping"
			es.bulk(index=INDEX_NAME, body=bulk_data, refresh=True)
		print chunk
		search_data.append(bulk_data[0])


threads = []

for i in xrange(0, 4):
    t = Thread(target=run, args=(i * 2500000,))
    threads.append(t)
    t.start()


for i in xrange(0, 4):
    threads[i].join()


with open("search_data", "w") as f:
    for item in search_data:
        f.write('%s\n' % item)



# search_args = {
# 	'index': 'test',
# 	'doc_type': 'document',
# 	'body': {
# 		"query": {
# 			"match": {
# 				'age': doc['age']
# 			}
# 		}
# 	},
# }

# print "searching", doc['age']
# print es.search(index='test', body={"query": {"match_all": {}}})
# print es.search(index='test', body={"query": {"match": {'age': doc['age']}}})

