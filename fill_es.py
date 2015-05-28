import elasticsearch

import generate_docs

CHUNK_SIZE = 2500
DOC_NUMBER = 1000

INDEX_NAME = 'test'
TYPE_NAME = 'document'

def run(start_index):
	es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])
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
		es.bulk(index=INDEX_NAME, body=bulk_data, refresh=True)


threads = []

for i in xrange(0, 4):
        t = Thread(target=run, args=(i * 2500000,))
        threads.append(t)
        t.start()


for i in xrange(0, 4):
        threads[i].join()



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

