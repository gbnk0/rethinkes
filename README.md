# rethinkes
Python program to sync rethinkdb database with elasticsearch


#### USAGE EXAMPLE 

```bash
rethinkes.py --keep-id --eshost localhost --rdbhost localhost --tables posts --database backend
```

#### PARAMETERS

--keep-id : Keeps the rethinkdb document id when inserting into elasticsearch (useful for in place updates)

--eshost *localhost* : Choose the elasticsearch destination host

--rdbhost *localhost* : Choose the rethinkdb source server

--tables *posts,users* : Choose the tables you want to sync

--database *testdb* :  Choose the source rethinkdb database

--doctype *mydoc* : Set an elasticsearch document type
