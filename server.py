from flask import Flask
from json import dumps
app = Flask(__name__)

course_list = [
    {"id": 1, "name": "COMP1511"},
    {"id": 2, "name": "COMP1521"},
    {"id": 3, "name": "COMP1531"},
]


@app.route("/", methods=['get'])
def home():
    return "Hello World!"


@app.route("/api/courses", methods=['get'])
def courses():
    return dumps(course_list)


if __name__ == "__main__":
    app.run()
