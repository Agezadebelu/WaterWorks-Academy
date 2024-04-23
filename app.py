from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
""""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/waterworks_db'  # Replace with your MySQL database URI
db = SQLAlchemy(app)

# Define Course model
class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    instructor = db.Column(db.String(100))
    description = db.Column(db.Text)
"""


@app.route('/')
def index():
  return render_template('index.html')


@app.route('/home')
def home():
  return render_template('index.html')


@app.route('/courses')
def course_list():
  # Placeholder for fetching course data from database
  # courses = Course.query.all()
  return render_template('course-list.html')


@app.route('/about')
def about():
  return render_template('about.html')


@app.route('/contact')
def contact():
  return render_template('contact.html')


@app.route('/login')
def login():
  return render_template('login.html')

@app.route('/signup')
def signup():
  return render_template('signup.html')


"""
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
