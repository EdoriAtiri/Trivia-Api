import os
from dotenv import load_dotenv
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category

load_dotenv()

DB_HOST = os.environ["DB_HOST"]
DB_USER = os.environ["DB_USER"]
DB_PASSWORD = os.environ["DB_PASSWORD"]
DB_NAME = os.environ["DB_NAME"] + '_test'
DB_PATH = "postgresql://{}:{}@{}/{}".format(
    DB_USER, DB_PASSWORD, DB_HOST, DB_NAME
)


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = DB_PATH
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_get_all_categories(self):
        res = self.client().get('/categories')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['total_categories'])
        self.assertTrue(len(data['categories']))

    def test_404_for_requesting_invalid_page(self):
        res = self.client().get('/categoriess')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Resource not found")

    def test_get_paginated_questions(self):
        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['total_questions'])
        self.assertEqual(len(data['current_category']), 6)
        self.assertTrue(len(data['categories']))

    def test_404_for_getting_invalid_page(self):
        res = self.client().get('/questions?page=4004')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_create_new_question(self):
        res = self.client().post(
            '/questions',
            json={
                'question': 'What football is the real football?',
                'answer': 'British Football',
                'difficulty': 4,
                'category': 6})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))

    def test_405_question_creation_not_allowed(self):
        res = self.client().post(
            '/questions/67',
            json={
                'question': 'What football is the real football?',
                'answer': 'British Football',
                'difficulty': 4,
                'category': 6})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 405)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Method not allowed')

    def test_search_questions(self):
        res = self.client().post(
            '/search_question',
            json={
                "searchTerm": "title"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 2)
        self.assertTrue(len(data['questions']))

    def test_search_questions_no_results(self):
        res = self.client().post(
            '/search_question',
            json={
                "searchTerm": "untitled"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entry')

    def test_get_questions_based_on_category(self):
        res = self.client().get('/categories/4/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['total_questions'], 4)
        self.assertEqual(data['current_category'], 'History')
        self.assertTrue(len(data['questions']))

    def test_404_for_get_questions_for_unavailable_category(self):
        res = self.client().get('/categories/1899/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Resource not found')

    def test_play_quiz_category(self):

        res = self.client().post('/quizzes', json={
            "previous_questions": [5, 9],
            "quiz_category": {"id": 4, "type": "History"}
        })
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200),
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['question']))

    def test_422_for_play_quiz_without_category_or_prev_question(self):
        res = self.client().post('/quizzes', json='')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entry')

#   Change the id every time you run this test
    def test_delete_question_using_id(self):
        res = self.client().delete('/questions/17')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 17).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 17)
        self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):
        res = self.client().delete('/questions/100')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'Unprocessable entry')


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
