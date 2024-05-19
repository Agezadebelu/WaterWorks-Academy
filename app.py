from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, LoginManager, UserMixin
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from datetime import datetime


app = Flask(__name__)


# CONFIGURATION
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://sql5703438:39hBSZh4HF@sql5.freesqldatabase.com/sql5703438'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config['SECRET_KEY'] = 'your_secret_key'
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.login_view = 'login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return users.query.get(int(user_id))

# MODELS
class users(UserMixin, db.Model):
  id = db.Column(db.Integer, primary_key=True)
  first_name = db.Column(db.String(80), unique=False, nullable=False)
  last_name = db.Column(db.String(80), unique=False, nullable=False)
  email = db.Column(db.String(120), unique=True, nullable=False)
  password = db.Column(db.String(120), unique=False)
  organization =db.Column(db.String(120), unique=False, nullable=False)
  role = db.Column(db.String(80), unique=False, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "first_name": self.first_name,
      "last_name": self.last_name,
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


# ROUTES
@app.route('/home')
@app.route('/')
@login_required
def index():
  Courses = courses.query.all()
  json_courses = list(map(lambda x: x.to_json(), Courses))
  Categories = categories.query.all()
  json_categories = list(map(lambda x: x.to_json(), Categories))
  return render_template('index.html', categories=json_categories, courses=json_courses)


@app.route('/courses')
@login_required
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


@app.route('/about')
@login_required
def about():
  return render_template('about.html')


@app.route('/contact')
@login_required
def contact():
  return render_template('contact.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
  if request.method == 'POST':
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False
    user = users.query.filter_by(email=email).first()
    # check if user actually exists
    # take the user supplied password, hash it, and compare it to the hashed password in database
    if not user or not password: 
        flash('Please check your login details and try again.')
        return redirect(url_for('login'))

    # if the above check passes, then we know the user has the right credentials
    login_user(user, remember=remember)
    return redirect(url_for('index'))
    #return redirect(url_for('home'))
  return render_template('login.html')


@app.route('/register', methods=['GET','POST'])
def register():
  if request.method == 'POST':
    first_name = request.form.get('first_name')
    last_name = request.form.get('last_name')
    email = request.form.get('email')
    password = request.form.get('password')
    organization = request.form.get('organization')
    role = request.form.get('role')

    user = users.query.filter_by(email=email).first() # if this returns a user, then the email already exists in database

    if user: # if a user is found, we want to redirect back to signup page so user can try again  
        flash('Email address already exists')
        return redirect(url_for('register'))

    new_user = users()
    new_user.first_name = first_name
    new_user.last_name = last_name
    new_user.email = email
    new_user.password = password
    new_user.organization = organization
    new_user.role = role

    db.session.add(new_user)
    db.session.commit()
    flash('User registered successfully')
    return redirect(url_for('login'))
  return render_template('register.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
  return jsonify({"error": "Not found"}), 404


# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
  return jsonify({"error": "Internal server error"}), 500


if __name__ == "__main__":
  with app.app_context():
    db.create_all()
  app.run(host='0.0.0.0', debug=True)
