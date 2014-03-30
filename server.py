# Import your application as:
from wsgi import *

# Import CherryPy
import cherrypy

if __name__ == '__main__':

    # Mount the application
    cherrypy.tree.graft(index, "/")
    cherrypy.tree.graft(login, "/login")
<<<<<<< HEAD
    cherrypy.tree.graft(lst, "/list")
    cherrypy.tree.graft(take, "/take")
    cherrypy.tree.graft(view, "/view")
    cherrypy.tree.graft(modify, "/modify")
=======
>>>>>>> a57c26c3ddd48eab9398844e481f1751b210806f
    # Unsubscribe the default server
    cherrypy.server.unsubscribe()

    # Instantiate a new server object
    server = cherrypy._cpserver.Server()

    # Configure the server object
    server.socket_host = "0.0.0.0"
    server.socket_port = 8080
    server.thread_pool = 30

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

    # Subscribe this server
    server.subscribe()

    cherrypy.engine.start()
    cherrypy.engine.block()
