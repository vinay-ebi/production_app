import logging.config
import click
from flask import Flask, Blueprint
#from ensembl_prodinf import HiveInstance
from production_app import settings
#from production_app.ensembl.datacheck.endpoints import ns
#from production_app.ensembl.datacheck.restplus import api 
from production_app.database import db
from production_app import factory

def configure_app(flask_app):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = settings.SQLALCHEMY_DATABASE_URI
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = settings.RESTPLUS_ERROR_404_HELP

def initialize_blueprint(flask_app, modules=[]):
    for module in modules:
        module_name = 'production_app.ensembl.' + module
        blueprint = Blueprint('ensembl/' + module, __name__, url_prefix='/ensembl/' + module)
        module_inst =  __import__(module_name, fromlist = ["api", "ns"])
        module_inst.api.init_app(blueprint)
        module_inst.api.add_namespace(module_inst.ns)
        flask_app.register_blueprint(blueprint)

def initialize_app(flask_app):
    configure_app(flask_app)
    db.init_app(flask_app)


def make_celery(app, factory):
    initialize_blueprint(app, ['handover', 'datacheck', 'dbcopy', 'metadata'])
    initialize_app(app)
    factory.make_celery(app)
    return factory.celery



app = Flask(__name__)
#make celery
celery = make_celery(app, factory)
logging.basicConfig(level=logging.INFO)

