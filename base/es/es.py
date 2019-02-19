import mysql.connector
from mysql.connector import errorcode
from elasticsearch5 import Elasticsearch

config={
    'user':'root',
    'password':'123456',
    'host':'60.205.94.252',
    'database':''
}
es=Elasticsearch([{"host":"59.110.18.77","port":9200}])
index="storm-audit-log-2019-01-22"
'''
res=es.search(
    index=index,
    body={
        "aggs":{
            "servertype_agg":{
                "terms":{
                    "field":"@serviceType"
                }
            }
        }
    }
)
'''
facet=es.search(
    index=index,
    body={
        'facets':{
            'stat':{
                'terms':{
                    'field':'serviceType',
                    'order':'count',
                    'size':50
                }
            }
        }
    }
)

print(facet)
