#!/usr/bin/env python3
"""Simple HTTP server with proper Content-Disposition for file downloads."""
import http.server
import os

class DownloadHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add Content-Disposition for PDF files to force download with correct name
        if self.path.endswith('.pdf'):
            filename = os.path.basename(self.path)
            self.send_header('Content-Disposition', f'attachment; filename="{filename}"')
        super().end_headers()

if __name__ == '__main__':
    PORT = 8000
    print(f"Serving at http://localhost:{PORT}")
    with http.server.HTTPServer(("", PORT), DownloadHandler) as httpd:
        httpd.serve_forever()
