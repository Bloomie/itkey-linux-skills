import elasticsearch

import generate_docs

es = elasticsearch.Elasticsearch([{'host': 'localhost', 'port': 9200}])

# es_args = {
# 	'index': 'test',
#     'doc_type': 'document',
# }


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

NAME = ""
AGE = ""


print 'searching: name = %(name)s ,age = %(age)s' % {'name': NAME, 'age': AGE}
print es.search(index='test', body={"query": {"match_all": {}}})
print es.search(index='test', body={"query": {"match": {'age': AGE}}})

