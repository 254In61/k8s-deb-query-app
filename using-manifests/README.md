# introduction
=> Deploying a single-instance MySQL database that is hosted within a K8s cluster
=> For clustered stateful applications, you would need to create StatefulSet objects.

# Step 1: Deploy storage

To get this going, you have to :
   - Define the PV and pvc in a manifest .yaml file

     $ kubectl apply -f manifests/mysql-storage.yaml
       persistentvolume/mysql-pv-volume created
       persistentvolumeclaim/mysql-pv-claim created

   - PV will be defined under Cluster
   - PV claim is found under Config & Storage

To confirm:
   $ kubectl get pv

   $ kubectl get pv -n <namespace>


# Step 2 : Deploy the secrets

DB needs credentials to access, right?
   - Define the secret to be deployed in a .yaml file.
   - Apply the changes.
     $ kubectl apply -f manifests/mysql-secret.yaml 
       secret/mysql-secret created

   - Secret is defined under Config and Storage

To confirm:
    $ kubectl get secrets -n <namespace>

# Step 3 : Deploy the pods
Deploy the DB and then expose it to the outside world as K8s service.
   - Define the deployment and service in a .yml file.
   - Apply the changes
  
   $ kubectl apply -f manifests/mysql-deployment.yaml
      deployment.apps/mysql created

To confirm:
   $ kubectl get pods -n countries
   $ kubectl describe pods mysql-deployment-5c994b9fc-j8257 -n countries

# Step 4 : Expose the MySQL instance to be accessed from outside the pod.

  $ kubectl apply -f manifests/mysql-service.yaml

To confirm:

  $ kubectl get svc -n countries
NAME        TYPE        CLUSTER-IP      EXTERNAL-IP   PORT(S)    AGE
mysql-svc   ClusterIP   10.152.183.39   <none>        3306/TCP   47m



