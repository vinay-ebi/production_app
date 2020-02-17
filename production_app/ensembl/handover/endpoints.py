import sys
import logging
from flask import jsonify
from flask_restplus import Resource
from flask import current_app as app
from celery.result import AsyncResult
from production_app import factory
#from production_app.ensembl.handover.serializers import
#from production_app.ensembl.handover.parsers import search_arguments, search_status
from production_app.ensembl.handover.restplus import api
from production_app.celeryd.tasks.celery_tasks import handover_celery

log = logging.getLogger(__name__)


ns = api.namespace('api', description='Handover process')

@ns.route('/')
@api.response(405, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'done.')
class Handover(Resource):
    def __init__(self, *args):
        self.pipeline_functions = [func for func in dir(Handover) if callable(getattr(Handover, func)) and not func.startswith("__")]
    def get(self):
        """
        Get DBcopy Server status
        """
        ens={'a':'b', 'b':'c', 
                'flow':['datacheck', 'dbcopy', 'metadata'],
                'status': True,
                'process': 'handover'
            }
        handover_celery.delay(ens)
        return {'title': 'Database copy REST endpoints', 'uiversion': 2, 'status': True} # 'result_state': result.state, 'result_id': result.id }, 200
