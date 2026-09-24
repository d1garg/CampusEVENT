from flask import Flask, jsonify, render_template

app = Flask(__name__)

# True = API working
# False = API DOWN (for testing)
API_ON = True

notices = [
    {
        "id": 1,
        "title": "Mid Semester Examination",
        "date": "2026-10-05"
    },
    {
        "id": 2,
        "title": "College Holiday",
        "date": "2026-10-02"
    }
]

events = [
    {
        "id": 1,
        "name": "Tech Fest",
        "date": "2026-10-15"
    },
    {
        "id": 2,
        "name": "Coding Competition",
        "date": "2026-10-20"
    }
]


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/notices")
def get_notices():

    if not API_ON:
        return jsonify({
            "status": "error",
            "message": "Campus API is currently unavailable"
        }), 503

    return jsonify({
        "status": "success",
        "data": notices
    })


@app.route("/api/events")
def get_events():

    if not API_ON:
        return jsonify({
            "status": "error",
            "message": "Campus API is currently unavailable"
        }), 503

    return jsonify({
        "status": "success",
        "data": events
    })


if __name__ == "__main__":
    app.run(debug=True)
