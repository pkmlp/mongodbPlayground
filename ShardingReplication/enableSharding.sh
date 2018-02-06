mongo --port 30000 --eval "use myDatabase"
mongo --port 30000 --eval "db.myCollection.ensureIndex({_id:"hashed"})"
mongo --port 30000 --eval "sh.enableSharding("myDatabase")"
mongo --port 30000 --eval "sh.shardCollection("myDatabase.myCollection", {"_id": "hashed"})"
