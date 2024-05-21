-- MySQL dump 
--
-- Host: localhost    Database: waterworks_db
-- ------------------------------------------------------
SHOW databases;



-- Create database + tabels if doesn't exist
CREATE DATABASE IF NOT EXISTS waterworks_db;
-- CREATE USER IF NOT EXISTS 'root'@'localhost';
-- SET PASSWORD FOR 'root'@'localhost' = '12345678@mysql';
-- GRANT ALL ON waterworks_db.* TO 'root'@'localhost';
-- GRANT SELECT ON performance_schema.* TO 'root'@'localhost';
-- FLUSH PRIVILEGES;

USE waterworks_db;

--
-- Table structure for table `users`
--
DROP TABLE IF EXISTS `users`;

CREATE TABLE `users` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `first_name` varchar(50) NOT NULL,
  `last_name` varchar(50) NOT NULL,
  `user_name` varchar(50) NOT NULL,
  `email` varchar(50) NOT NULL,
  `password` varchar(50) NOT NULL,
  `organization` varchar(50) NOT NULL,
  `role` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `users`
--

INSERT INTO `users` VALUES (1, '2017-03-25 19:44:42','2017-03-25 19:44:42', 'Ageza', 'Debelu', 'agezadeb', 'lateradeb09@gmail.com', '12345678@w', 'Dilla University', 'lecturer');

--
-- Table structure for table `category`
--
DROP TABLE IF EXISTS `categories`;

CREATE TABLE `categories` (
  `id` int NOT NULL AUTO_INCREMENT ,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `category_name` varchar(250) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `categories`
--

INSERT INTO `categories` VALUES (1, '2017-03-25 19:44:42','2017-03-25 19:44:42', 'Surface Water Hydrology');

--
-- Table structure for table `course`
--
DROP TABLE IF EXISTS `courses`;

CREATE TABLE `courses` (
  `id` int NOT NULL AUTO_INCREMENT,
  `instructor_id` int NOT NULL,
  `category_id` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `course_name` varchar(250) NOT NULL,
  `duration` varchar(128) NOT NULL,
  `description` varchar(5000) NOT NULL,
  `image` varchar(250) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `instructor_id` (`instructor_id`),
  KEY `category_id` (`category_id`),
  CONSTRAINT `courses_ibfk_1` FOREIGN KEY (`instructor_id`) REFERENCES `users` (`id`),
  CONSTRAINT `courses_ibfk_2` FOREIGN KEY (`category_id`) REFERENCES `categories` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `courses`
--

INSERT INTO `courses` VALUES (1, 1, 1, '2017-03-25 19:44:42','2017-03-25 19:44:42', 'Advanced Hydrology', '4 weeks', 'Description 1', 'image link');

--
-- Table structure for table `modules`
--
DROP TABLE IF EXISTS `modules`;

CREATE TABLE `modules` (
  `id` int NOT NULL AUTO_INCREMENT,
  `course_id` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `module_name` varchar(250) NOT NULL,
  `duration` varchar(128) NOT NULL,
  `description` varchar(5000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `modules_ibfk_1` FOREIGN KEY (`course_id`) REFERENCES `courses` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `module`
--

INSERT INTO `modules` VALUES (1, 1, '2017-03-25 19:44:42', '2017-03-25 19:44:42', 'module: 1. Advanced Hydrology', '4 weeks', 'Description 1');

--
-- Table structure for table `lesson`
--
DROP TABLE IF EXISTS `lessons`;

CREATE TABLE `lessons` (
  `id` int NOT NULL AUTO_INCREMENT,
  `module_id` int NOT NULL,
  `quiz_id` int NOT NULL,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `lesson_name` varchar(250) NOT NULL,
  `video_url` varchar(250) NOT NULL,
  `content` varchar(5000) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `module_id` (`module_id`),
  CONSTRAINT `lessons_ibfk_1` FOREIGN KEY (`module_id`) REFERENCES `modules` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `lesson`
--

INSERT INTO `lessons` VALUES (1, 1, 1, '2017-03-25 19:44:42', '2017-03-25 19:44:42', 'lesson: 1. Advanced Hydrology', 'url: 1 link', 'content: 1');

--
-- Table structure for table `quizs`
--
DROP TABLE IF EXISTS `quizs`;

CREATE TABLE `quizs` (
  `id` int NOT NULL AUTO_INCREMENT,
  `created_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `questions` varchar(500) NOT NULL,
  `answers` varchar(600) NOT NULL,
  `correct_answer` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `quizs`
--

INSERT INTO `quizs` VALUES (1, '2017-03-25 19:44:42', '2017-03-25 19:44:42', 'question: 1. Advanced Hydrology', 'answer: 1. Advanced Hydrology', 'correct answer: 1. Advanced Hydrology');
