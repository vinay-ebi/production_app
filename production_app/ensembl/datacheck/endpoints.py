import sys
import logging
from flask import jsonify
from flask_restplus import Resource
from flask import current_app as app
from celery.result import AsyncResult
from production_app import factory
#from production_app.ensembl_api.datacheck_api.datacheck.serializers import
#from production_app.ensembl_api.datacheck_api.datacheck.parsers import search_arguments, search_status
from production_app.ensembl.datacheck.restplus import api
from production_app.celeryd.tasks.celery_tasks import datacheck

log = logging.getLogger(__name__)

ns = api.namespace('api', description='datacheck process')

@ns.route('/')
@api.response(405, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'done.')
class Datacheck(Resource):

    def get(self):
        """
        Server status
        """
        ens={'a':'b', 'b':'c', 
                'flow':[],
                'status': True,
                'process': 'datacheck'
            }
        result =  datacheck.delay(ens)
        return {'title': 'Datacheck REST endpoints', 'uiversion': 2, 'status': True, 'result_id': result.id }, 200
