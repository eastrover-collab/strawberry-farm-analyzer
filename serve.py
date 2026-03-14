import http.server
import functools

class UTF8Handler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        if self.path.endswith('.html'):
            self.send_header('Content-Type', 'text/html; charset=utf-8')
        super().end_headers()

if __name__ == '__main__':
    http.server.test(HandlerClass=functools.partial(UTF8Handler, directory='.'), port=8000)
