import pymysql
from flask import Flask, Response, request
from json import dumps
from courses import courses
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


def db_connection():
    conn = None
    try:
        conn = pymysql.connect(
            host='sql6.freesqldatabase.com',
            database='sql6432733',
            user='sql6432733',
            password='MTTiE8MquJ',
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )
    except pymysql.error as e:
        print(e)
    return conn


@app.route("/", methods=['GET'])
def home():
    return "Hello World!"


@app.route("/api/courses", methods=['GET'])
def get_courses():
    conn = db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    courses = [
        dict(id=row['id'], name=row['name'], likes=row['likes'])
        for row in cursor.fetchall()
    ]
    if courses is not None:
        return dumps(courses)


@app.route("/api/courses", methods=["POST"])
def add_course():
    conn = db_connection()
    cursor = conn.cursor()
    new_name = request.form["name"]
    new_likes = request.form["likes"]
    sql = """INSERT INTO course (name, likes)
            VALUES (%s, %s)"""
    cursor = cursor.execute(sql, (new_name, new_likes))
    conn.commit()
    return dumps("Hi")


@app.route("/api/courses/likes/<int:id>", methods=["PUT"])
def like_course(id):
    conn = db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    courses = [
        dict(id=row['id'], name=row['name'], likes=row['likes'])
        for row in cursor.fetchall()
    ]

    cursor = conn.cursor()
    new = courses[id - 1]["likes"] + 1
    sql = """UPDATE course
            SET likes=%s
            WHERE id=%s """

    cursor.execute(sql, (str(new), str(id)))
    conn.commit()
    return dumps(new)


@app.route("/api/courses/likes/<int:id>", methods=["DELETE"])
def unlike_course(id):
    conn = db_connection()

    cursor = conn.cursor()
    cursor.execute("SELECT * FROM course")
    courses = [
        dict(id=row['id'], name=row['name'], likes=row['likes'])
        for row in cursor.fetchall()
    ]

    cursor = conn.cursor()
    new = courses[id - 1]["likes"] - 1
    sql = """UPDATE course
            SET likes=%s
            WHERE id=%s """

    cursor.execute(sql, (str(new), str(id)))
    conn.commit()
    return dumps(new)


@app.route("/api/courses/<id>", methods=["GET"])
def get_course(id):
    if len(courses) < int(id):
        return Response(
            "The course ID was not found.",
            status=400,
        )
    course = courses[int(id)]
    return dumps(course)


@app.route("/api/courses/<id>", methods=["DELETE"])
def delete_course(id):
    if len(courses) < int(id):
        return Response(
            "The course ID was not found.",
            status=400,
        )
    course = courses.pop(int(id))
    return dumps(course)


if __name__ == "__main__":
    app.run(port=8000)
