#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}

@app.get("/")
def home():
    return "Welcome to the Flask API!"

@app.get("/data")
def data():
    return jsonify(list(users.keys()))

@app.get("/status")
def status():
    return "OK"

@app.get("/users/<username>")
def get_user(username):
    u = users.get(username)
    if not u:
        return jsonify({"error": "User not found"}), 404
    return jsonify({"username": username, **u})

@app.post("/add_user")
def add_user():
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400
    data = request.get_json(silent=True) or {}
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400
    users[username] = {
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    return jsonify({
        "message": "User added",
        "user": {"username": username, **users[username]}
    }), 201

if __name__ == "__main__":
    app.run()