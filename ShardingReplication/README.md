# Demo eines MongoDB Clusters

Init und Starten eines MongoDB Cluster: 

    > mlaunch --replicaset  \
              --sharded tic tac toe \ 
              --config 3 \
              --mongos 3 \
              --port 30000 


Auflisten der Cluster Komponenten: 

    > mlaunch list


Stoppen des Cluster: 

    > mlaunch stop


Starten des Cluster: 

    > mlaunch start 


Um den Cluster zu starten, am besten ein Verzeichnis erstellen dann in diesem 
einmal "Init und Starten" ausführen. Nachher nur noch mit "Stoppen" und "Starten" 
arbeiten. Soll alles weggeräumt werden, das komplette Verzeichnis löschen

