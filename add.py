from flask import Flask, request, jsonify
from flask_jwt_extended import JWTManager, jwt_required, create_access_token, get_jwt_identity

app = Flask(__name__)
app.config['JWT_SECRET_KEY'] = 'super-secret'  # Change this to a long, random string in production
jwt = JWTManager(app)

# Dummy data for courses and enrollments
courses = [
    {"id": 1, "name": "Introduction to Water Resources Engineering", "description": "Learn the basics of water resources engineering.", "duration": "4 weeks", "instructor": "Dr. Smith"},
    {"id": 2, "name": "Advanced Hydrology", "description": "In-depth study of hydrological processes.", "duration": "6 weeks", "instructor": "Prof. Johnson"}
]

enrollments = [
    {"user_id": 1, "course_id": 1},
    {"user_id": 2, "course_id": 2},
]

# Dummy users for authentication
users = {
    "user1": "password1",
    "user2": "password2"
}

# Error handler for 404 Not Found
@app.errorhandler(404)
def not_found_error(error):
    return jsonify({"error": "Not found"}), 404

# Error handler for 500 Internal Server Error
@app.errorhandler(500)
def internal_error(error):
    return jsonify({"error": "Internal server error"}), 500

# API endpoint for generating JWT token
@app.route('/api/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    if username in users and users[username] == password:
        access_token = create_access_token(identity=username)
        return jsonify(access_token=access_token), 200
    else:
        return jsonify({"error": "Invalid username or password"}), 401

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


if __name__ == '__main__':
    app.run(debug=True)
