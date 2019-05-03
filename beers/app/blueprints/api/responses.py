from flask import jsonify


def resp_successfully(msg, status):
    """
    Response 201: for Created successfully!
    Response 200: for Updated successfully!
    Response 202: for Deleted successfully!
    """
    message = {
        201: {'message': f'{msg} created successfully!'},
        200: {'message': f'{msg} updated successfully!'},
        202: {'message': f'{msg} deleted successfully!'}
    }
    response = jsonify(
        message[status]
    )
    response.status_code = status
    return response


def resp_content_successfully(content):
    """Response 200"""
    response = jsonify(content)
    response.status_code = 200
    return response


def resp_empty_data_base():
    """Response 200"""
    response = jsonify({
        'message': 'Data base empty!'
    })
    response.status_code = 200
    return response
