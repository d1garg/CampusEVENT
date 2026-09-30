from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# =========================
# API STATUS
# =========================

API_ON = True


# =========================
# CAMPUS DATA
# =========================

notices = [
    {
        "id": 1,
        "title": "Mid Semester Examination Schedule Released",
        "date": "2026-10-05",
        "category": "Examination"
    },
    {
        "id": 2,
        "title": "College will remain closed on Gandhi Jayanti",
        "date": "2026-10-02",
        "category": "Holiday"
    },
    {
        "id": 3,
        "title": "Registration Open for Technical Workshop",
        "date": "2026-09-28",
        "category": "Workshop"
    }
]

events = [
    {
        "id": 1,
        "name": "Tech Fest 2026",
        "date": "2026-10-15",
        "category": "Technology"
    },
    {
        "id": 2,
        "name": "Inter College Coding Competition",
        "date": "2026-10-20",
        "category": "Competition"
    },
    {
        "id": 3,
        "name": "AI & Machine Learning Workshop",
        "date": "2026-10-08",
        "category": "Workshop"
    }
]


# =========================
# HOME / API STATUS
# =========================

@app.route("/")
def home():
    return jsonify({
        "status": "success",
        "message": "Campus Information API is running!",
        "api": "online" if API_ON else "offline"
    })


# =========================
# NOTICES API
# =========================

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


# =========================
# EVENTS API
# =========================

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


# =========================
# START SERVER
# =========================

if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
