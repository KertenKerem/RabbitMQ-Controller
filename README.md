This file contains a Python script that lists all the queues on a RabbitMQ server that have no consumers. 
The script uses the RabbitMQ API to get a list of all the queues, and then filters the list to only include queues that have no consumers and that match a given regular expression.

The script takes four arguments:

* `host`: The hostname of the RabbitMQ server.
* `username`: The username to use to authenticate to the RabbitMQ server.
* `password`: The password to use to authenticate to the RabbitMQ server.
* `regex`: A regular expression that is used to filter the list of queues.

The script prints the names of all the queues that match the regular expression and have no consumers.

This will print the names of all the queues on the RabbitMQ server at `<Your_Server_IP>` that have no consumers and that match the regular expression like `^(?!_)([a-zA-Z0-9]+)$`.

The script uses the following Python libraries:

* `json`: This library is used to parse the JSON response from the RabbitMQ API.
* `requests`: This library is used to make HTTP requests to the RabbitMQ API.
* `re`: This library is used to match regular expressions.
  
For example:

* `python3` rabbitmq_zero_consumer.py my-rabbit-server my-username my-password
