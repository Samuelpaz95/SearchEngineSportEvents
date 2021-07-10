from flask import Blueprint
from flask import render_template, request

view_pages = Blueprint('view_pages', __name__)

from .index import *