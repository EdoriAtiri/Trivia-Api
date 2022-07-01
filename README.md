# TRIVIA API

## Project Description

This documentation describes the resources that make up the Trivia API.The trivia api is an open source Rest api that allows developers to connect create quizzes and online trivia's through it. This repository also comes with a frontend application that allows developers to demo its abilities. Through this api you can:

- Retrieve all questions categories or;
- Filter questions based on their category
- Add new questions, their answers and specify their category and level of difficulty
- Delete questions
- Search for questions via a substring of that question
- Play the quiz game

## Getting Started

### Installation

#### Requirements

Understanding of Python, Flask and PostgreSQL is necessary to effectively run this program. This project requires the following programs and packages:

- [Python 3.x](https://www.python.org/downloads/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/installation/)
- [PostgreSQL](https://www.postgresql.org/download/)
- [NPM](https://www.npmjs.com/package/npm)

It is advised that you run this project in a virtual environment. Follow the instructions in the [python documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/) to set up your virtual environment.

#### Installing Dependencies

- Backend Dependency installation
  Follow the instructions below to install the project dependencies with Python's [preferred installer program](https://pypi.org/project/pip/).

1. Change the working directory in your terminal to the backend directory > cd backend/
2. Enter the following command > pip install -r requirements.txt

- Frontend Dependency installation

1. Change the working directory in your terminal to the frontend directory > cd frontend/
2. Enter the following command > npm install

#### Setup the Database

In your backend directory, run the following command to populate your database:

> psql trivia < trivia.psql

#### Running the Server

Still in the backend directory, run the following command in your terminal:

```
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

#### Running the Frontend

The frontend was built using ReactJS. To run it, check into the frontend directory and enter

> npm start

## API Reference

### Base URL

At present this app can only be run locally. The backend is hosted at the default, `http://127.0.0.1:5000/` which is set as a proxy on the frontend configuration. The default URL for the frontend is, `http://127.0.0.1:3000/`

### Authentication

The version of this application does has no authentication mechanism, method or requirements.

### Error Handling

If this application runs into an error on either the client or from the server, the erro will be returned in a json object. For example:

```
{
  "error": 404,
  "message": "Resource Not Found",
  "success": false
}
```

The Api will return three error types when requests fail:

- 404: Resource not found
- 405: Method not allowed
- 422: Unprocessable entry

### Endpoint library

> **GET /categories**

- Fetches a dictionary or object of key value pairs, with the id being the key and the value the corresponding category
- Request arguments: None

```
{
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
```
