from flask import Blueprint, render_template

admin = Blueprint('admin', __name__, url_prefix='/admin', template_folder='templates')

@admin.route('/')
def index():
	return render_template('index.html')
