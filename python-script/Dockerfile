# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory in the container
WORKDIR /usr/src/app

# Copy the Python script into the container
RUN git clone -b develop 

# Install MySQL client library
RUN pip install mysql-connector-python

# Run the Python script when the container launches
CMD ["python", "./your_script.py"]
