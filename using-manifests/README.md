# introduction
=> Deploying a single-instance MySQL database that is hosted within a K8s cluster
=> For clustered stateful applications, you would need to create StatefulSet objects.

# Step 1: Deploy storage

To get this going, you have to :
   - Define the PV and pvc in a manifest .yaml file

     $ kubectl apply -f mysql-storage.yaml
       persistentvolume/mysql-pv-volume created
       persistentvolumeclaim/mysql-pv-claim created

   - PV will be defined under Cluster
   - PV claim is found under Config & Storage

To confirm:
   $ kubectl get persistentvolume


# Step 2 : Deploy the secrets

DB needs credentials to access, right?
   - Define the secret to be deployed in a .yaml file.
   - Apply the changes.
     $ kubectl apply -f mysql-secret.yaml 
       secret/mysql-secret created

   - Secret is defined under Config and Storage

To confirm:
    $ kubectl get secrets

# Step 3 : Deploy the pods
Deploy the DB and then expose it to the outside world as K8s service.
   - Define the deployment and service in a .yml file.
   - Apply the changes
  
     $ kubectl apply -f mysql-deployment.yaml
       deployment.apps/mysql created

     $ kubectl apply -f mysql-deployment.yaml
       service/mysql created

To confirm:
   $ kubectl get deployment

   $ kubectl get svc   .. You get to see the IP and port
    

