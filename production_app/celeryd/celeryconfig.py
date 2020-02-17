broker='pyamqp://localhost//'
backend='rpc://'
task_default_exchange = 'vinay'
task_default_exchange_type = 'topic'
task_default_routing_key = 'vinay_key'
task_routes = ('production_app.celeryd.task_route.TaskRouter')

#{
#    'db_copy.api.rabbitmqp.endpoints.rabbitmq_db_copy.db_copy_submit': {
#        'exchange': 'service_exchange',
#        'exchange_type': 'topic',
#        'routing_key': 'metadata', 
#    },
#}
