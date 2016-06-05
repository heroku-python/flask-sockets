Flask-Sockets
=============

Elegant WebSockets for your Flask apps.

.. image:: http://farm4.staticflickr.com/3689/9755961864_577e32a106_c.jpg


Simple usage of ``route`` decorator:

.. code-block:: python

    from flask import Flask
    from flask_sockets import Sockets


    app = Flask(__name__)
    sockets = Sockets(app)


    @sockets.route('/echo')
    def echo_socket(ws):
        while not ws.closed:
            message = ws.receive()
            ws.send(message)


    @app.route('/')
    def hello():
        return 'Hello World!'


    if __name__ == "__main__":
        from gevent import pywsgi
        from geventwebsocket.handler import WebSocketHandler
        server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
        server.serve_forever()


Usage of `Flask blueprints`_:

.. code-block:: python

    from flask import Flask, Blueprint
    from flask_sockets import Sockets


    html = Blueprint(r'html', __name__)
    ws = Blueprint(r'ws', __name__)


    @html.route('/')
    def hello():
        return 'Hello World!'

    @ws.route('/echo')
    def echo_socket(socket):
        while not socket.closed:
            message = socket.receive()
            socket.send(message)


    app = Flask(__name__)
    sockets = Sockets(app)

    app.register_blueprint(html, url_prefix=r'/')
    sockets.register_blueprint(ws, url_prefix=r'/')


    if __name__ == "__main__":
        from gevent import pywsgi
        from geventwebsocket.handler import WebSocketHandler
        server = pywsgi.WSGIServer(('', 5000), app, handler_class=WebSocketHandler)
        server.serve_forever()


Serving WebSockets in Python was really difficult. Now it's not.


Installation
------------

To install Flask-Sockets, simply::

    $ pip install Flask-Sockets


Deployment
----------

A custom Gunicorn worker is included to make deployment as friendly as possible::

    $ gunicorn -k flask_sockets.worker hello:app

Production services are provided by `gevent <http://www.gevent.org>`_
and `gevent-websocket <https://bitbucket.org/noppo/gevent-websocket>`_.

The given example can run standalone as main.

Anything that inserts ``wsgi.websocket`` into the WSGI environ is
supported, but gevent-websocket is recommended.


Development / Testing
---------------------

Because the Werkzeug development server cannot provide the WSGI environ with
a websocket interface, it is not possible to run a Flask app using the standard
``app.run()``.

If you try to, Flask will still try to serve on all the specified routes, and
throw a ``KeyError`` whenever a client tries to connect to a websocket route.

Instead, just use the included gunicorn worker (explained above), or anything that
can insert ``wsgi.websocket`` into the WSGI environ.



WebSocket Interface
-------------------

The websocket interface that is passed into your routes is
`provided by gevent-websocket <https://bitbucket.org/noppo/gevent-websocket>`_.
The basic methods are fairly straightforward — 
``send``, ``receive``, ``send_frame``, and ``close``.


Release History
---------------

v0.2.1
~~~~~~

- Add support of `Flask blueprints`_.


v0.2.0
~~~~~~

- Add request context into the socket handler.
- Fallback to Flask logic if websocket environment is not available.
- Use Flask routing to allow for variables in URL

v0.1.0
~~~~~~

- Initial release.


.. _Flask blueprints: http://flask.pocoo.org/docs/latest/blueprints/



