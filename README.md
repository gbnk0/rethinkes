# rethinkes
Python program to sync rethinkdb database with elasticsearch


#### USAGE EXAMPLE WITH PROVIDED EXAMPLE CONFIG FILE

```bash
rethinkes.py --config config.conf
```

#### CONFIG FILE PARAMETERS

##### GLOBAL

**keep-id** : Keeps the rethinkdb document id when inserting into elasticsearch (useful for in place updates)


##### RETHINKDB

**rdbhost** *localhost* : Choose the rethinkdb source server

**rdbport** *28015* : Choose the rethinkdb source server

**tables** *posts,users* : Choose the tables you want to sync

**database** *testdb* :  Choose the source rethinkdb database


##### ELASTICSEARCH

**eshost** *localhost* : Choose the elasticsearch destination host

**doctype** *mydoc* : Set an elasticsearch document type
