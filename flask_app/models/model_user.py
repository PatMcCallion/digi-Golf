#! 4 ****Datatypes returned****
# INSERT INTO => INTEGER
# SELECT FROM => LIST OF OBJS/INSTANCES
# UPDATE/DELETE => NOTHING
# ERROR => BOOLEAN (FALSE)


# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash, session
from flask_app import bcrypt
from flask_app.models import model_tracker
import re
# model the class after the friend table from our database
# CHANGE class name to table name but singular! Table Friends => class Friend
DATABASE = 'digi_golf_db'
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


class User:
    def __init__(self, data):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.city = data['city']
        self.state = data['state']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #!!CRUD ------------- CREATE - INSERT INTO
    @classmethod
    def create(cls, data):
        # NOTE add all attributs and %()s for each
        query = "INSERT INTO users (first_name, last_name, email, password, city, state) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s, %(city)s, %(state)s);"
        user_id = connectToMySQL(DATABASE).query_db(query, data)
        return user_id

    #!!CRUD ---------------READ - SELECT
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # ! This ^^^ returns a LIST OF DICTIONARIES, MUST SPECIFY USING List of Dict notation ==> result[index]['key_name']
        # Create an empty list to append our instances of users

        all_users = []
        # Iterate over the db results and create instances of users with cls.
        for dict in results:
            all_users.append(cls(dict))
        return all_users
        # *******THIS MUST BE DONE EVERYTIME TO PASS EXAM************
        # LIST OF INSTANCE/OBJECTS

    @classmethod
    def get_one_by_email(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        if not results:
            return False

        return cls(results[0])

    @classmethod
    def get_one_by_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)

        return cls(results[0])
    #!!CRUD ---------------UPDATE - UPDATE

    @classmethod
    def update_one(cls, data):
        query = """UPDATE users
                SET first_name=%(first_name)s, last_name=%(last_name)s, email=%(email)s, city=%(city)s, state=%(state)s
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    #!!CRUD ---------------DELETE - DELETE
    @classmethod
    def delete_one(cls, data):
        query = """DELETE FROM users WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)


# Needed files always
# create/save - Create
# get_all - Read
# get_one - Read
# update_one - Update
# delete_one - Delete


    @staticmethod
    def validator(data):
        is_valid = True

        if not data['first_name']:
            print("First name needs to be filed out")
            flash("First name needs to be filled out", 'err_user_first_name')
            is_valid = False
        elif not len(data['first_name']) > 2:
            print("First name needs to be more than 2 characters")
            flash("First name needs to be more than 2 characters",
                  'err_user_first_name')
            is_valid = False

        if not data['last_name']:
            print("Last name needs to be filed out")
            flash("Last name needs to be filled out", 'err_user_last_name')
            is_valid = False
        elif not len(data['last_name']) > 2:
            print("Last name needs to be more than 2 characters")
            flash("Last name needs to be more than 2 characters",
                  'err_user_last_name')
            is_valid = False

        if not data['email']:
            print("Email needs to be filed out")
            flash("Email needs to be filled out", 'err_user_email')
            is_valid = False
        elif not EMAIL_REGEX.match(data['email']):
            flash("Invalid email address!", 'err_user_email')
            is_valid = False
        else:
            potential_user = User.get_one_by_email(data)
            if potential_user:
                is_valid = False
                flash("Email already in use", 'err_user_email')

        if not data['reg_password']:
            print("Password needs to be filed out")
            flash("Password needs to be filled out", 'err_user_password')
            is_valid = False
        elif not len(data['reg_password']) > 7:
            print("Password must be Minimum eight characters")
            flash("Password must be Minimum eight characters",
                  'err_user_password')
            is_valid = False

        if not data['confirm_password']:
            print("Confirm password needs to be filed out")
            flash("Confirm Password needs to be filled out",
                  'err_user_confirm_password')
            is_valid = False
        elif data['confirm_password'] != data['reg_password']:
            is_valid = False
            flash("Passwords do not match", 'err_user_confirm_password')

        if not data['city']:
            print("City needs to be filed out")
            flash("City needs to be filled out",
                  'err_user_city')
            is_valid = False
        elif not len(data['city']) > 1:
            print("City needs to be atleast 2 characters")
            flash("City needs to be atleast 2 characters",
                  'err_user_city')
            is_valid = False

        return is_valid

    @ staticmethod
    def validator_login(data):
        is_valid = True

        if not data['email']:
            is_valid = False
            flash("Email is required", "err_user_login_email")

        elif not EMAIL_REGEX.match(data['email']):
            is_valid = False
            flash("Invalid email address!", "err_user_login_email")

        if not data['password']:
            is_valid = False
            flash("Password is required", "err_user_login_password")

        if is_valid:
            possible_user = User.get_one_by_email(data)
            if not possible_user:
                is_valid = False
                flash("Invalid credentials", "err_user_login_password")

            else:
                if not bcrypt.check_password_hash(possible_user.password, data['password']):
                    is_valid = False
                    flash("Invalid credentials", "err_user_login_password")
                else:
                    session['uuid'] = possible_user.id

        return is_valid
