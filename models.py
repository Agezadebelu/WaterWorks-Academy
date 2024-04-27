from app import db
from datetime import datetime


class user(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(80), unique=False, nullable=False)
    last_name = db.Column(db.String(80), unique=False, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    user_name = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), unique=False, nullable=False)
    organization =db.Column(db.String(120), unique=False, nullable=False)
    role = db.Column(db.String(80), unique=False, nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "firstName": self.first_name,
            "lastName": self.last_name,
            "email": self.email,
            "userName": self.user_name,
            "password": self.password,
            "organization": self.organization,
            "role": self.role
        }


class course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    instructor_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_name = db.Column(db.String(80), unique=False, nullable=False)
    duration = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)

    def to_json(self):
        return {
            "instructorId": self.instructor_id,
            "courseName": self.course_name,
            "duration": self.duration,
            "description": self.description
        }
    

class module(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_name = db.Column(db.String(80), unique=False, nullable=False)
    duration = db.Column(db.String(80), unique=False, nullable=False)
    description = db.Column(db.String(120), unique=True, nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "moduleName": self.module_name,
            "duration": self.duration,
            "description": self.description,
            "courseId": self.course_id
        }


class enrollment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
    enrollment_date = db.Column(db.DateTime, default=datetime.now(datetime.UTC))


    def to_json(self):
        return {
            "id": self.id,
            "userId": self.user_id,
            "courseId": self.course_id,
            "enrollmentDate": self.enrollment_date
        }


class lesson(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'), nullable=False)
    lesson_name = db.Column(db.String(80), unique=False, nullable=False)
    video_url = db.Column(db.String(100), unique=False, nullable=False)
    content = db.Column(db.String(5000), unique=False, nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "moduleId": self.module_id,
            "quizId": self.quiz_id,
            "lessonName": self.lesson_name,
            "videoUrl": self.video_url,
            "content": self.content
        }


class quiz(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    module_id = db.Column(db.Integer, db.ForeignKey('module.id'), nullable=False)
    questions = db.Column(db.String(1000), unique=False, nullable=False)
    answers = db.Column(db.String(1000), unique=False, nullable=False)
    correct_answer = db.Column(db.String(1000), unique=False, nullable=False)


    def to_json(self):
        return {
            "id": self.id,
            "moduleId": self.module_id,
            "questions": self.questions,
            "answers": self.answers,
            "correctAnsewr": self.correct_answer
        }