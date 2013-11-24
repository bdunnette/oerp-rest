from flask import render_template
from oerp_rest import oerp_rest

@oerp_rest.route('/')
def index():
    return render_template('index.html')
