Oveview
=======
=> Building a basic application that is hosted by the K8s cluster.

Design
======
1. MySQL server with the "countries" table as a DB.
2. A python script that runs and queries the SQL server..Python server script queries based on certains string recieved.

Getting it done
===============
1. Setup Kubernetes Cluster: First, you'll need to set up a Kubernetes cluster. You can use tools like Minikube for local development or cloud-based solutions like Google Kubernetes Engine (GKE), Amazon Elastic Kubernetes Service (EKS), or Azure Kubernetes Service (AKS).

2. Deploy MySQL Server: You can use a MySQL Docker image to deploy MySQL server in your Kubernetes cluster. Define a Kubernetes deployment and service for MySQL.

3. Create Database and Table: Once MySQL is up and running, connect to it and create a database and table to store your data.

4. Build Python Script: Write a Python script that listens for the certain string you mentioned. Use a MySQL client library to connect to the MySQL database and execute queries.

5. Containerize Python Script: Create a Dockerfile for your Python script, and build a Docker image for it.

6. Deploy Python Script as Pod: Define a Kubernetes deployment or a job for your Python script, and deploy it to your Kubernetes cluster.

7. Set Up Communication: Ensure that your Python script can communicate with the MySQL server. This might involve setting environment variables or configuring network policies in Kubernetes.

8. Test: Test your setup by sending the certain string to trigger the Python script, which should then query the MySQL database.

9. Monitor and Maintain: Set up monitoring for your Kubernetes cluster and the applications running on it. Regularly maintain and update your applications and infrastructure as needed.



TOMMOROW??
==========
=> The challenge is, how does it piece together?
=> There is a mysql created with the necessary data.
=> To query MySQL data running in a Kubernetes cluster using a Job, you can create a Python script that connects to the MySQL database and executes the desired queries. Then, you can containerize this script and run it as a Kubernetes Job. 
=> But how do I kickstart this Job for the queries to happen?
   - To kickstart a Kubernetes Job when a certain string is received, you can set up an event-driven architecture where an event, such as receiving a string, triggers the creation of a Kubernetes Job. One common way to achieve this is by using a message broker like Kafka, RabbitMQ, or AWS SQS.
=> This is when shit gets complex!!.. 