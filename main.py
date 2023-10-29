from flask import Flask
from app.processor import processor
from app.auth import auth

app = Flask(__name__)

@app.route("/")
def process():
    return processor.process()

@app.route("/admin")
def admin_process():
    user = auth.get_user()

    if user.can_process_admin():
        return processor.process()

    return "Denied"