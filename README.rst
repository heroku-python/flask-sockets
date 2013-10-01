Flask-Sockets
=============

Elegant WebSockets for your Flask apps.


.. code-block:: python

    from flask import Flask
    from flask_sockets import Sockets

    app = Flask(__name__)
    sockets = Sockets(app)

    @sockets.route('/echo')
    def echo_socket(ws):
        while True:
            message = ws.receive()
            ws.send(message)

    @app.route('/')
    def hello():
        return 'Hello World!'

Serving WebSockets in Python were really difficult. Now they're not.


Deployment
----------

A custom Gunicorn worker is included to make deployment as friendly as possible::

    $ gunicorn -k flask_sockets.worker hello:app

Production services are provided by `gevent <http://www.gevent.org>`_
and `gevent-websocket <http://www.gelens.org/code/gevent-websocket/>`_.

Anything that inserts ``wsgi.websocket`` into the WSGI environ is
supported, but gevent-websocket is recommended.


WebSocket Interface
-------------------

The websocket interface that is passed into your routes is
`provided by gevent-websocket <https://bitbucket.org/Jeffrey/gevent-websocket/src/6da9851586843a655851b1b196c0d90599de091d/geventwebsocket/websocket.py?at=v0.3.6>`_.
The basic methods are fairly straitforward — 
``send``, ``receive``, ``send_fname``, and ``close``.

Hopefully, more documentation will be available soon.