Flask-Sockets
=============

Elegant WebSockets for your Flask apps.

.. image:: http://farm4.staticflickr.com/3689/9755961864_577e32a106_c.jpg

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
and `gevent-websocket <http://www.gelens.org/code/gevent-websocket/>`_.


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
The basic methods are fairly straitforward — 
``send``, ``receive``, ``send_frame``, and ``close``.
