
import sys
import argparse
import rethinkdb as r
import configparser
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Choose a config file')
parser.add_argument('--test', help='Test and exit', action="store_true")
args = parser.parse_args()

if args.config:
    config = configparser.ConfigParser()

    config.read(args.config)

    keep_id = bool(config['global']['keep-id'])
    rdbhost = config['rethinkdb']['host']
    rdbport = config['rethinkdb']['port']
    database = config['rethinkdb']['database']
    tables = (config['rethinkdb']['tables']).split(',')
    hosts = (config['elasticsearch']['hosts']).split(',')
    doctype = config['elasticsearch']['doctype']

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
            
            if keep_id:
                options['id'] = doc['id']

            res = es.index(index=table, doc_type=doctype, body=doc, **options)
            print("INSERT: ", doc)

if args.test:
    sys.exit(0)