class generate_index_page(object):
    def __init__(self):
        self.username = ""
        self.password = ""

    def show_login(self):
        with open('/home/tyler/sad/app/index.html', 'r') as template:
            html = template.read()
            return html

