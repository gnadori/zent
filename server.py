import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8000
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)

def run():
    # Allow port reuse
    socketserver.TCPServer.allow_reuse_address = True
    try:
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            url = f"http://localhost:{PORT}"
            print("=" * 60)
            print(f" Zent Presenter fut a következő címen: {url}")
            print(" Kilépéshez nyomj Ctrl+C billentyűkombinációt.")
            print("=" * 60)
            webbrowser.open(url)
            httpd.serve_forever()
    except OSError as e:
        print(f"A {PORT}-es port foglalt, vagy más hiba lépett fel: {e}")
        # Try alternate port 8080
        alt_port = 8080
        with socketserver.TCPServer(("", alt_port), Handler) as httpd:
            url = f"http://localhost:{alt_port}"
            print(f"Indítás a tartalék porton: {url}")
            webbrowser.open(url)
            httpd.serve_forever()

if __name__ == '__main__':
    run()
