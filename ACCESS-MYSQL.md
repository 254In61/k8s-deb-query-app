# Overview
- This is after the POD has been deployed and services are up and running.

# Within the Cluster
You use a temporary Kubernetes pod to connect to the MySQL service.
*** Comes in handy when running a Python3 POD that querries DB and returns to the clients.. Right?* 

1. Start a mysql client pod (A pod that has mysql client already installed):
   ** This is a temporary pod that dies and is deleted once not in use ***
   $ kubectl run mysql-client --rm -it --image=bitnami/mysql --namespace database --command -- bash

2. Once inside the pod, access the mysql-with-helm pod.
   $ mysql -h mysql-with-helm-0 -u root -p

## Outside the Cluster
- If accessing from within the NODE .

  $ kubectl get pod -n database
NAME                READY   STATUS    RESTARTS   AGE
mysql-with-helm-0   1/1     Running   0          49m

  $ kubectl exec --stdin --tty mysql-with-helm-0 -n database -- /bin/bash

You will need to expose MySQL to the outside world as a service.

In my case, I am using NodePort since it is a home-lab with no loadbalance.


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