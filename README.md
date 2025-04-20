# Student-Result-Management-System

Overview
The Student Result Management System is a web-based application developed using Python, Django, and PostgreSQL. The system allows administrators to manage student records, including adding student data, assigning subjects, and storing marks. It also provides functionality to calculate the total, average, and grades for each student and view the results of top-performing students.

Features:
  Student Management: Add, edit, and delete student records.
  Subject Management: Add, edit, and delete subjects.
  Result Management: Assign marks to students for different subjects.
  Result Calculation: Automatically calculates the total, average, and grades for each student.
  Top Performers: Display the top-performing students based on their results.
  Data Integrity: Ensures data consistency and integrity using database constraints and relationships.

Tech Stack
  Backend: Python (Django)
  Database: PostgreSQL
  Frontend: HTML, CSS (for styling)
  Others:
  Django's ORM for database interaction
  PL/pgSQL functions for result management and queries

Usage
Available Pages:
  Add Student: Add new student records by entering the student's name and other details.
  Add Subject: Add new subjects to the system.
  Add Marks: Assign marks to students for different subjects.
  View Results: View student results, including the student's name, subjects, marks, and grade.
  View Top Performers: See a list of top-performing students based on their total marks.

Database Schema
  The database consists of the following main tables:
  Student: Stores information about each student.
  Subject: Stores information about subjects.
  Result: Stores marks for each student in each subject.
