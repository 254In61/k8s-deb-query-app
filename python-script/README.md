Overview
========
To query MySQL data running in a Kubernetes cluster using a Job, you can create a Python script that connects to the MySQL database and executes the desired queries. Then, you can containerize this script and run it as a Kubernetes Job. Here's how you can do it:

1. Write Python Script: Write a Python script that connects to the MySQL database and executes the query. You can use a MySQL client library like mysql-connector-python to interact with the database. Check db-query.py.

2. Containerize Python Script: Create a Dockerfile to containerize the Python script. Check Dockerfile.

3. Build Docker Image: Build the Docker image using the Dockerfile

4. Run Job in Kubernetes: Define a Kubernetes Job YAML file to run the Python script as a Job. Check python-job.yaml

5. Apply Job Configuration: Apply the Job configuration to your Kubernetes cluster.
   $kubectl apply -f python-job.yaml
   
   - This Job will run the Python script as a container in the Kubernetes cluster, connect to the MySQL database, execute the query, and print the results.




MySQL
=====
- The SQL server details are added in AppModule/socketParams.py

- Sample MySQL Table used:

mysql> select * from Countries;
+-------------+-------------+------------+-----------------+-------------------+

| CountryName | CountryCode | Capitol    | Leader          | PopulationMillion |

+-------------+-------------+------------+-----------------+-------------------+

| Kenya       |         254 | Nairobi    | William Ruto    |              50.2 |

| Tanzania    |         255 | Dodoma     | Samia Suluhu    |              60.2 |

| Australia   |          61 | Canberra   | Antony Albanese |              28.5 |

| USA         |           1 | Washington | Joe Biden       |             320.4 |

+-------------+-------------+------------+-----------------+-------------------+

4 rows in set (0.00 sec)

- Ensure your Application Server has python mysql-connector installed.

  $ pip install mysql-connector-python



Author
======
254in61