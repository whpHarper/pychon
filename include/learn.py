from elasticsearch5 import Elasticsearch

es = Elasticsearch([{"host": "59.110.18.77", "port": 9200}])
res = es.search(index="sadb-2018.11.12", doc_type="hiversl")
print(res['hits']['hits'])
for hit in res['hits']['hits']:
    print(hit["_source"]["reqid"],hit["_source"]["ts"])
