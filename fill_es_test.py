import elasticsearch

import generate_docs

es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])

#es.indices.delete(index='test-index')

CHUNK_SIZE = 13


INDEX_NAME = 'test'
TYPE_NAME = 'document'


bulk_data = []
for i in xrange(0, DOC_NUMBER):
	op_dict = {
        "index": {
        	"_index": INDEX_NAME, 
        	"_type": TYPE_NAME, 
        	"_id": i
        }
    }
	doc = generate_docs.generate_doc()
	bulk_data.append(op_dict)
	bulk_data.append(doc)
	# print doc
	# res = es.index(id=i, body=doc, **es_args)
	# print res

#print docs
print es.bulk(index=INDEX_NAME, body=bulk_data, refresh=True)


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

