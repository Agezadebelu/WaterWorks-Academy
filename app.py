from flask import Flask, render_template, jsonify, request, redirect, url_for, session, flash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
'''
CORS(app)

# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://username:password@localhost/waterworks_db'  # Replace with your MySQL database URI
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

app.config[
    'JWT_SECRET_KEY'] = 'super-secret'  # Change this to a long, random string in production
jwt = JWTManager(app)
app.secret_key = "your_secret_key"

# Dummy data for courses and enrollments
courses = [{
    "id": 1,
    "name": "Introduction to Water Resources Engineering",
    "description": "Learn the basics of water resources engineering.",
    "duration": "4 weeks",
    "instructor": "Dr. Smith"
}, {
    "id": 2,
    "name": "Advanced Hydrology",
    "description": "In-depth study of hydrological processes.",
    "duration": "6 weeks",
    "instructor": "Prof. Johnson"
}]

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
'''
# Dummy users for authentication
users = {"user1": "password1", "user2": "password2"}


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


@app.route('/register')
def register():
  return render_template('register.html')


@app.route('/enrollement')
def enrollement():
  return render_template('enrollement.html')


@app.route('/module')
def module():
  return render_template('module-view.html')


@app.route('/lesson')
def lesson():
  return render_template('lesson-view.html')


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
      return jsonify({"error":
                      "Missing username or password in request data"}), 400
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
