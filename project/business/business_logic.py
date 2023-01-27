from flask import jsonify

from random import randint

from utils.custom_errors import Response, RequestParameterError
from utils.validator import Validator
from config.sql import SQL

from dao.catalog import Catalog
from dao.student import Student

response = Response()

STATUS_REGISTER_STUDENT = 1
STATUS_UPDATE_REGISTER = 2
STATUS_ACCEPTED_STUDENT = 3
STATUS_REJECT_REQUEST_STUDENT = 4
STATUS_DELETE_STUDENT = 5

STATUS_ACTIVO = 1

def get_catalog(event = None):
    try:
        print('catalog', event)
        result = Catalog.retrivied_catalog_by_name(
            name_catalog = event.get('name_catalog'), 
            status = STATUS_ACTIVO)
        if result:
            return jsonify({"data": result})
        else:
            return response.bad_request_answer('no hay datos')
    except Exception as ex:
        print(ex)
        return response.classify_error(ex)

def register_student(event = None):
    try:
        body = event
        if not body:
            raise RequestParameterError('Body vacio')

        Validator.validator(body,"register_student.json")

        identicaion = Student.retrivied_by_identification(body.get('identification'), (STATUS_REGISTER_STUDENT,STATUS_UPDATE_REGISTER,STATUS_ACCEPTED_STUDENT,STATUS_REJECT_REQUEST_STUDENT))
        if identicaion:
            raise RequestParameterError('0001/identification already exists')

        magic_affinity = Catalog.retrivied_catalog_by_id(body.get('magic_affinity'), 'magic_affinity')
        if not magic_affinity:
            raise RequestParameterError('0002/magic affinity does not exist')

        data_student = dict(
            name           = body.get('name'),
            lastname       = body.get('lastname'),
            identification = body.get('identification'),
            age            = body.get('age'),
            magic_affinity = body.get('magic_affinity'),
            status         = STATUS_REGISTER_STUDENT
        )

        data_student = Student.save_student(data_student)
        SQL.commit()
        return jsonify({
            "message": "success",
            "id": data_student.get('id')
            })
    except Exception as ex:
        return response.classify_error(ex)

def update_register_student(event = None):
    try:
        body = event
        if not body:
            raise RequestParameterError('Body vacio')

        Validator.validator(body,"update_register_student.json")

        identicaion = Student.retrivied_by_identification(body.get('identification'), (STATUS_REGISTER_STUDENT,STATUS_UPDATE_REGISTER,STATUS_ACCEPTED_STUDENT,STATUS_REJECT_REQUEST_STUDENT))
        if identicaion and identicaion.get('id') != body.get('id'):
                raise RequestParameterError('0001/identification already exists')

        magic_affinity = Catalog.retrivied_catalog_by_id(body.get('magic_affinity'), 'magic_affinity')
        if not magic_affinity:
            raise RequestParameterError('0002/magic affinity does not exist')

        data_student = dict(
            name           = body.get('name'),
            lastname       = body.get('lastname'),
            identification = body.get('identification'),
            age            = body.get('age'),
            magic_affinity = body.get('magic_affinity'),
            status         = STATUS_UPDATE_REGISTER,
            id             = body.get('id')
        )
        print(data_student)
        Student.update_student(data_student)
        SQL.commit()
        return jsonify({
            "message": "update",
            "id": data_student.get('id')
            })
    except Exception as ex:
        return response.classify_error(ex)

def accept_student_request(event = None):
    try:
        body = event
        if not body:
            raise RequestParameterError('Body vacio')

        Validator.validator(body,"accept_register_student.json")

        exists_student = Student.retrivied_by_id_and_status(body.get('id'), (STATUS_REGISTER_STUDENT, STATUS_UPDATE_REGISTER))
        if not exists_student:
            raise RequestParameterError('0003/Id does no exist or not valid')
        
        name_grimonio = ''
        if body.get('accept') == "no":
            Student.update_status_student(STATUS_REJECT_REQUEST_STUDENT, body.get('id'))
        else:
            ids_grimonios = Catalog.retrivied_catalog_by_name("grimonio",STATUS_ACTIVO)
            if not ids_grimonios:
                raise RequestParameterError("0004/data grimonios does not exist")
            print(ids_grimonios)
            index = randint(0, len(ids_grimonios) - 1)
            name_grimonio = ids_grimonios[index]['name']
            Student.update_status_and_grimonio_student(
                STATUS_ACCEPTED_STUDENT,
                ids_grimonios[index]['id'],
                body.get('id')                 
            )

        SQL.commit()
        return jsonify({
            "message": "accepted_student" if body.get('accept') == "yes" else "rejected_student",
            "grimonio": name_grimonio
            })
    except Exception as ex:
        return response.classify_error(ex)

def get_requests_estudents(event = None):
    try:
        students = Student.retrivied_all_students()
        if not students:
            raise RequestParameterError("0005/students does not exist")

        return jsonify({
            "students": students
        })
    except Exception as ex:
        return response.classify_error(ex)

def get_estudents_by_grimonios(event = None):
    try:
        count = Student.count_students_by_grimonio(event.get('id_grimonio'))
        name_grimonio = Catalog.retrivied_catalog_by_id(event.get('id_grimonio'), 'grimonio')
        return jsonify({
            "number_of_students": count,
            "name_grimonio": name_grimonio.get('name') if name_grimonio else ''
        })
    except Exception as ex:
        return response.classify_error(ex)

def delete_request_student(event = None):
    try:
        body = event
        if not body:
            raise RequestParameterError('Body vacio')

        Validator.validator(body,"delete_register_student.json")

        exists_student = Student.retrivied_by_id_and_status(body.get('id'), (STATUS_REGISTER_STUDENT, STATUS_UPDATE_REGISTER, STATUS_ACCEPTED_STUDENT, STATUS_DELETE_STUDENT))
        if not exists_student:
            raise RequestParameterError('0003/Id does no exist or not valid')
        
        Student.update_status_student(STATUS_DELETE_STUDENT, body.get('id'))

        SQL.commit()
        return jsonify({
            "message": "delete_student"
            })
    except Exception as ex:
        return response.classify_error(ex)