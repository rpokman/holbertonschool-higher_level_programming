#!/usr/bin/python3
import csv
import requests

API = "https://jsonplaceholder.typicode.com/posts"

def fetch_and_print_posts():
    resp = requests.get(API)
    print(f"Status Code: {resp.status_code}")
    if resp.status_code == 200:
        for post in resp.json():
            print(post.get("title"))

def fetch_and_save_posts():
    resp = requests.get(API)
    if resp.status_code == 200:
        rows = [
            {"id": p.get("id"), "title": p.get("title"), "body": p.get("body")}
            for p in resp.json()
        ]
        with open("posts.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=["id", "title", "body"])
            writer.writeheader()
            writer.writerows(rows)
