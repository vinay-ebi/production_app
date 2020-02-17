from celery import Celery
from production_app.celeryd.factory_celery import Factory
from production_app import  settings

factory = Factory()
factory.set_celery()
factory.celery.conf.update(
        CELERY_BROKER_URL=settings.CELERY_BROKER_URL, 
        CELERY_RESULT_BACKEND=settings.CELERY_RESULT_BACKEND,
        FLASK_DEBUG = True,  # Do not use debug mode in production
        # Flask-Restplus settings
        RESTPLUS_SWAGGER_UI_DOC_EXPANSION = settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION,
        RESTPLUS_VALIDATE = settings.RESTPLUS_VALIDATE,
        RESTPLUS_MASK_SWAGGER = settings.RESTPLUS_MASK_SWAGGER,
        RESTPLUS_ERROR_404_HELP = settings.RESTPLUS_ERROR_404_HELP,
        # SQLAlchemy settings
        SQLALCHEMY_DATABASE_URI = settings.SQLALCHEMY_DATABASE_URI,
        SQLALCHEMY_TRACK_MODIFICATIONS = settings.SQLALCHEMY_TRACK_MODIFICATIONS
        )

__all__ = ['Factory']
