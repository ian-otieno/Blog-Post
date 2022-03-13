from flask import Blueprint
auth =Blueprint('auth', __name__)
from flask import Blueprint
main = Blueprint('main', __name__)
from . import views