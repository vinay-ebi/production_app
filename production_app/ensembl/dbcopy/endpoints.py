import sys
import logging
from flask import jsonify
from flask_restplus import Resource
from flask import current_app as app
from celery.result import AsyncResult
from production_app import factory
#from production_app.ensembl.dbcopy.serializers import
#from production_app.ensembl.dbcopy.parsers import search_arguments, search_status
from production_app.ensembl.dbcopy.restplus import api
from production_app.celeryd.tasks.celery_tasks import dbcopy

log = logging.getLogger(__name__)


ns = api.namespace('api', description='DBcopy process')

@ns.route('/')
@api.response(405, 'Post not found.')
@api.response(400, 'Validation Error')
@api.response(200, 'done.')
class DBcopy(Resource):
    def get(self):
        """
        Get DBcopy Server status
        """
        ens={'a':'b', 'b':'c', 
                'flow':[],
                'status': True,
                'process': 'dbcopy'
            }
        result = dbcopy.delay(ens)
        return {'title': 'Database copy REST endpoints', 'uiversion': 2, 'status': True, 'result_id': result.id }, 200
