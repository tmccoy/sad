import os

appdir = os.path.dirname(os.path.abspath('index.py'))
htmldir= '/app/index/html/index'

class generate_index_page(object):
    def __init__(self):
        self.username = ""
        self.password = ""

    def show_login(self):
        with open(appdir+htmldir, 'r') as template:
            html = template.read()
            return html

