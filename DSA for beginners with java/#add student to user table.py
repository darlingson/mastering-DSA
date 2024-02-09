#add student to user table
#add student to user_config
#add student to student table
#assign student to course
users = {
    1: {
        "user_id": "user_kamzimbi_student_1",
        "student_id": "kamzimbi_student_3",
        "f_name": "first name",
        "l_name": "surname",
        "sex": "M",
        "dob": "2000-01-01",
        "phone": "phone",
        "email": "email",
        "password": "student_3",
        "role": "student",
        "locale": "MW-en",
        "school_id": "",
        "class_id":"",
        "location_id":"",
        "special_needs":"non",
        "courses":["course_1","course_2"],
    },
        2: {
        "user_id": "user_kamzimbi_student_1",
        "student_id": "kamzimbi_student_3",
        "f_name": "first name",
        "l_name": "surname",
        "sex": "M",
        "dob": "2000-01-01",
        "phone": "phone",
        "email": "email",
        "password": "student_3",
        "role": "student",
        "locale": "MW-en",
        "school_id": "",
        "class_id":"",
        "location_id":"",
        "special_needs":"non",
        "courses":["course_1","course_2"],
    }
}

import mysql.connector

db_connection = mysql.connector.connect(
    host="your_mysql_host",
    user="your_mysql_user",
    password="your_mysql_password",
    database="your_database_name"
)

cursor = db_connection.cursor()

def insert_user(email, password, user_id, f_name, l_name, sex, phone, dob, role):
    query = """
        INSERT INTO your_table_name
        (email, password, user_id, f_name, l_name, sex, phone, dob, role)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
    """

    values = (email, password, user_id, f_name, l_name, sex, phone, dob, role)
    cursor.execute(query, values)
    db_connection.commit()
def insert_user_config(user_id, locale,):
    query = """
        INSERT INTO your_table_name
        (user_id, locale)
        VALUES (%s, %s)
    """

    values = (user_id, locale)
    cursor.execute(query, values)
    db_connection.commit()

def insert_student(student_id, user_id, school_id, class_id, location_id, special_needs):
    query = """
        INSERT INTO your_table_name
        (student_id, user_id, school_id, class_id, location_id, special_needs)
        VALUES (%s, %s, %s, %s, %s, %s)
    """

    values = (student_id, user_id, school_id, class_id, location_id, special_needs)
    cursor.execute(query, values)
    db_connection.commit()
def insert_student_course(student_id, course_id):
    query = """
        INSERT INTO your_table_name
        (student_id, course_id)
        VALUES (%s, %s)
    """

    values = (student_id, course_id)
    cursor.execute(query, values)
    db_connection.commit()

for user_data in users.values():
    insert_user(
        user_data.get("email", ""),
        user_data.get("password", ""),
        user_data.get("user_id", ""),
        user_data.get("f_name", ""),
        user_data.get("l_name", ""),
        user_data.get("sex", ""),
        user_data.get("phone", ""),
        user_data.get("dob", None),
        user_data.get("role", "")
    )

cursor.close()
db_connection.close()
