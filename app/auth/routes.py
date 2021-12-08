from flask import Blueprint
from flask import render_template

auth = Blueprint('sign_in',__name__,template_folder='auth_templates')

@auth.route('/sign_in')
def sign_in():
    return render_template('auth.html')