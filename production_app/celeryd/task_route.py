class TaskRouter:
    def route_for_task(self, task, *args, **kwargs):
        if ':' not in task:
            return {'queue': 'default'}

        namespace, _ = task.split(':')
        return {'queue': namespace}

#'exchange': 'service_exchange',
#        'exchange_type': 'topic',
#        'routing_key': 'metadata', 
