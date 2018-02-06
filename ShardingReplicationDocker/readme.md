# Mongo Sharded Cluster with Docker Compose

A simple sharded Mongo Cluster with a replication factor of 3 running in `docker` using `docker-compose`.

Designed to be quick and simple to get a local or test environment up and running. 
Needless to say... DON'T USE THIS IN PRODUCTION!

Heavily inspired by [https://github.com/jfollenfant/mongodb-sharding-docker-compose](https://github.com/jfollenfant/mongodb-sharding-docker-compose)


## Mongo Components

* Config Server (3 member replica set): `config01`,`config02`,`config03`
* 3 Shards (each a 3 member replica set):
	* `shard01a`,`shard01b`,`shard01c`
	* `shard02a`,`shard02b`,`shard02c`
	* `shard03a`,`shard03b`,`shard03c`
* 1 Router (mongos): `router`

(TODO): DB data persistence using docker data volumes
(TODO): DB Authentication



## First Run (initial setup)

**Make sure there is no other MongoDB Instanc running**

	> sudo service mongod stop

**Start all of the containers** (daemonized)

	> docker-compose up -d

**Initialize the replica sets (config server and shards) and router**

	> sh init.sh

This script has a `sleep 20` to wait for the config server and shards to elect their primaries before initializing the router


**Verify the status of the sharded cluster**

	> docker-compose exec router mongo
	mongos> sh.status()

``` 
--- Sharding Status --- 
  sharding version: {
        "_id" : 1,
        "minCompatibleVersion" : 5,
        "currentVersion" : 6,
        "clusterId" : ObjectId("5a795a6b5179f663653ba8b3")
  }
  shards:
        {  "_id" : "shard01",  "host" : "shard01/shard01a:27018,shard01b:27018,shard01c:27018",  "state" : 1 }
        {  "_id" : "shard02",  "host" : "shard02/shard02a:27019,shard02b:27019,shard02c:27019",  "state" : 1 }
        {  "_id" : "shard03",  "host" : "shard03/shard03a:27020,shard03b:27020,shard03c:27020",  "state" : 1 }
  active mongoses:
        "3.6.2" : 1
  autosplit:
        Currently enabled: yes
  balancer:
        Currently enabled:  yes
        Currently running:  no
        Failed balancer rounds in last 5 attempts:  0
        Migration Results for the last 24 hours:
                No recent migrations
  databases:
        {  "_id" : "config",  "primary" : "config",  "partitioned" : true }
```


## Normal Startup

The cluster only has to be initialized on the first run. Subsequent startup can be achieved 
simply with `docker-compose up` or `docker-compose up -d`



## Accessing the Mongo Shell

Its as simple as:

	> docker-compose exec router mongo



## Resetting the Cluster

To remove all data and re-initialize the cluster, make sure the containers are stopped and then:

	> docker-compose stop
	> docker-compose rm

Execute the **First Run (initial setup)**  instructions again.


# Analyzing the Cluster

**Config:**

The containers are configured as follows:
* router    IP 192.168.0.77   PORT 27017
* config1   IP 192.168.0.11   PORT 27017 
* config2   IP 192.168.0.12   PORT 27017 
* config3   IP 192.168.0.13   PORT 27017 
* shard1    IP 192.168.0.111 / .112 / .113   PORT 27018
* shard2    IP 192.168.0.121 / .122 / .123   PORT 27019
* shard3    IP 192.168.0.131 / .132 / .133   PORT 27020

To access replica-sets in shard1:
* mongo --host 192.168.0.111 --port 27108
* mongo --host 192.168.0.112 --port 27108
* mongo --host 192.168.0.113 --port 27108
One of them will be primary, the others are secondary


## Test Scenario

Step 1. Connect to MongoDB-Router

      > docker-compose exec router mongo

Step 2. Create a Database and a Collection with only one Dokument:

      > use myDatabase
      > db.myCollection.insert({firstename:"Peter", lastname:"Kessler"})
      > db.myCollection.find()

Step 3. Check on which shard the Database was created (use the primary of each replica set)

      > mongo --host 192.168.0.111 --port 27108 (assuming shard01a is primary)
      > show dbs
      > mongo --host 192.168.0.121 --port 27108 (assuming shared02a is primary)
      > show dbs
      > mongo --host 192.168.0.131 --port 27108 (assuming shared03a is primary)
      > show dbs
      
You should see the database only on one of the shards:

Step 4. Check whether the database.collection.document is on all replica-sets in the shards

      > mongo --host 192.168.0.121 --port 27108 (assuming the database.collection.document is on shared2)
      > use myDatabase
      > db.myCollection.find()
      > quit()
      > mongo --host 192.168.0.122 --port 27108 
      > use myDatabase
      > db.myCollection.find()
      > quit()
      > mongo --host 192.168.0.123 --port 27108 
      > use myDatabase
      > db.myCollection.find()
      > quit()
      
Step 5. Create more documents and check whether they are really sharded and replicated

      > ...


