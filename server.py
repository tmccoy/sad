# Import CherryPy
import cherrypy
import os

class LoginPage(object):
    def __init__(self):
        self.appdir = os.path.dirname(os.path.abspath('server.py'))
        
    @cherrypy.expose
    def index(self, **kwargs):
        htmldir= '/html/index.html'
        with open(self.appdir+htmldir, 'r') as template:
            html = template.read()
            return html

appdir = os.path.dirname(os.path.abspath('index.py'))
cssdir = appdir + "/css"

root = LoginPage()
if __name__ == '__main__':

    # Configure the server object
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080,})
    cherrypy.tree.mount(root, '/', config = 'app.conf')

    #Configure CSS handler 
    css_handler = cherrypy.tools.staticdir.handler(section="/", dir=cssdir)
    cherrypy.tree.mount(css_handler, '/css')

    # Start the server
    cherrypy.engine.start()
   

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

