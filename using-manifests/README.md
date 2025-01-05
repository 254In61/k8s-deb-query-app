# introduction
=> Deploying a single-instance MySQL database that is hosted within a K8s cluster
=> For clustered stateful applications, you would need to create StatefulSet objects.

# Getting it done

=> All this is done using .yml files.
=> You define everything on .yml files then "$ kubectl apply -f <.yml file>"

## Step 1: Deploy storage

To get this going, you have to :
   - Define the PV and pvc in a manifest .yaml file

     $ kubectl apply -f mysql-storage.yaml
       persistentvolume/mysql-pv-volume created
       persistentvolumeclaim/mysql-pv-claim created

   - PV will be defined under Cluster
   - PV claim is found under Config & Storage

To confirm:
   $ kubectl get persistentvolume


## Step 2 : Deploy the secrets

DB needs credentials to access, right?
   - Define the secret to be deployed in a .yaml file.
   - Apply the changes.
     $ kubectl apply -f mysql-secret.yaml 
       secret/mysql-secret created

   - Secret is defined under Config and Storage

To confirm:
    $ kubectl get secrets
    

## Step 3 : Deploy the database and expose as a service

Deploy the DB and then expose it to the outside world as K8s service.
   - Define the deployment and service in a .yml file.
   - Apply the changes
  
     $ kubectl apply -f mysql-deployment.yaml
       deployment.apps/mysql created
       service/mysql created

To confirm:
   $ kubectl get deployment

   $ kubectl get svc   .. You get to see the IP and port

# Access MySQL DB instance & build tables

## Access the mydb instance to build the db tables
1. List pods

 $ kubectl get pod
   NAME                     READY   STATUS    RESTARTS      AGE
   mysql-85d5bb8d57-9ng7v   1/1     Running   0             47m
   nginx-7854ff8877-jdqjv   1/1     Running   1 (11h ago)   27h

2. Get a shell for the pod by executing the following command from the worker node(the-eagle)

 $ kubectl exec --stdin --tty <pod name> -- /bin/bash 

 $ kubectl exec --stdin --tty mysql-85d5bb8d57-9ng7v -- /bin/bash
   bash-4.4#

3. access the MySQL shell and type in the password created when building the secret using mysql-secret.yml.
  ** So, how does one store this password securely??**

bash-4.4# mysql -p
Enter password: 
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 9
Server version: 8.3.0 MySQL Community Server - GPL

Copyright (c) 2000, 2024, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> 
mysql> 

## Build user & the db tables

1. Build the DB from here (Ref : db-build.sh )

2. Build new username that can be used by the scripts (Ref : db-build.sh )

## Confirm all is created - Access DB instance remotely

1. Check IP
 $ kubectl get svc
NAME         TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
kubernetes   ClusterIP   10.152.183.1     <none>        443/TCP    17d
mysql-svc    ClusterIP   10.152.183.81    <none>        3306/TCP   75m
nginx        ClusterIP   10.152.183.108   <none>        80/TCP     17d

2. Access the instance from remotely. mysql has to installed on the end device.

 $ mysql -u dev -h 10.152.183.81 -P 3306 -p
Enter password:
Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 10
Server version: 9.1.0 MySQL Community Server - GPL

3. Run your commands from there!

mysql> use mydb;
mysql> select * from countries;

# Update Your MySQL Deployment

To update any part of the deployment, all you need to do is edit the relevant YAML file with the updates followed by applying the changes:

kubectl apply -f <.yaml file>

# Delete Your MySQL Instance

If you intend to remove the entire deployment, use kubectl to delete each of the Kubernetes objects related to it:

kubectl delete deployment,svc mysql
kubectl delete pvc mysql-pv-claim
kubectl delete pv mysql-pv-volume
kubectl delete secret mysql-secret

This series of commands delete the deployment, the service, PV, PVC, and the secret you created. The system confirms the successful deletion