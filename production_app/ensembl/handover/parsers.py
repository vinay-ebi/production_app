from flask_restplus import reqparse

search_arguments = reqparse.RequestParser()
search_arguments.add_argument('', type=str, required=True,  help='')
search_arguments.add_argument('', type=str,  help='')

