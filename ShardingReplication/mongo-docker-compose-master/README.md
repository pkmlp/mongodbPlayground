# mongo-docker-compose
This repository provides a fully sharded mongo environment using docker-compose and local storage.

The MongoDB environment consists of the following docker containers

 - **mongosrs(1-3)n(1-3)**: Mongod data server with three replica sets containing 3 nodes each (9 containers)
 - **mongocfg(1-3)**: Stores metadata for sharded data distribution (3 containers)
 - **mongos(1-2)**: Mongo routing service to connect to the cluster through (1 container)



## Caveats

 - This is designed in no way for production but as a cheap learning and exploration vehicle.



## Setup Cluster
This will pull all the images from Docker and run all the containers.

    docker-compose up -d



You will need to run the following *once* only to initialize all replica sets and shard data across them

    ./initiate



You should now be able connect to mongos1 and the new sharded cluster from the mongos container itself using the mongo shell to connect to the running mongos process

    docker exec -it mongos1 mongo



## Stop Cluster
This will stop all comtainers.

    docker-compose down



## Persistent storage
Data is stored at ./data/ and is excluded from version control. Data will be persistent between container runs. To remove all data 

./reset

 
