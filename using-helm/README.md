# Bitnami Library for K8s
Popular applications, provided by Bitnami, ready to launch on Kubernetes using Kubernetes Helm.
 $ helm repo add bitnami https://charts.bitnami.com/bitnami
 $ helm search repo bitnami
 $ helm install my-release bitnami/<chart>

For more information, please refer to the Bitnami charts project on GitHub.
https://github.com/bitnami/charts 

# Install Helm
1. Install Helm cli tool
   $ curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

2. Fix permissions of your ~/.kube/config file incase it is readable by whole group. 
   Chmod 600 should do.

# Deploying mysql ( Happens in the worker node , the-eagle)

1. Add a maintained Helm repo & update the repos
   $ helm repo add bitnami https://charts.bitnami.com/bitnami
   $ helm repo update

2. To keep things organized, create a namespace for MySQL: (Optional)
   $ kubectl create namespace database

3. Deploy
    3.1) To deploy with default installation values 
       $ helm install my-mysql bitnami/mysql --namespace database --kube-insecure-skip-tls-verify 
       ** --kube-insecure-skip-tls-verify  : Certificates authority not deployed on my home lab

    3.2) Customized installation
       
       1. Extract the default values into a file you can edit.
          $ helm show values bitnami/mysql > mysql-values.yaml

       2. Edit the file to configure:
          2.1) Root Password:
 
            auth:
                rootPassword: your-root-password

          2.2) Database and User:
            
            auth:
                database: your-database-name
                username: your-username
                password: your-password
          
          2.3) Persistence (to use a PersistentVolumeClaim):

            primary:
                persistence:
                enabled: true
                storageClass: "microk8s-hostpath"
                size: 8Gi
        
       3. Deploy with the custom values:
          $ helm install mysql-with-helm bitnami/mysql --namespace database -f mysql-values.yaml
     
        
4. Confirmation:
   - Check if pod is up and running:

     $ kubectl get pods -n database
    NAME                READY   STATUS    RESTARTS   AGE
    mysql-with-helm-0   1/1     Running   0          117s
   
   - Get service details :

     $ kubectl get svc -n database
     NAME                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
     mysql-with-helm            ClusterIP   10.152.183.197   <none>        3306/TCP   4m40s
     mysql-with-helm-headless   ClusterIP   None             <none>        3306/TCP   4m40s

    - Verify Persistent Volume (if persistence is enabled):


# Access MySQL
- Steps are in CONSUMING-MYSQL
- NB: *** Had challenges with the credentials.. Maybe I need to get it right when deploying with Helm.
 



