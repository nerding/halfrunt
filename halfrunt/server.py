from flask import Flask
from halfrunt.admin import admin

app = Flask(__name__)
app.register_blueprint(admin.admin)