from flask import Flask, Response, request
from json import dumps

app = Flask(__name__)

courses = [
    {"id": 1, "name": "COMP1511"},
    {"id": 2, "name": "COMP1521"},
    {"id": 3, "name": "COMP1531"},
]


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
    return course


if __name__ == "__main__":
    app.run()
