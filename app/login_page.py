class generate_login_page(object):
    def __init__(self):
        self.username = ""
        self.password = ""

    def show_login(self):
        with open('/var/opt/sad_app/app/login.html', 'r') as template:
            html = template.read()
            return html

