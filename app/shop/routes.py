from flask import Blueprint
from flask import render_template

shop = Blueprint('shop',__name__,template_folder='shop_templates')

@shop.route('/shop')
def main_shop():
    return render_template('shop.html')

