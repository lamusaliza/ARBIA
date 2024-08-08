from flask import Blueprint, render_template

hola_bp = Blueprint('hola', __name__)

@hola_bp.route('/hola')
def hola():
    return render_template('arbia.html')
