from app import db
from datetime import datetime



# MODELS

class users(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
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
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
  category_name = db.Column(db.String(80), unique=False, nullable=False)


  def to_json(self):
    return {
      "id": self.id,
      "category_name": self.category_name
    }


class courses(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
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
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
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


class enrollments(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
  course_id = db.Column(db.Integer, db.ForeignKey('course.id'), nullable=False)
  enrollment_date = db.Column(db.DateTime, default=datetime.utcnow)


  def to_json(self):
    return {
      "id": self.id,
      "user_id": self.user_id,
      "course_id": self.course_id,
      "enrollment_date": self.enrollment_date
    }


class lessons(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
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
  created_at =  db.Column(db.DateTime, default=datetime.utcnow)
  updated_at = db.Column(db.DateTime, default=datetime.utcnow)
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