#! 4 ****Datatypes returned****
# INSERT INTO => INTEGER
# SELECT FROM => LIST OF OBJS/INSTANCES
# UPDATE/DELETE => NOTHING
# ERROR => BOOLEAN (FALSE)


# import the function that will return an instance of a connection
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import model_user
# model the class after the friend table from our database
# CHANGE class name to table name but singular! Table Friends => class Friend
DATABASE = 'digi_golf_db'


class Tracker:
    def __init__(self, data):
        self.id = data['id']
        self.course_name = data['course_name']
        self.course_city = data['course_city']
        self.course_state = data['course_state']
        self.holes_played = data['holes_played']
        self.hole_1 = data['hole_1']
        self.hole_2 = data['hole_2']
        self.hole_3 = data['hole_3']
        self.hole_4 = data['hole_4']
        self.hole_5 = data['hole_5']
        self.hole_6 = data['hole_6']
        self.hole_7 = data['hole_7']
        self.hole_8 = data['hole_8']
        self.hole_9 = data['hole_9']
        self.hole_10 = data['hole_10']
        self.hole_11 = data['hole_11']
        self.hole_12 = data['hole_12']
        self.hole_13 = data['hole_13']
        self.hole_14 = data['hole_14']
        self.hole_15 = data['hole_15']
        self.hole_16 = data['hole_16']
        self.hole_17 = data['hole_17']
        self.hole_18 = data['hole_18']
        self.par_1 = data['par_1']
        self.par_2 = data['par_2']
        self.par_3 = data['par_3']
        self.par_4 = data['par_4']
        self.par_5 = data['par_5']
        self.par_6 = data['par_6']
        self.par_7 = data['par_7']
        self.par_8 = data['par_8']
        self.par_9 = data['par_9']
        self.par_10 = data['par_10']
        self.par_11 = data['par_11']
        self.par_12 = data['par_12']
        self.par_13 = data['par_13']
        self.par_14 = data['par_14']
        self.par_15 = data['par_15']
        self.par_16 = data['par_16']
        self.par_17 = data['par_17']
        self.par_18 = data['par_18']
        self.course_par = (data['par_1'] + data['par_2'] + data['par_3'] + data['par_4'] + data['par_5'] + data['par_6'] + data['par_7'] + data['par_8'] + data['par_9'] +
                           data['par_10'] + data['par_11'] + data['par_12'] + data['par_13'] +
                           data['par_14'] + data['par_15'] + data['par_16'] + data['par_17'] + data['par_18'])
        self.total_strokes = (data['hole_1'] + data['hole_2'] + data['hole_3'] + data['hole_4'] + data['hole_5'] + data['hole_6'] + data['hole_7'] + data['hole_8'] + data['hole_9'] +
                              data['hole_10'] + data['hole_11'] + data['hole_12'] + data['hole_13'] +
                              data['hole_14'] + data['hole_15'] + data['hole_16'] + data['hole_17'] + data['hole_18'])
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']

    #!!CRUD ------------- CREATE - INSERT INTO
    @classmethod
    def create(cls, data):
        # NOTE add all attributs and %()s for each
        query = "INSERT INTO trackers (course_name, course_city, course_state, holes_played, hole_1, hole_2, hole_3, hole_4, hole_5, hole_6, hole_7, hole_8, hole_9, hole_10, hole_11, hole_12, hole_13, hole_14, hole_15, hole_16, hole_17, hole_18, user_id) VALUES (%(course_name)s, %(course_city)s, %(course_state)s, %(holes_played)s, %(hole_1)s, %(hole_2)s, %(hole_3)s, %(hole_4)s, %(hole_5)s, %(hole_6)s, %(hole_7)s, %(hole_8)s, %(hole_9)s, %(hole_10)s, %(hole_11)s, %(hole_12)s, %(hole_13)s, %(hole_14)s, %(hole_15)s, %(hole_16)s, %(hole_17)s, %(hole_18)s, %(user_id)s);"
        tracker_id = connectToMySQL(DATABASE).query_db(query, data)
        return tracker_id

    @classmethod
    def create_tracker_holes_null(cls, data):
        query = "INSERT INTO trackers (course_name, course_city, course_state, holes_played, hole_1, hole_2, hole_3, hole_4, hole_5, hole_6, hole_7, hole_8, hole_9, hole_10, hole_11, hole_12, hole_13, hole_14, hole_15, hole_16, hole_17, hole_18, par_1, par_2, par_3, par_4, par_5, par_6, par_7, par_8, par_9, par_10, par_11, par_12, par_13, par_14, par_15, par_16, par_17, par_18, user_id) VALUES (%(course_name)s, %(course_city)s, %(course_state)s, %(holes_played)s, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, %(user_id)s);"
        tracker_id = connectToMySQL(DATABASE).query_db(query, data)
        return tracker_id

    #!!CRUD ---------------READ - SELECT
    # Now we use class methods to query our database

    @classmethod
    def get_all_trackers_user(cls, data):
        query = "SELECT * FROM trackers LEFT JOIN users ON trackers.user_id = users.id WHERE user_id = %(user_id)s;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DATABASE).query_db(query, data)
        # ! This ^^^ returns a LIST OF DICTIONARIES, MUST SPECIFY USING List of Dict notation ==> result[index]['key_name']
        # Create an empty list to append our instances of trackers

        all_trackers = []
        for dict in results:
            all_trackers.append(cls(dict))

        tracker_instance = cls(dict)
        user_data = {
            # conflicting
            'id': dict['users.id'],
            'created_at': dict['users.created_at'],
            'updated_at': dict['users.updated_at'],
            # non-conflicting
            'first_name': dict['first_name'],
            'last_name': dict['last_name'],
            'email': dict['email'],
            'password': dict['password'],
            'city': dict['city'],
            'state': dict['state']
        }
        user_instance = model_user.User(user_data)
        all_trackers.append(user_instance)
        tracker_instance.single_user = all_trackers

        return tracker_instance
        # *******THIS MUST BE DONE EVERYTIME TO PASS EXAM************
        # LIST OF INSTANCE/OBJECTS

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM trackers WHERE id = %(id)s"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    @classmethod
    def get_most_recent(cls, data):
        query = "SELECT * from trackers WHERE user_id = %(user_id)s ORDER BY id DESC LIMIT 1;"
        results = connectToMySQL(DATABASE).query_db(query, data)
        return cls(results[0])

    #!!CRUD ---------------UPDATE - UPDATE

    @classmethod
    def update_edit_form(cls, data):
        query = """UPDATE trackers 
                SET course_name=%(course_name)s, course_city=%(course_city)s, course_state=%(course_state)s, holes_played=%(holes_played)s, hole_1=%(hole_1)s, hole_2=%(hole_2)s, hole_3=%(hole_3)s, hole_4=%(hole_4)s, hole_5=%(hole_5)s, hole_6=%(hole_6)s, hole_7=%(hole_7)s, hole_8=%(hole_8)s, hole_9=%(hole_9)s, hole_10=%(hole_10)s, hole_11=%(hole_11)s, hole_12=%(hole_12)s, hole_13=%(hole_13)s, hole_14=%(hole_14)s, hole_15=%(hole_15)s, hole_16=%(hole_16)s, hole_17=%(hole_17)s, hole_18=%(hole_18)s, par_1=%(par_1)s, par_2=%(par_2)s, par_3=%(par_3)s, par_4=%(par_4)s, par_5=%(par_5)s, par_6=%(par_6)s, par_7=%(par_7)s, par_8=%(par_8)s, par_9=%(par_9)s, par_10=%(par_10)s, par_11=%(par_11)s, par_12=%(par_12)s, par_13=%(par_13)s, par_14=%(par_14)s, par_15=%(par_15)s, par_16=%(par_16)s, par_17=%(par_17)s, par_18=%(par_18)s 
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def update_one(cls, data):
        query = """UPDATE trackers
                SET course_name=%(course_name)s, holes_to_play=%(holes_to_play)s, course_city=%(course_city)s, course_state=%(course_state)s, user_id=%(user_id)s
                WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_1(cls, data):
        query = """UPDATE trackers SET hole_1=%(hole_1)s, par_1=%(par_1)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_2(cls, data):
        query = """UPDATE trackers SET hole_2=%(hole_2)s, par_2=%(par_2)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_3(cls, data):
        query = """UPDATE trackers SET hole_3=%(hole_3)s, par_3=%(par_3)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_4(cls, data):
        query = """UPDATE trackers SET hole_4=%(hole_4)s, par_4=%(par_4)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_5(cls, data):
        query = """UPDATE trackers SET hole_5=%(hole_5)s, par_5=%(par_5)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_6(cls, data):
        query = """UPDATE trackers SET hole_6=%(hole_6)s, par_6=%(par_6)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_7(cls, data):
        query = """UPDATE trackers SET hole_7=%(hole_7)s, par_7=%(par_7)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_8(cls, data):
        query = """UPDATE trackers SET hole_8=%(hole_8)s, par_8=%(par_8)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_9(cls, data):
        query = """UPDATE trackers SET hole_9=%(hole_9)s, par_9=%(par_9)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_10(cls, data):
        query = """UPDATE trackers SET hole_10=%(hole_10)s, par_10=%(par_10)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_11(cls, data):
        query = """UPDATE trackers SET hole_11=%(hole_11)s, par_11=%(par_11)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_12(cls, data):
        query = """UPDATE trackers SET hole_12=%(hole_12)s, par_12=%(par_12)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_13(cls, data):
        query = """UPDATE trackers SET hole_13=%(hole_13)s, par_13=%(par_13)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_14(cls, data):
        query = """UPDATE trackers SET hole_14=%(hole_14)s, par_14=%(par_14)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_15(cls, data):
        query = """UPDATE trackers SET hole_15=%(hole_15)s, par_15=%(par_15)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_16(cls, data):
        query = """UPDATE trackers SET hole_16=%(hole_16)s, par_16=%(par_16)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_17(cls, data):
        query = """UPDATE trackers SET hole_17=%(hole_17)s, par_17=%(par_17)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)

    @classmethod
    def updated_hole_18(cls, data):
        query = """UPDATE trackers SET hole_18=%(hole_18)s, par_18=%(par_18)s WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)
    #!!CRUD ---------------DELETE - DELETE

    @classmethod
    def delete_one(cls, data):
        query = """DELETE FROM trackers WHERE id = %(id)s;"""
        return connectToMySQL(DATABASE).query_db(query, data)


# Needed files always
# create/save - Create
# get_all - Read
# get_one - Read
# update_one - Update
# delete_one - Delete
