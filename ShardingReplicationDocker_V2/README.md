# mongodb-sharding-docker-compose

Quelle: https://github.com/jfollenfant/mongodb-sharding-docker-compose 



## work in progress - authentication does not work (permission denied for keyfile)




:whale: docker-compose stack that allows you to turn on a full MongoDB sharded cluster with the following components :

 * configserver replicaset: 3x mongod with configsrv enabled 
 * first replicaset shard: 3x mongod 
 * second replicaset shard: 3x mongod
 * third replicaset shard: 3x mongod
 * mongo query router: 1x mongos
 * authentication enabled + global auth key certificate between nodes

:warning: Of course this is for development purpose only  

    > ./up.sh
    
    
You can also edit mongo-auth.init.js to change admin credentials before turning up the cluster

    admin = db.getSiblingDB("admin")
    admin.createUser(
      {
         user: "admin",
         pwd: "admin",
         roles: [ { role: "userAdminAnyDatabase", db: "admin" } ] 
      }
    )


:beer: log in to the cluster:

    > docker exec -it mongodbdocker_mongo-router-01_1 mongo admin  -u'admin' -p'admin'


:beer: enable sharding and check status

    > use myDatabase
    > db.myCollection.ensureIndex({_id:"hashed"})
    > sh.enableSharding("myDatabase")
    > sh.shardCollection("myDatabase.myCollection", {"_id": "hashed"})
    > sh.status()    


:tropical_drink: work with the cluster

    > use myDatabase
    > db.myCollection.insert({"AnzDok":"1", "Timestamp":"gerade eben", "Remark":"manuell eingefügt"})
    > db.myCollection.find()
    > db.myCollection.find().count()

    > db.myCollection.insert({"AnzDok":"2", "Timestamp":"gerade eben", "Remark":"manuell eingefügt"})
    > ... and so on ...
    > db.myCollection.insert({"AnzDok":"13", "Timestamp":"gerade eben", "Remark":"manuell eingefügt"})
    > db.myCollection.find()
    > db.myCollection.find().count()
    

:beer: And turn it down with:

    > ./down.sh

