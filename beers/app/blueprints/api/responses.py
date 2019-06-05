from flask import jsonify


def resp_content_successfully(content):
    """Response 200"""
    response = jsonify(content)
    response.status_code = 200
    return response


def resp_created_successfully(resource):
    """Response 201"""
    response = jsonify({
        'message': f'{resource} created successfully!'
    })
    response.status_code = 201
    return response


def resp_updated_successfully(resource):
    """Response 201"""
    response = jsonify({
        'message': f'{resource} updated successfully!'
    })
    response.status_code = 201
    return response


def resp_deleted_successfully(resource):
    """Response 202"""
    response = jsonify({
        'message': f'{resource} deleted successfully!'
    })
    response.status_code = 202
    return response


def resp_empty_data_base():
    """Response 200"""
    response = jsonify({
        'message': 'Data base empty!'
    })
    response.status_code = 200
    return response
