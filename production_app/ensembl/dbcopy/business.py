import json
from flask import current_app as app
from production_app.database import db
#from production_app.database.models 
from celery.result import AsyncResult
import sys


def db_copy_run():
    pass
