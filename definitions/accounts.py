schema = {
    'username': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 25,
        'required': True,
    },
    'password': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 25,
        'required': True,
    },
    'email': {
        'type': 'string',
        'minlength': 1,
        'maxlength': 40,
        'required': True,
    }
}

definition = {
    # most global settings can be overridden at resource level
    'resource_methods': ['GET', 'POST'],
    'schema': schema,
    'additional_lookup': {
        'url': 'regex("[\w]+")',
        'field': 'username'
    },
    # We choose to override global cache-control directives for this resource.
    'cache_control': 'max-age=10,must-revalidate',
    'cache_expires': 10,
}