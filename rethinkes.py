
import json
import rethinkdb as r
from elasticsearch import Elasticsearch

rdbhost = "localhost"
rdbport = 28015
database = "backend"
tables = ["posts"]
hosts = ["localhost"]
doctype = "post"

r.connect(rdbhost, rdbport).repl()

es = Elasticsearch(hosts,
          sniff_on_start=True,
          sniff_on_connection_fail=True,
          sniffer_timeout=60,
          http_auth=('elastic', 'changeme'))

for table in tables:
    cursor = r.db(database).table(table).run()

    for doc in cursor:
        print("INSERT: ", doc)
        res = es.index(index=table, doc_type=doctype, id=doc['id'], body=doc)
        