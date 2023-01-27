from flask import jsonify

class SQLException(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class RequestParameterError(Exception):
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)

class Response:

    def classify_error(self, error):
        msg = str(error).split('/')
        print('valor s msg', msg)
        print(len(msg))
        code = 409
        if isinstance(error, RequestParameterError):
            response = {
                "code":  msg[0] if len(msg) > 1 else 409,
                "message": msg[1] if len(msg) == 2 else msg[0],
            }
        elif isinstance(error, SQLException):
            response = {
                "code":  msg[0] if len(msg) > 1 else 404,
                "message": msg[1] if len(msg) == 2 else msg[0],
            }
        
        return jsonify(response), code

    def bad_request_answer(self, message):
        code = 400
        response = {
            "code": 400,
            "message": str(message)
        }
        return jsonify(response), code