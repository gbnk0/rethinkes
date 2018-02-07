
import sys
import argparse
import rethinkdb as r
import configparser
from time import sleep
from retrying import retry
from elasticsearch import Elasticsearch

parser = argparse.ArgumentParser()
parser.add_argument('--config', help='Choose a config file')
parser.add_argument('--test', help='Test and exit', action="store_true")
args = parser.parse_args()

@retry(wait_fixed=5000)
def make_elastic_client(hosts):
    try:
        es = Elasticsearch(hosts,
                            sniff_on_start=True,
                            sniff_on_connection_fail=True,
                            retry_on_timeout=True,
                            sniffer_timeout=60,
                            http_auth=('elastic', 'changeme'))
        return es
    except:
        print('Error while connecting to elasticsearch')


def start_sync(keep_id, rdbhost, rdbport, database, tables, hosts, doctype):
    
    # Connect first to elasticsearch
    es = make_elastic_client(hosts)
    
    # Connect to rethinkdb
    r.connect(rdbhost, rdbport).repl()

    for table in tables:
        cursor = r.db(database).table(table).run()

        for doc in cursor:
            options = {}

            if keep_id == True:
                options['id'] = doc['id']

            res = es.index(index=table, doc_type=doctype,
                            body=doc, **options)
            print("INSERT: ", doc)

if args.config:
    config = configparser.ConfigParser()

    config.read(args.config)

    keep_id = bool(config['global']['keep-id'])
    looptime = int(config['global']['loop-time'])
    rdbhost = config['rethinkdb']['host']
    rdbport = config['rethinkdb']['port']
    database = config['rethinkdb']['database']
    tables = (config['rethinkdb']['tables']).split(',')
    hosts = (config['elasticsearch']['hosts']).split(',')
    doctype = config['elasticsearch']['doctype']

    sync_args = (keep_id, rdbhost, rdbport, database, tables, hosts, doctype)

    if looptime > 0:
        while True:
            start_sync(*sync_args)
            sleep(looptime)
    
    start_sync(*sync_args)

if args.test:
    sys.exit(0)
