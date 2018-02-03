# Demo eines MongoDB Clusters

Init und Starten eines MongoDB Cluster: 

    > mlaunch init \
              --replicaset \
              --nodes 3 \
              --sharded tic tac toe \
              --config 3 \
              --mongos 3 \
              --port 30000 


Auflisten der Cluster Komponenten: 

    > mlaunch list


Zugreifen auf den Cluster: Alle Kommunikation it dem Cluster erfolgt über die 
Mongo Router (mongos). Dieser ist auf dem Port 30000. Somit kann aus einer
Linux-Shell oder über ein MongoDB GUI "normal" zugegriffen werden. 

    > mongo --port 30000

Öffnet eine MongoDB Shell auf dem MongoDB Router mongos. Damit kann der Cluster 
angesprochen werden, als ob es eine einige MongoDB Instanz ist. Die Verteilung der
Daten auf die Shards und die Spiegelung der Daten auf die Replica-Sets managed
MongoDB von alleine.

Wenn nun ein (ein einziges) Document in der Datenbank myDatabase in der Collection
myCollection erstellt wird, so wid dieses Dokument auf einem der Shards angelegt und 
dort auch auf die Replica-Sets gespiegelt. Um das zu sehen, greifen wir direkt auf die
Shards zu (Wichtig: dies ist egentlich nicht üblich. Der Zugriff auf die Daten erfolgt 
i.d.R. immer über den Router und dieser managed alles). Die Port-Nummern der Shards 
entnehmen wir der Cluster-Config, die mit ... 

    > sh.status()

... in der MongoDB-Shell (oder auch in einem MongoDB GUI) abgerufen werden kann. 
Es müssen drei Shards (tic, tac, toe) sein. Nun kann man sich auf die drei Shards 
einloggen ...

    > mongo --port 30003 (resp. der Port-Nr aus sh.status)

... und mit ...

    > show dbs

... die Datenbanken anzeigen lassen. Nach dem login sehen wir im MongoDB-Shell-Prompt 
den Namen des jweilgen Shard und den Status des darauf enthaltenen Replica-Set (primary,
secondary). Nur auf einem der Shards ist die von uns angelegte Datenbank myDatabase auch
wirklich vorhanden. Den Inhalt der Datenbank können wir uns mit ...

    > use myDatebase
    > show collections
    > db.myCollection.find()

... anzeigen lassen. 

Nun können wir auch prüfen, ob das erstellte Dokument auch auf den Replica-Sets des 
entsprechenden Shards ist. Pro Shard gibt es zwei Replica-Sets, die jeweils in einer
eigenen MongoDB Instanz angelegt wurden. Die beiden Replica-Set Instanzen haben die 
jeweils folgenden Port-Nummern des Primary des Shards. Loggen wir also auf das erste
Replica-Set des Shards ein ...

    > mongo --port 30004 (resp. der Port-Nr +1 aus sh.status))

... und versuchen wir auf das Dokument zuzugreifen ...

    > use myDatabase
    > db.myCollection.find()

... was mit einer Fehlermeldung abgelehnt wird:

    > "errmsg" : "not master and slaveOk=false"

Das bedeutet, das wir nicht ohne weiteres Daten aus einem der Replica-Sets lesen
können. Wir müssen explizit angeben, dass wir wissen, dass wir auf ein Replica-Set
zugreifen und dass wir nichts ändern wollen:

    > db.setSlaveOk()
    > db.myCollection.find()

Damit wird nun das Dokument angezeigt. 

Auf einem Secondary Replica-Set können keine Dokumente eingefügt werden. Diese 
können nur auf dem Primary Replica-Set erstellt werden. 


Stoppen des Cluster: 

    > mlaunch stop


Starten des Cluster: 

    > mlaunch start 


Um den Cluster zu starten, am besten ein Verzeichnis erstellen dann in diesem 
einmal "Init und Starten" ausführen. Nachher nur noch mit "Stoppen" und "Starten" 
arbeiten. Soll alles weggeräumt werden, das komplette Verzeichnis löschen

    > rm -r data


link zu mtools: https://github.com/rueckstiess/mtools 

