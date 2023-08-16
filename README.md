# RabbitMQ-Controller
This script is used to get the list of queues with zero consumers in RabbitMQ.

The script first imports the following modules:

* json: This module is used to parse the JSON response from the RabbitMQ API.
* requests: This module is used to make HTTP requests to the RabbitMQ API.
* re: This module is used to match the queue name with the regular expression.

The script then defines the `get_queues()` function. This function takes the following parameters:

* host: The hostname of the RabbitMQ server.
* username: The username for the RabbitMQ user.
* password: The password for the RabbitMQ user.
* regex: The regular expression to match the queue name.

The function first creates a URL for the RabbitMQ API. This URL is in the format `http://<host>:15672/api/queues/`.

The function then makes a GET request to the API. The request is authenticated with the username and password.

The function then parses the JSON response from the API. The response contains a list of queues. The function returns a list of the names of the queues that have zero consumers and match the regular expression.

The script then sets the following variables:

* host: The hostname of the RabbitMQ server.
* username: The username for the RabbitMQ user.
* password: The password for the RabbitMQ user.
* regex: The regular expression to match the queue name.

The script then calls the `get_queues()` function. The function returns a list of queues with zero consumers. The script prints the names of the queues.

Here is an example of how to use the script:

```
python rabbitmq_zero_consumer.py
```

This will print the names of all the queues with zero consumers in RabbitMQ.
