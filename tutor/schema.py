from jsonschema import validate
from jsonschema.exceptions import ValidationError, SchemaError

TutorModel = {
    'type': 'object',
    'properties': {
        "firstname": {
            'type': 'string'
        },
        "lastname": {
            'type': 'string'
        },
        'email': {
            'type': 'string',
            'format': 'email'
        },
        'password': {
            'type': 'string'
        }
    },
    'required': ['firstname', 'lastname', 'email'],
    'additionalProperties': False
}

CourseModel = {
    'type': 'object',
    'properties': {
        "title": {
            'type': 'string'
        },
        "description": {
            'type': 'string'
        },
        "category": {
            'type': 'string'
        },
        "price": {
            'type': 'number'
        },
        "tags": {
            'type': 'string'
        }
    },
    'required': ['title', 'description', 'category', 'price'],
    'additionalProperties': False
}


def validate_tutor(data):
    try:
        validate(data, TutorModel)
        return {'msg': 'success'}
    except SchemaError as e:
        return {'msg': 'error', 'error': e.message}
    except ValidationError as e:
        return {'msg': 'error', 'error': e.message}


def validate_course(data):
    try:
        validate(data, CourseModel)
        return {'msg': 'success'}
    except SchemaError as e:
        return {'msg': 'error', 'error': e.message}
    except ValidationError as e:
        return {'msg': 'error', 'error': e.message}
