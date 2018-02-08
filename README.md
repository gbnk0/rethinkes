# rethinkes
Sync a rethinkdb database with elasticsearch

![pipeline status](https://travis-ci.org/gbnk0/rethinkes.svg?branch=master)
![coverage](https://coveralls.io/repos/github/gbnk0/rethinkes/badge.svg?branch=master)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![python_version](https://img.shields.io/badge/python-3.5%2C3.6-blue.svg)

#### USAGE EXAMPLE WITH PROVIDED EXAMPLE CONFIG FILE

```bash
rethinkes.py --config config.conf
```

#### QUICK START WITH DOCKER (DEFAULT CONFIG)

```bash
docker run gbnk0/rethinkes
```

#### WITH CUSTOM CONFIG FILE

```bash
docker run -v /path/containing/config.conf:/etc/rethinkes/ gbnk0/rethinkes
```

#### CONFIG FILE PARAMETERS

##### GLOBAL

**keep-id** : Keeps the rethinkdb document id when inserting into elasticsearch (useful for in place updates)
**loop-time** *0*: Delay (in seconds) before re-syncing all the tables to elastic (0 = One shot)


##### RETHINKDB

**rdbhost** *localhost* : Choose the rethinkdb source server

**rdbport** *28015* : Choose the rethinkdb port

**tables** *posts,users* : Choose the tables you want to sync

**database** *testdb* :  Choose the source rethinkdb database


##### ELASTICSEARCH

**eshost** *localhost* : Choose the elasticsearch destination host

**doctype** *mydoc* : Set an elasticsearch document type

**create-index** *0* : Create index if not exists

**wait-for-index** *1* : Wait for index to be created , nothing will be replicated until you create the index
