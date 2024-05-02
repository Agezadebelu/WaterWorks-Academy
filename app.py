from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime
from flask_mysqldb import MySQL

app = Flask(__name__)


# CONFIGURATION

#CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql5703438:39hBSZh4HF@sql5.freesqldatabase.com/sql5703438'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

'''
app.config[
    'JWT_SECRET_KEY'] = 'super-secret'  # Change this to a long, random string in production
jwt = JWTManager(app)
app.secret_key = "your_secret_key"
'''


# MODELS

class users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80), unique=False, nullable=False)
  last_name = db.Column(db.String(80), unique=False, nullable=False)
  user_name = db.Column(db.String(80), unique=True, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False, nullable=False)
  organization =db.Column(db.String(120), unique=False, nullable=False)
  role = db.Column(db.String(80), unique=False, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "first_name": self.first_name,
      "last_name": self.last_name,
      "user_name": self.user_name,
      "email": self.email,
      "password": self.password,
      "organization": self.organization,
      "role": self.role
    }


class categories(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  category_name = db.Column(db.String(80), unique=False, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "category_name": self.category_name
    }


class courses(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  category_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  course_name = db.Column(db.String(80), unique=False, nullable=False)
  duration = db.Column(db.String(80), unique=False, nullable=False)
  description = db.Column(db.String(120), unique=True, nullable=False)
  image = db.Column(db.String(120), unique=False, nullable=False)

  def to_json(self):
    return {
      "id": self.id,
      "instructor_d": self.instructor_id,
      "category_id": self.category_id,
      "course_name": self.course_name,
      "duration": self.duration,
      "description": self.description,
      "image": self.image
    }


class modules(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
  module_name = db.Column(db.String(80), unique=False, nullable=False)
  duration = db.Column(db.String(80), unique=False, nullable=False)
  description = db.Column(db.String(120), unique=True, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "course_id": self.course_id,
      "module_name": self.module_name,
      "duration": self.duration,
      "description": self.description
    }


class lessons(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
  quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
  lesson_name = db.Column(db.String(80), unique=False, nullable=False)
  video_url = db.Column(db.String(100), unique=False, nullable=False)
  content = db.Column(db.String(5000), unique=False, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "module_id": self.module_id,
      "quiz_id": self.quiz_id,
      "lesson_name": self.lesson_name,
      "video_url": self.video_url,
      "content": self.content
    }


class quizs(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  questions = db.Column(db.String(1000), unique=False, nullable=False)
  answers = db.Column(db.String(1000), unique=False, nullable=False)
  correct_answer = db.Column(db.String(1000), unique=False, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "questions": self.questions,
      "answers": self.answers,
      "correct_ansewr": self.correct_answer
    }

'''
enrollments = [
    {
        "user_id": 1,
        "course_id": 1
    },
    {
        "user_id": 2,
        "course_id": 2
    },
]

# Dummy users for authentication
users = {"user1": "password1", "user2": "password2"}
'''

@app.route('/')
def index():
  Courses = courses.query.all()
  json_courses = list(map(lambda x: x.to_json(), Courses))
  Categories = categories.query.all()
  json_categories = list(map(lambda x: x.to_json(), Categories))
  return render_template('index.html', categories=json_categories, courses=json_courses)


@app.route('/home')
def home():
  Courses = courses.query.all()
  json_courses = list(map(lambda x: x.to_json(), Courses))
  Categories = categories.query.all()
  json_categories = list(map(lambda x: x.to_json(), Categories))
  return render_template('index.html', categories=json_categories, courses=json_courses)


@app.route('/courses')
def course_list():
  Courses = courses.query.all()
  json_courses = list(map(lambda x: x.to_json(), Courses))
  return render_template('course-list.html', courses=json_courses)


@app.route('/category')
def category():
  Courses = courses.query.all()
  json_courses = list(map(lambda x: x.to_json(), Courses))
  Categories = categories.query.all()
  json_categories = list(map(lambda x: x.to_json(), Categories))
  return render_template('category.html', categories=json_categories, courses=json_courses)


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/register')
def register():
  return render_template('register.html')


@app.route('/enrollement')
def enrollement():
  return render_template('enrollement.html')


@app.route('/module')
def module():
  Courses = courses.query.all()
  json_courses = list(map(lambda x: x.to_json(), Courses))
  Modules = modules.query.all()
  json_modules = list(map(lambda x: x.to_json(), Modules))
  Lessons = lessons.query.all()
  json_lessons = list(map(lambda x: x.to_json(), Lessons))
  return render_template('module-view.html', modules=json_modules, courses=json_courses, lessons=json_lessons)


@app.route('/lesson')
def lesson():
  return render_template('lesson-view.html', lessons=lessons)


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
  return jsonify({"error": "Not found"}), 404


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
  return jsonify({"error": "Internal server error"}), 500


# API endpoint for generating JWT token
@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
    data = request.json
    if data is not None and "username" in data and "password" in data:
      username = data.get("username")
      password = data.get("password")
      if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
      else:
        return jsonify({"error": "Invalid username or password"}), 401
    else:
      return jsonify({"error": "Missing username or password in request data"}), 400
  return render_template('login.html')


@app.route('/logout')
def logout():
  # Clear session data
  session.clear()
  # Redirect to the login page (you can customize the redirect URL)
  return redirect(url_for('home'))

"""
# Protected API endpoints with authentication and authorization
@app.route('/api/courses', methods=['GET', 'POST'])
@jwt_required()
def courses_api():
  current_user = get_jwt_identity()
  if current_user == "user1":
    if request.method == 'GET':
      return jsonify(courses)
    elif request.method == 'POST':
      data = request.json
      new_course = {
          "id": len(courses) + 1,
          "name": data.get("name"),
          "description": data.get("description"),
          "duration": data.get("duration"),
          "instructor": data.get("instructor")
      }
      courses.append(new_course)
      return jsonify(new_course), 201
  else:
    return jsonify({"error": "Unauthorized access"}), 403


@app.route('/api/enrollments', methods=['GET', 'POST'])
@jwt_required()
def enrollments_api():
  # Implementation similar to courses_api, add authorization as needed
  pass


@app.route('/api/modules', methods=['GET', 'POST'])
@jwt_required()
def modules_api():
  # Implementation similar to courses_api, add authorization as needed
  pass



@app.route('/course-list')
def course_list():
    # Placeholder for fetching course data from database
    courses = Course.query.all()
    return render_template('course-list.html', courses=courses)


# Define API endpoints to retrieve dynamic content
@app.route('/api/courses')
def api_courses():
    # Placeholder for fetching course data from database
    courses = Course.query.all()
    course_data = [{'name': course.name, 'instructor': course.instructor, 'description': course.description} for course in courses]
    return jsonify(course_data)


@app.route('/api/course-detail')
def api_course_detail():
    # Placeholder for fetching course detail data from database
    course_detail = {'name': 'Course Name', 'instructor': 'Instructor Name', 'description': 'Course Description'}
    return jsonify(course_detail)

@app.route('/api/module-view')
def api_module_view():
    # Placeholder for fetching module view data from database
    module_view = {'name': 'Module Name', 'description': 'Module Description'}
    return jsonify(module_view)

@app.route('/api/lesson-view')
def api_lesson_view():
    # Placeholder for fetching lesson view data from database
    lesson_view = {'name': 'Lesson Name', 'content': 'Lesson Content'}
    return jsonify(lesson_view)
"""

if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
