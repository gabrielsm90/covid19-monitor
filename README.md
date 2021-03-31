# Covid 19 Monitor

Personal project made just to have some Python programming fun and get to 
practice a bit with tools such as Kafka, Docker and code linters.

## Project

This application is composed of a set of decoupled microservices which
keep monitoring results from https://api.covid19api.com/summary.

### Services

#### Scheduler

Scheduler running at every X minutes and scheduling new Jobs.

#### API Client

Service that, at each new Job, fetches the API and get latest data.

#### Server

Flask application exposing data through a REST API.

#### Register

When the client publishes new results to the broker, this service
uses the Flask app to update the database.

#### Logger

Keeps listening to a Log topic on the broker and registering the
messages in a text file.

### Technology Stack

Programming language: Python
Database: Mongodb
Message Broker: Apache Kafka
