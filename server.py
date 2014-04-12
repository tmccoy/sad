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

class AddPage(object):
    def __init__(self):
        self.appdir = os.path.dirname(os.path.abspath('server.py'))
        
    @cherrypy.expose
    def index(self, **kwargs):
        htmldir= '/html/add.html'
        with open(self.appdir+htmldir, 'r') as template:
            html = template.read()
            return html

class LoggedIn(object):
    def __init__(self):
        self.appdir = os.path.dirname(os.path.abspath('server.py'))
        
    @cherrypy.expose
    def index(self, **kwargs):
        htmldir= '/html/loggedin.html'
        with open(self.appdir+htmldir, 'r') as template:
            html = template.read()
            return html

class LoggedInMgr(object):
    def __init__(self):
        self.appdir = os.path.dirname(os.path.abspath('server.py'))
        
    @cherrypy.expose
    def index(self, **kwargs):
        htmldir= '/html/loggedinmgr.html'
        with open(self.appdir+htmldir, 'r') as template:
            html = template.read()
            return html

class ModifyEmp(object):
    def __init__(self):
        self.appdir = os.path.dirname(os.path.abspath('server.py'))
        
    @cherrypy.expose
    def index(self, **kwargs):
        htmldir= '/html/modifyemp.html'
        with open(self.appdir+htmldir, 'r') as template:
            html = template.read()
            return html

# Page Dispatches
root = LoginPage()
root.add = AddPage()
root.loggedin = LoggedIn()
root.loggedinmgr = LoggedInMgr()
root.modifyemp = ModifyEmp()


if __name__ == '__main__':

    # Configure the server object
    cherrypy.config.update({'server.socket_host': '0.0.0.0','server.socket_port': 8080})
    cherrypy.tree.mount(root, '/', config = 'app.conf')

    #Configure CSS handler 
    appdir = os.path.dirname(os.path.abspath('server.py'))
    cssdir = appdir + "/css"
    css_handler = cherrypy.tools.staticdir.handler(section="/", dir=cssdir)
    cherrypy.tree.mount(css_handler, '/css')

    # Start the server
    cherrypy.engine.start()
    cherrypy.engine.block()
   

    # For SSL Support
    # server.ssl_module            = 'pyopenssl'
    # server.ssl_certificate       = 'ssl/certificate.crt'
    # server.ssl_private_key       = 'ssl/private.key'
    # server.ssl_certificate_chain = 'ssl/bundle.crt'

