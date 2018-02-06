# rethinkes
Python program to sync rethinkdb database with elasticsearch

![pipeline status](https://travis-ci.org/gbnk0/rethinkes.svg?branch=master)
![coverage](https://coveralls.io/repos/github/gbnk0/rethinkes/badge.svg?branch=master)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![python_version](https://img.shields.io/badge/python-3.5%2C3.6-blue.svg)

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
