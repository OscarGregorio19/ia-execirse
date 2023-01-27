from config.sql import SQL

from utils.custom_errors import SQLException

class Student:

    @classmethod
    def save_student(cls, data):
        query = """
            INSERT INTO reino.ta_students(
	        name, lastname, identification, age, magic_affinity, status)
	        VALUES (%s, %s, %s, %s, %s, %s) returning id;"""
        
        result = SQL.execute(query,data)
        if result:
            return result
        return None
    
    @classmethod
    def update_student(cls, data):
        query = """
            update reino.ta_students set 
	        name = %s, lastname = %s, identification = %s, age = %s, magic_affinity = %s, status = %s
	        where id = %s"""
        
        SQL.save(query,data)
    
    @classmethod
    def retrivied_by_identification(cls, identification, status):
        query = "select id from reino.ta_students where identification = %s and status in %s;"
        data = {
            "identification": identification,
            "status": status
        }
        result = SQL.retrivied_all_wcolumnsname(query,data)
        if result:
            return result[0]
        return None
    
    @classmethod
    def retrivied_by_id_and_status(cls, id, status):
        query = "select id from reino.ta_students where id = %s and status in %s;"
        data = {
            "identification": id,
            "status": status
        }
        result = SQL.retrivied_all_wcolumnsname(query,data)
        if result:
            return result[0]
        return None

    @classmethod
    def update_status_student(cls, status, id):
        query = """
            update reino.ta_students set 
	        status = %s
	        where id = %s"""
        data = {
            "status": status,
            "id": id
        }
        SQL.save(query,data)
    
    @classmethod
    def update_status_and_grimonio_student(cls, status, grimonio, id):
        query = """
            update reino.ta_students set 
	        status = %s, grimonio = %s
	        where id = %s"""
        data = {
            "status": status,
            "grimonio": grimonio,
            "id": id
        }
        SQL.save(query,data)
    
    @classmethod
    def retrivied_all_students(cls):
        query = """
            select ts.id, ts.name, ts.lastname, ts.age, ts.identification,
            cg.name as grimonio, cm.name as magic_affinity,
            cs.name as status
            from reino.ta_students ts
            left join reino.ct_grimonio cg on cg.id = ts.grimonio
            left join reino.ct_magic_affinity cm on cm.id = ts.magic_affinity
            left join reino.ct_status cs on cs.id = ts.status
            order by 1 desc;
        """
        result = SQL.retrivied_all_wcolumnsname(query)
        if result:
            return result
        return None

    @classmethod
    def count_students_by_grimonio(cls, id_grimonio):
        if id_grimonio:
            query = "select COALESCE(count(id), 0) as contador from reino.ta_students where grimonio = %s;"
            data = {"id_grimonio": id_grimonio}
            result = SQL.retrivied_all_wcolumnsname(query,data)
        else:
            query = "select * from reino.ta_students where grimonio is null;"
            result = SQL.retrivied_all_wcolumnsname(query)
        if result:
            return result[0]['contador']
        return 0