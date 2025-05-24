from flask import Blueprint

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return {"message": "Volunteer Tracking System is up and running!"}

