*
* Demo eines MongoDB Clusters auf localhost mit Authentifizierung
*
* Beachte dazu unbedingt: https://docs.mongodb.com/manual/core/security-users/#sharding-security 
*   --> direkter Zugriff auf die einzelnen Shards ist nicht ohne zusätzliche Aktionen möglich
*       für Demo-Zwecke bei denen auf einzelne Shards und Replica-Sets zugegriffen werden soll,
*       enpfehle ich den Cluster ohne Authentifizierung aufzusetzen. Für den eigentlichen Einsatz
*       eines Clusters diesen mit Authentication aufsetzen und folgendes beachten:
*
*       --> Important:  Always connect and authenticate to sharded clusters via a mongos instance.
*
*


Init und Starten eines MongoDB Clusters mit Authentifizierung: 

    > mlaunch init \
              --auth \
              --username mongoAdmin \
              --password pkmlp \
              --replicaset \
              --nodes 3 \
              --sharded tic tac toe \
              --config 3 \
              --mongos 3 \
              --port 30000


Auflisten der Cluster Komponenten: 

    > mlaunch list


Nun müssen wir im Mongo Router noch das Sharding einrichten. Dazu Verbindeun wir uns mit 
dem Mongo Router. Alle Kommunikation mit dem Cluster erfolgt über die Mongo Router (mongos). 
Dieser ist auf dem Port 30000. 

    > mongo --port 30000 -u mongoAdmin -p pkmlp --authenticationDatabase admin
    > use myDatabase
    > db.myCollection.ensureIndex({_id:"hashed"})
    > sh.enableSharding("myDatabase")
    > sh.shardCollection("myDatabase.myCollection", {"_id": "hashed"})

Die Verteilung der Daten auf die Shards und die Spiegelung der Daten auf die Replica-Sets 
managed MongoDB nun von alleine.


Damit kann der Cluster angesprochen werden, als ob es eine einzige MongoDB Instanz ist. 
Die Verteilung der Daten auf die Shards und die Spiegelung der Daten auf die Replica-Sets 
sowie die User-Authentication managed MongoDB von alleine.


Mit ...

    > show dbs
    > use myDatebase
    > show collections
    > db.myCollection.insert({firstname:"Peter", lastname:"Kessler"})
    > db.myCollection.find()

... die Datenbank myDatabase anlegen (resp. auswählen wenn bereits vorhanden) und darin 
    ein Dokument in der Collection myCollection anlegen und anzeigen lassen. 


Mit Authentifizierung ist der Zugriff auf die einzelnen Shards nicht ohne weiteres möglich.
Dazu müssten auf jedem der Shards entsprechende User eingerichtet werden. In produktiven 
Umgebungen empfiehlt sich dies, um damit die Möglichkeit zu haben, auf einem Shard selber
Wartungs- / Korrekturarbeiten vornehmen zu können.

In dieser Demo verzichte ich darauf. Dass das Sharding und die Replikation mit dieser 
Konfiguration funktioniert, ist im ersten Beislpiel (ohne Authentifizierung) bewiesen.


Stoppen des Cluster: 

    > mlaunch stop


Starten des Cluster: 

    > mlaunch start 


Um den Cluster zu starten, am besten ein Verzeichnis erstellen dann in diesem 
einmal "Init und Starten" ausführen. Nachher nur noch mit "Stoppen" und "Starten" 
arbeiten. Soll alles weggeräumt werden, das komplette Verzeichnis löschen

    > rm -r data


link zu mtools: https://github.com/rueckstiess/mtools 

