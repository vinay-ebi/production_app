from celery import Celery
import production_app.celeryd.celeryconfig as celeryconfig

class Factory():
    """celery Instance for API."""
    def set_celery(self):
        self.celery = Celery() #include=['production_app.celeryd.tasks.celery_tasks'])
        self.celery.config_from_object(celeryconfig)
        return self.celery

    def make_celery(self, app):
        self.celery = Celery() #include=['production_app.celeryd.tasks.celery_tasks'])
        self.celery.config_from_object(celeryconfig)
        class ContextTask(self.celery.Task):
            def __call__(self, *args, **kwargs):
                with app.app_context():
                    return self.run(*args, **kwargs)
        self.celery.Task = ContextTask
        return self.celery    
