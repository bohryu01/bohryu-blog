import http.server
import socketserver
PORT = 1313
Handler = http.server.SimpleHTTPRequestHandler
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("?????http://localhost:1313")
    httpd.serve_forever()