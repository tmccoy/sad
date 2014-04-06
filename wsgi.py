from app.index.index import generate_index_page

def index(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    new_login = generate_index_page()
    return  [ new_login.show_login() ]

def login(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["after login page"]

def lst(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["list shift page"]

def take(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["Take shift page"]

def view(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["view shift page"]

def modify(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["modify page"]
    return ["test"]
