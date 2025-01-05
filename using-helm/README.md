# Bitnami Library for K8s
Popular applications, provided by Bitnami, ready to launch on Kubernetes using Kubernetes Helm.
 $ helm repo add bitnami https://charts.bitnami.com/bitnami
 $ helm search repo bitnami
 $ helm install my-release bitnami/<chart>

For more information, please refer to the Bitnami charts project on GitHub.
https://github.com/bitnami/charts 

# Deploy Steps
## Install Helm
1. Install Helm cli tool
   $ curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash

2. Fix permissions of your ~/.kube/config file incase it is readable by whole group. 
   Chmod 600 should do.

## Deploying an application e.g mysql ( Happens in the worker node , the-eagle)

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
     