from http.server import BaseHTTPRequestHandler, HTTPServer
import json

class H(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path=="/":
            self.send_response(200); self.send_header("Content-Type","text/plain; charset=utf-8"); self.end_headers(); self.wfile.write(b"Hello, this is a simple API!")
        elif self.path=="/data":
            b=json.dumps({"name":"John","age":30,"city":"New York"}).encode()
            self.send_response(200); self.send_header("Content-Type","application/json; charset=utf-8"); self.end_headers(); self.wfile.write(b)
        elif self.path=="/status":
            self.send_response(200); self.send_header("Content-Type","text/plain; charset=utf-8"); self.end_headers(); self.wfile.write(b"OK")
        else:
            b=json.dumps({"error":"Endpoint not found"}).encode()
            self.send_response(404); self.send_header("Content-Type","application/json; charset=utf-8"); self.end_headers(); self.wfile.write(b)

if __name__=="__main__":
    HTTPServer(("127.0.0.1",8000),H).serve_forever()
