import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get("page", 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)

    CORS(app)

    """
    Use the after_request decorator to set Access-Control-Allow
    """
    @app.after_request
    def after_request(response):
        response.headers.add(
            'Access-Control-Allow-Headers',
            'Content-Type,Authorization,true')
        response.headers.add(
            'Access-Control-Allow-Methods',
            'GET,PUT,POST,DELETE,OPTIONS')
        return response

    """
    Create an endpoint to handle GET requests
    for all available categories.
    """
    @app.route('/categories')
    def get_categories():
        categories = Category.query.order_by(Category.id).all()
        current_categories = [category.format() for category in categories]
        if len(categories) == 0:
            abort(404)

        new_category = []
        for c in current_categories:
            new_obj = {c['id']: c['type']}
            new_category.append(new_obj)
        category_obj = {}
        for i in new_category:
            category_obj.update(i)

        return jsonify({
            "success": True,
            "categories": category_obj,
            "total_categories": len(Category.query.all())
        })

    """
    Create an endpoint to handle GET requests for questions,
    including pagination (every 10 questions).
    This endpoint should return a list of questions,
    number of total questions, current category, categories.
    """
    @app.route("/questions")
    def get_questions():
        questions = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, questions)
        categories = Category.query.order_by(Category.id).all()
        current_categories = [category.format() for category in categories]

        new_category = []
        current_category_arr = []
        for c in current_categories:
            new_obj = {c['id']: c['type']}
            new_category.append(new_obj)
            current_category_arr.append(c['type'])
        category_obj = {}
        for i in new_category:
            category_obj.update(i)

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            "success": True,
            "questions": current_questions,
            "total_questions": len(Question.query.all()),
            "categories": category_obj,
            "current_category": current_category_arr,
        })

    """
    Create an endpoint to DELETE question using a question ID.
    """

    @app.route("/questions/<int:question_id>", methods=["DELETE"])
    def delete_question(question_id):

        try:
            question = Question.query.filter(
                Question.id == question_id).one_or_none()

            if question is None:
                abort(422)

            question.delete()

            return jsonify({
                'success': True,
                'deleted': question_id,
            })

        except BaseException:
            abort(422)

    """
    Create an endpoint to POST a new question,
    which will require the question and answer text,
    category, and difficulty score.
    """
    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_difficulty = body.get('difficulty', None)
        new_category = body.get('category', None)

        try:
            question = Question(
                question=new_question,
                answer=new_answer,
                difficulty=new_difficulty,
                category=new_category
            )

            question.insert()

            questions = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, questions)

            return jsonify({
                'success': True,
                'questions': current_questions
            })

        except BaseException:
            abort(422)

    """
    Create a POST endpoint to get questions based on a search term.
    It should return any questions for whom the search term
    is a substring of the question.
    """
    @app.route('/search_question', methods=['POST'])
    def search_questions():
        body = request.get_json()

        search_term = body.get('searchTerm', None)

        try:
            results = Question.query.order_by(
                Question.id).filter(
                Question.question.ilike(
                    '%{}%'.format(search_term)))

            current_questions = paginate_questions(request, results)
            category = Category.query.filter(
                Category.id == current_questions[0]['category']).one_or_none()

            return jsonify({
                'success': True,
                'questions': current_questions,
                'total_questions': len(results.all()),
                'current_category': category.type
            })

        except BaseException:
            abort(422)

    """
    Create a GET endpoint to get questions based on category.
    """
    @app.route("/categories/<int:category_id>/questions")
    def get_question_with_category(category_id):
        questions = Question.query.filter(
            Question.category == category_id).all()
        category = Category.query.filter(
            Category.id == category_id).one_or_none()

        if len(questions) == 0:
            abort(404)

        return jsonify({
            "success": True,
            'questions': [question.format() for question in questions],
            "total_questions": len(questions),
            'current_category': category.type
        })

    """
    Create a POST endpoint to get questions to play the quiz.
    This endpoint should take category and previous question parameters
    and return a random questions within the given category,
    if provided, and that is not one of the previous questions.
    """
    @app.route("/quizzes", methods=["POST"])
    def play_quiz():
        body = request.get_json()

        # Check if category and previous question actually exist to handle
        # unexpected error
        if 'category' not in body and 'previous_questions' not in body:
            abort(422)

        category = body.get('quiz_category')
        prev_questions = body.get('previous_questions')

        try:
            if category['type'] == 'click':
                questions = Question.query.filter(
                    Question.id.notin_(prev_questions)).all()
            else:
                questions = Question.query.filter_by(
                    category=category['id']).filter(
                        Question.id.notin_(prev_questions)).all()

            if len(questions) > 0:
                next_question = questions[random.randrange(
                    0, len(questions))].format()
            else:
                next_question = None

            return jsonify({
                'success': True,
                'question': next_question
            })
        except BaseException:
            abort(422)

    """
    Create error handlers for all expected errors
    including 404 and 422.
    """
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({
            "success": False,
            "error": 400,
            "message": "Bad request"
        }), 400

    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            "success": False,
            "error": 404,
            "message": "Resource not found"
        }), 404

    @app.errorhandler(405)
    def not_allowed(error):
        return jsonify({
            "success": False,
            "error": 405,
            "message": "Method not allowed"
        }), 405

    @app.errorhandler(422)
    def unprocessable_entry(error):
        return jsonify({
            "success": False,
            "error": 422,
            "message": "Unprocessable entry"
        }), 422

    @app.errorhandler(500)
    def internal_server_error(error):
        return jsonify({
            "success": False,
            "error": 500,
            "message": "Internal server error, please try again later"
        }), 500

    return app
