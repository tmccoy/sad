from app.login_page import generate_login_page

def index(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    new_login = generate_login_page()
    return [ new_login.show_login() ]

def login(env, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return ["test"]
