from flask_restful import abort
from flask import jsonify


def error_does_not_exist(resource, msg):
    """Response 404 Not Found"""
    if not resource:
        abort(http_status_code=404, error=f"{msg} does not exist.")


def error_already_exists():
    """Response 400"""
    response = jsonify({
        'error': 'An ingredient with this name already exists.'
    })
    response.status_code = 400
    return response

# def error_not_inserted():
#     """Response 404"""
#     response = jsonify({
#         'error': 'No items inserted in the search!'
#     })
#     response.status_code = 404
#     return response
