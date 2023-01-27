import os
import json
import jsonref

from os.path import dirname
from jsonschema import validate


from utils.custom_errors import RequestParameterError

class Validator:

    @classmethod
    def read_json_file(cls, file_path):
        try:
            json_content_file = open(f"{os.getcwd()}/schemas/{file_path}", 'r')
        except IOError as error:
            print(error)

        else:
            try:
                base_path = dirname(file_path)
                base_uri = 'file://{}/'.format(base_path)
                json_schema = jsonref.load(json_content_file, base_uri=base_uri, jsonschema=True)
            except (ValueError, KeyError) as error:
                print(file_path)
                print(error)

            json_content_file.close()

        return json_schema

    @classmethod
    def validator(cls, data, schema):
        try:
            req_schema = cls.read_json_file(schema)
            validate(instance=data, schema=req_schema)
        except Exception as ex:
            print(f"Error: {ex}")
            raise RequestParameterError('Request invalido')