import sys
from production_app import factory
from celery.result import AsyncResult

celery = factory.celery

@celery.task(bind=True, name='datacheck:production_app.datacheck')
def datacheck(self, payload):
    #do some stuff
    payload['process']='datacheck'
    payload['status']= True
    handover_celery.delay(payload)
    return {'datacheck': 'done4'}


@celery.task(bind=True, name='dbcopy:production_app.dbcopy')
def dbcopy(self, payload):
    payload['process']='dbcopy'
    payload['status']= True
    handover_celery.delay(payload)
    return {'dbcopy': 'done4'}

@celery.task(bind=True, name='metadata:production_app.metadata')
def metadata(self, payload):

    payload['process']='metadata'
    payload['status']= True
    handover_celery.delay(payload)
    return {'metadata': 'done4'}

@celery.task(bind=True, name='handover:production_app.handover')
def handover_celery(self, payload):
    #functions = [ for func in dir(sys.modules[__name__]) if  callable(getattr(sys.modules[__name__], func)) and not func.startswith("__")]
    if not payload['status']:
        return {'failed to run': payload['process']}
    if not any(payload['flow']):
        return {'end': 'end'}

    next_step = payload['flow'].pop(0)
    if not callable(getattr(sys.modules[__name__], next_step)):
        return {'nostep': next_step}

    getattr(sys.modules[__name__], next_step).delay(payload)
    print(next_step)
    return {'done': 'handover2'}


