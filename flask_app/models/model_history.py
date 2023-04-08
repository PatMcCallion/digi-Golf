#! 4 ****Datatypes returned****
# INSERT INTO => INTEGER
# SELECT FROM => LIST OF OBJS/INSTANCES
# UPDATE/DELETE => NOTHING
# ERROR => BOOLEAN (FALSE)


# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
# CHANGE class name to table name but singular! Table Friends => class Friend
DATABASE = 'digi_golf_db'


class History:
    def __init__(self, data):
        self.id = data['id']
        self.course_name = data['course_name']
        self.course_par = data['course_par']
        self.score = data['score']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.tracker_id = data['tracker_id']

    #!!CRUD ------------- CREATE - INSERT INTO
    @classmethod
    def create(cls, data):
        # NOTE add all attributs and %()s for each
        query = "INSERT INTO histories (course_name, course_par, score, user_id, tracker_id) VALUES (%(course_name)s, %(course_par)s, %(score)s, %(tracker_id)s, %(city)s, %(state)s, %(user_id)s);"
        history_id = connectToMySQL(DATABASE).query_db(query, data)
        return history_id

    #!!CRUD ---------------READ - SELECT
    # Now we use class methods to query our database

    @classmethod
    def get_all(cls):
        query = "histories;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query)
        # ! This ^^^ returns a LIST OF DICTIONARIES, MUST SPECIFY USING List of Dict notation ==> result[index]['key_name']
        # Create an empty list to append our instances of histories

        all_histories = []
        # Iterate over the db results and create instances of histories with cls.
        for dict in results:
            all_histories.append(cls(dict))
        return all_histories
        # *******THIS MUST BE DONE EVERYTIME TO PASS EXAM************
        # LIST OF INSTANCE/OBJECTS

    @classmethod
    def get_one_user_(cls, data):
        query = "SELECT * FROM histories WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    #!!CRUD ---------------UPDATE - UPDATE

    @classmethod
    def update_one(cls, data):
        query = """UPDATE histories
                SET course_name=%(course_name)s, course_par=%(course_par)s, score=%(score)s, user_id=%(user_id)s, tracker_id=%(tracker_id)s
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    #!!CRUD ---------------DELETE - DELETE
    @classmethod
    def delete_one(cls, data):
        query = """DELETE FROM histories WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)


# Needed files always
# create/save - Create
# get_all - Read
# get_one - Read
# update_one - Update
# delete_one - Delete
