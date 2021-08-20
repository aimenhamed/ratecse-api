from flask import Flask, Response, request
from json import dumps
from courses import courses
from flask_cors import CORS

app = Flask(__name__)
CORS(app)


@app.route("/", methods=['GET'])
def home():
    return "Hello World!"


@app.route("/api/courses", methods=['GET'])
def get_courses():
    return dumps(courses)


@app.route("/api/courses", methods=["POST"])
def add_course():
    req = request.get_json()
    name = req["name"]
    if len(name) != 8:
        return Response(
            "Name is required and should be 8 chars long, e.g. COMP1511",
            status=400,
        )
    course = {
        "id": len(courses) + 1,
        "name": name,
    }

    courses.append(course)
    return dumps(course)


@app.route("/api/courses/<id>", methods=["GET"])
def get_course(id):
    if len(courses) < int(id):
        return Response(
            "The course ID was not found."
        )
    course = courses[int(id) - 1]
    return dumps(course)


@app.route("/api/courses/<id>", methods=["DELETE"])
def delete_course(id):
    if len(courses) < int(id):
        return Response(
            "The course ID was not found."
        )
    course = courses.pop(int(id) - 1)
    return dumps(course)


if __name__ == "__main__":
    app.run()
