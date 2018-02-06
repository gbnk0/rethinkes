
import json
import argparse
import rethinkdb as r
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser()
parser.add_argument('--keep-id', help='Keeps the rethinkdb document ID in elasticsearch', action='store_true')
parser.add_argument('--rdbhost', help='Set the rethinkdb source host', default='localhost')
parser.add_argument('--eshost', help='Set the elasticsearch dest hosts (comma separated if multiple)', default='localhost')
parser.add_argument('--doctype', help='Set the doctype in ES (comma separated if multiple)', default='doc')
parser.add_argument('--tables', help='Choose the tables to replicate (comma separated if multiple)', default='test')
parser.add_argument('--database', help='Set the database name', default='test')
args = parser.parse_args()

rdbhost = args.rdbhost
rdbport = 28015
database = args.database
tables = (args.tables).split(',')
hosts = (args.eshost).split(',')
doctype = args.doctype

r.connect(rdbhost, rdbport).repl()

es = Elasticsearch(hosts,
          sniff_on_start=True,
          sniff_on_connection_fail=True,
          sniffer_timeout=60,
          http_auth=('elastic', 'changeme'))

for table in tables:
    cursor = r.db(database).table(table).run()

    for doc in cursor:
        options = {}
        
        if args.keep_id:
            options['id'] = doc['id']

        res = es.index(index=table, doc_type=doctype, body=doc, **options)
        print("INSERT: ", doc)
