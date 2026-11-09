"""Optional static server for the Re-enrollment prototype.

Python 3 standard library only. Serves this repository root with the same
layout GitHub Pages uses for the `main` branch (root directory, no rewrites).

    python3 serve.py
    open http://localhost:8799/

`index.html` opens `project/Reenroll.dc.html`. Any other static server of this
folder does the same thing, for example `python3 -m http.server 8799`.
Another port: PORT=8800 python3 serve.py
"""
import http.server
import mimetypes
import os

ROOT = os.path.dirname(os.path.abspath(__file__))
PORT = int(os.environ.get("PORT", "8799"))
mimetypes.add_type("font/ttf", ".ttf")
mimetypes.add_type("font/otf", ".otf")
mimetypes.add_type("image/svg+xml", ".svg")
mimetypes.add_type("text/javascript", ".js")


class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=ROOT, **kwargs)

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, *args):
        pass


if __name__ == "__main__":
    print("Re-enrollment prototype: http://localhost:%d/  (Ctrl+C to stop)" % PORT)
    http.server.ThreadingHTTPServer(("127.0.0.1", PORT), Handler).serve_forever()
