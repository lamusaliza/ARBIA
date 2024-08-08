from flask import Blueprint, render_template

adios_bp = Blueprint('adios', __name__)

@adios_bp.route('/adios')
def adios():
    return render_template('adios.html')
