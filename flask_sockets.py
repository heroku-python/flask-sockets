# -*- coding: utf-8 -*-

try:
    import gevent
    from geventwebsocket.gunicorn.workers import GeventWebSocketWorker as Worker
except ImportError:
    # Don't fail, in case someone is using somethign else that provides
    # "wsgi.websocket".
    pass


def log_request(self):
    log = self.server.log
    if log:
        write = log.info if hasattr(log, "info") else log.write
        write(self.format_request() + '\n')


class SocketMiddleware(object):

    def __init__(self, wsgi_app, socket):
        self.ws = socket
        self.app = wsgi_app

    def __call__(self, environ, start_response):
        path = environ["PATH_INFO"]

        if path in self.ws.url_map:
            handler = self.ws.url_map[path]
            environment = environ["wsgi.websocket"]

            handler(environment)
        else:
            return self.app(environ, start_response)


class Sockets(object):

    def __init__(self, app=None, patch=True):
        self.url_map = {}
        if app:
            self.init_app(app, patch=patch)

    def init_app(self, app, patch=True):
        if patch:
            # Monkey-patch log_request handler for Gevent/Gunicorn compatability.
            if 'gevent' in locals():
                if hasattr(gevent, 'pywsgi'):
                    gevent.pywsgi.WSGIHandler.log_request = log_request

        app.wsgi_app = SocketMiddleware(app.wsgi_app, self)

    def route(self, rule, **options):

        def decorator(f):
            endpoint = options.pop('endpoint', None)
            self.add_url_rule(rule, endpoint, f, **options)
            return f
        return decorator

    def add_url_rule(self, rule, _, f, **options):
        self.url_map[rule] = f

# CLI sugar.
if 'Worker' in locals():
    worker = Worker