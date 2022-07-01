# TRIVIA API

## Project Description

This documentation describes the resources that make up the Trivia API.The trivia api is an open source Rest api that allows developers to display and create quizzes and online trivia's through it. This repository also comes with a frontend application that allows developers to demo its abilities. Through this api you can:

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
  Follow the instructions below to install the project dependencies with Python's [preferred installer program (PIP)](https://pypi.org/project/pip/).

  1. Change the working directory in your terminal to the backend directory
     > cd backend/
  2. Enter the following command
     > pip install -r requirements.txt

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

> **GET /questions**

- Fetches a nested dictionary with a categories dictionary, a questions array that includes an array of questions, their answers, difficulty, id and category, the current category, the total number of questions and a success message.
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
  "current_category": null,
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    }
  ],
  "success": true,
  "total_questions": 19
}
```

> **DELETE /questions/<int:id>**

- Deletes the question with the given id in the URL parameter
- Request arguments: None
- sample url: http://127.0.0.1:5000/questions/3

```
"success": true,
"deleted": 3
```

> **POST /questions**

- Adds a new question to the database and returns a dictionary with a success message and a dictionary with all the new questions including the newly added one.
- Request arguments: This endpoint requires a value for the following keys: question, answer, difficulty, category e.g

```
{
"question": "What football is the real football?",
"answer": "British Football",
"difficulty": 4,
"category": 6
}
```

It will return a dictionary like this:

```
{
  "questions": [
    {
      "answer": "Apollo 13",
      "category": 5,
      "difficulty": 4,
      "id": 2,
      "question": "What movie earned Tom Hanks his third straight Oscar nomination, in 1996?"
    },
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
     {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    },
    {
      "answer": "Escher",
      "category": 2,
      "difficulty": 1,
      "id": 16,
      "question": "Which Dutch graphic artist–initials M C was a creator of optical illusions?"
    },
    {
      "answer": "Mona Lisa",
      "category": 2,
      "difficulty": 3,
      "id": 17,
      "question": "La Giaconda is better known as what?"
    },
    {
      "answer": "One",
      "category": 2,
      "difficulty": 4,
      "id": 18,
      "question": "How many paintings did Van Gogh sell in his lifetime?"
    },
    {
      "answer": "Jackson Pollock",
      "category": 2,
      "difficulty": 2,
      "id": 19,
      "question": "Which American artist was a pioneer of Abstract Expressionism, and a leading exponent of action painting?"
    },
    {
      "answer": "The Liver",
      "category": 1,
      "difficulty": 4,
      "id": 20,
      "question": "What is the heaviest organ in the human body?"
    },
    {
      "answer": "Alexander Fleming",
      "category": 1,
      "difficulty": 3,
      "id": 21,
      "question": "Who discovered penicillin?"
    },
    {
      "answer": "Blood",
      "category": 1,
      "difficulty": 4,
      "id": 22,
      "question": "Hematology is a branch of medicine involving the study of what?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    },
    {
      "answer": "British Football",
      "category": 6,
      "difficulty": 4,
      "id": 24,
      "question": "What football is the real football?"
    }
  ],
  "success": true
}
```

> **POST /search_question**

- Returns a an array of questions that match the users search query parameters.
- Request arguments: requires a key which in this case is 'SearchTerm and a value which is the string to search for. a sample request argument looks like this:

```
{
    "searchTerm": "title"
}
```

It will return a dictionary:

```
{
  "current_category": "History",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
  ],
  "success": true,
  "total_questions": 2
}
```

> **GET /categories/<int:category_id>/questions**

- Returns a dictionary that includes an array questions filtered to match the id of the category given in the url parameter. Also returns a success message and the total number of questions that match the search query.
- Request arguments: None

```
{
  "current_category": "History",
  "questions": [
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Scarab",
      "category": 4,
      "difficulty": 4,
      "id": 23,
      "question": "Which dung beetle was worshipped by the ancient Egyptians?"
    }
  ],
  "success": true,
  "total_questions": 4
}
```

> **POST /quizzes**

- Returns a dictionary of questions that dont match previously answered questions in the selected category.
- Request arguments: This endpoint requires a two keys. The first key is "previous_questions" and the value is an array of the ids of already answered questions. The second key is "quiz_category" and the value is an object with two more keys an "id" and a "type" and their corresponding values. For example:

```
{
    "previous_questions": [5, 9],
    "quiz_category": {"id": 4, "type":"History"}
}
```

This query will return:

```
{
  "question": {
    "answer": "Scarab",
    "category": 4,
    "difficulty": 4,
    "id": 23,
    "question": "Which dung beetle was worshipped by the ancient Egyptians?"
  },
  "success": true
}
```

## Contributors

- Edori Atiri contributed to this project, specifically to **init**.py, test_flaskr.py and the README.md file in the projects base directory.
- This project was originally created by [Udacity](https://www.udacity.com/) and forked from one of [Udacity's github repository's](https://github.com/udacity/cd0037-API-Development-and-Documentation-project)
