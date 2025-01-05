# What is HELM?
- A Helm chart is a package of pre-configured Kubernetes resources that you can use to deploy, manage, and update applications in a Kubernetes cluster.
  These pre-configure K8s packages are called Charts.

- Helm is a tool for managing Kubernetes charts.

- Helm, often referred to as the "package manager for Kubernetes," simplifies the deployment of complex applications by providing reusable, versioned, and parameterized templates.

# Key components of a Helm Chart
1. Chart.yaml  : Contains metadata about the chart (name, version, description, etc.).
2. Values.yaml : A default configuration file where you define customizable parameters for the chart.
3. Templates/  : Contains Kubernetes resource templates (YAML files with placeholders for dynamic values).
4. Charts/     : A directory for dependencies (other charts needed for this chart to work).
5. README.md   : Documentation about what the chart does and how to use it.

# How Helm works during installation
When you run a helm install command, the YAML files defined in the Helm chart are not physically stored in your local filesystem. 
Instead, they are applied directly to your Kubernetes cluster. 

## Here's how it works:

1. Templates Are Rendered:

- The Helm chart templates (*.yaml files in the templates/ directory of the chart) are rendered with the values you provide in the values.yaml file or via command-line flags.
- The resulting Kubernetes manifests (YAML definitions) are sent to the Kubernetes API server.

2. Resources Are Applied:

- The Kubernetes API server processes the manifests and creates the specified resources (e.g., Pods, Services, Deployments, ConfigMaps, etc.) in the target namespace.

## Where are the YAMLS files stored?:
=> In Kubernetes: The YAML files are stored as resources in your Kubernetes cluster. 
   
   You can view or retrieve them using kubectl commands:
   1.1) List all resources in a namespace: $ kubectl get all -n <namespace>
       e.g :
       $ kubectl get all -n database
NAME             READY   STATUS    RESTARTS   AGE
pod/my-mysql-0   1/1     Running   0          37m

NAME                        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
service/my-mysql            ClusterIP   10.152.183.147   <none>        3306/TCP   37m
service/my-mysql-headless   ClusterIP   None             <none>        3306/TCP   37m

NAME                        READY   AGE
statefulset.apps/my-mysql   1/1     37m

   1.2) View the YAML of a specific resource: $ kubectl get <resource-type> <resource-name> -n <namespace> -o yaml
      $ kubectl get pod my-mysql-0 -n database -o yaml

=> Helm releases (Metadata): 
    - Helm stores metadata about the release in a ConfigMap or Secret in the cluster. 
    - These are stored in the same namespace as the release under the kube-system namespace by default (or the namespace you install the chart into).
    
    $ helm list -n <namespace>

Example :
   $ helm list -n database
NAME            NAMESPACE       REVISION        UPDATED                                         STATUS          CHART           APP VERSION
my-mysql        database        1               2025-01-04 20:05:31.786917222 +1000 AEST        deployed        mysql-12.2.0    8.4.3

## If You Want the Rendered YAML Files Locally
You can generate the rendered Kubernetes YAML files without applying them to the cluster using the helm template command:

 $ helm template <release-name> <chart-name> --namespace <namespace> > output.yaml

This will render the templates using the provided values and save the resulting manifests to output.yaml.

