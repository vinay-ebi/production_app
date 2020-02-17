import sys
import logging
from flask import jsonify
from flask_restplus import Resource
from flask import current_app as app
from celery.result import AsyncResult
from production_app import factory
#from production_app.ensembl.metadata.serializers import
#from production_app.ensembl.metadata.parsers import search_arguments, search_status
from production_app.ensembl.metadata.restplus import api
from production_app.celeryd.tasks.celery_tasks import metadata

log = logging.getLogger(__name__)


ns = api.namespace('api', description='Metadata process')

@ns.route('/')
@api.response(405, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'done.')
class Metadata(Resource):
    def get(self):
        """
        Get Metadata Server status
        """
        ens={'a':'b', 'b':'c', 
                'flow':[],
                'status': True,
                'process': 'metadata'
            }
        result = metadata.delay(ens)
        return {'title': 'Metadata REST endpoints', 'uiversion': 2, 'status': True, 'result_id': result.id }, 200
