from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re

DB = "emails_schema"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')

class Email:
    def __init__(self, data):
        self.id = data['id']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls,data):
        query = "INSERT INTO emails (email, created_at, updated_at) VALUES (%(email)s, NOW(), NOW());"
        return connectToMySQL(DB).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM emails;"

        results = connectToMySQL(DB).query_db(query)

        emails = []

        for email in results:
            emails.append(cls(email))

        return emails

    @staticmethod
    def validate_email(email):
        is_valid = True # we assume this is true

        if len(email['email']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        elif not EMAIL_REGEX.match(email['email']):
            flash("Invalid email address!")
            is_valid = False

        return is_valid   