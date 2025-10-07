from http.server import SimpleHTTPRequestHandler, HTTPServer
import os

PORT = 8000
WEB_DIR = os.path.join(os.path.dirname(__file__), 'test')
os.chdir(WEB_DIR)

class MyHandler(SimpleHTTPRequestHandler):
    def end_headers(self):
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == '__main__':
    print(f"✅ Server đang chạy tại http://localhost:{PORT}/login.html")
    httpd = HTTPServer(('', PORT), MyHandler)
    httpd.serve_forever()

