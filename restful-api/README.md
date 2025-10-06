# RESTful API — Foundations v2.1 (Part 2)

Mini-project to learn how to **consume**, **build**, **secure**, and **document** REST APIs with Python.

## Prerequisites
- Python 3.8+
- `pip` and `venv` recommended
- CLI tools: `curl`, (optional) `jq`

## Quick setup
```bash
# from the restful-api/ folder
python3 -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -U pip
pip install Flask Flask-HTTPAuth Flask-JWT-Extended requests
```

## Expected structure
```
restful-api/
├── task_02_requests.py        # Consume an API in Python
├── task_03_http_server.py     # Mini API with http.server
├── task_04_flask.py           # Flask API (minimal CRUD)
├── task_05_basic_security.py  # Security: Basic Auth + JWT
└── README.md
```

## Tasks & usage

### 0) HTTP/HTTPS basics (theory)
- Understand methods (`GET/POST/PUT/PATCH/DELETE`), status codes (`200/201/404/401/403…`), headers, and the **HTTP vs HTTPS** difference (TLS encryption).

### 1) Consume an API with `curl`
Examples:
```bash
curl https://jsonplaceholder.typicode.com/posts        # GET
curl -I https://jsonplaceholder.typicode.com/posts     # Headers only
curl -X POST -H "Content-Type: application/json" \
  -d '{"title":"foo","body":"bar","userId":1}' \
  https://jsonplaceholder.typicode.com/posts
```

### 2) Consume & process an API with Python
Run (prints status + titles and creates `posts.csv`):
```bash
python3 -c "from task_02_requests import fetch_and_print_posts, fetch_and_save_posts; fetch_and_print_posts(); fetch_and_save_posts()"
```

### 3) Build a simple API with `http.server`
Start the server:
```bash
python3 task_03_http_server.py
# Default: http://localhost:8000
curl http://localhost:8000/           # 'Hello, this is a simple API!'
curl http://localhost:8000/data       # Sample JSON
curl http://localhost:8000/status     # OK
```

### 4) Simple API with **Flask**
> ⚠️ Do **not** commit test data in the in-memory `users` dictionary.

Run in dev:
```bash
flask --app task_04_flask.py run
# Default: http://127.0.0.1:5000
curl http://127.0.0.1:5000/           # Welcome
curl http://127.0.0.1:5000/status     # OK
curl http://127.0.0.1:5000/data       # list of usernames
curl -X POST -H "Content-Type: application/json" \
  -d '{"username":"alice","name":"Alice","age":25,"city":"SF"}' \
  http://127.0.0.1:5000/add_user
```

### 5) Security: Basic Auth & JWT (Flask)
- **Basic** (example): `/basic-protected`
```bash
# Without credentials -> 401
curl -i http://127.0.0.1:5000/basic-protected
# With credentials
curl -i -u user1:password http://127.0.0.1:5000/basic-protected
```
- **JWT**: `/login` → get a token, then access protected routes
```bash
TOKEN=$(curl -s -X POST -H "Content-Type: application/json" \
  -d '{"username":"user1","password":"password"}' \
  http://127.0.0.1:5000/login | jq -r .access_token)

curl -i -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/jwt-protected
curl -i -H "Authorization: Bearer $TOKEN" http://127.0.0.1:5000/admin-only   # requires admin role
```
> Important: all **authentication errors** must return **401**; role-based denials return **403**.

## Quick best practices
- Always return the **correct HTTP status** (`201` on creation, `404` if resource not found, `400` for invalid request).
- JSON responses with `Content-Type: application/json`.
- Store **hashed** passwords (never plain text).
- Use a strong `JWT_SECRET_KEY` in production.
- Handle errors cleanly (`try/except`, `resp.ok`, `timeout`).

## License
Educational project.