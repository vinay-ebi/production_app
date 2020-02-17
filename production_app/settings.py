# Flask settings
FLASK_DEBUG = True  # Do not use debug mode in production

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False

# SQLAlchemy settings
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://anonymous@ensembldb.ensembl.org/ensembl_website_97'
SQLALCHEMY_TRACK_MODIFICATIONS = False

CELERY_BROKER_URL = "pyamqp://localhost//"
CELERY_RESULT_BACKEND = "rpc://"
