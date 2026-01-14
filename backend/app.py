from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()
        self.wfile.write(b"Hello from Effective Mobile!")

httpd = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
httpd.serve_forever()
