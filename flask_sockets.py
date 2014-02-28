# -*- coding: utf-8 -*-

from functools import wraps

from flask import request


def log_request(self):
    log = self.server.log
    if log:
        if hasattr(log, 'info'):
            log.info(self.format_request() + '\n')
        else:
            log.write(self.format_request() + '\n')


# Monkeys are made for freedom.
try:
    import gevent
    from geventwebsocket.gunicorn.workers import GeventWebSocketWorker as Worker
except ImportError:
    pass

if 'gevent' in locals():
    # Freedom-Patch logger for Gunicorn.
    if hasattr(gevent, 'pywsgi'):
        gevent.pywsgi.WSGIHandler.log_request = log_request

class Sockets(object):

    def __init__(self, app=None):
        self.app = app

    def route(self, rule, **options):

        def decorator(f):
            @wraps(f)
            def inner(*args, **kwargs):
                return f(request.environ['wsgi.websocket'], *args, **kwargs)

            if self.app:
                endpoint = options.pop('endpoint', None)
                self.app.add_url_rule(rule, endpoint, inner, **options)
            return inner

        return decorator


# CLI sugar.
if 'Worker' in locals():
    worker = Worker
