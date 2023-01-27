from config.sql import SQL

from utils.custom_errors import SQLException

class Catalog:

    @classmethod
    def retrivied_catalog_by_name(cls,name_catalog: str, status: int):
        print('name2',name_catalog)
        name_table = 'ct_grimonio'
        if name_catalog == 'magic_affinity':
            name_table = 'ct_magic_affinity'
        elif name_catalog == 'status':
            name_table = 'ct_status'
        elif name_catalog == 'grimonio':
            name_table = 'ct_grimonio'
        else:
            raise SQLException(f"Catalogo {name_catalog} no existe")
        
        query = f"select id, name from reino.{name_table} where status = %s order by 1 asc;"
        data = {
            'status': status
        }
        result = SQL.retrivied_all_wcolumnsname(query,data)
        if result:
            return result
        return None
    
    @classmethod
    def retrivied_catalog_by_id(cls, id, name_catalog):
        name_table = 'ct_grimonio'
        if name_catalog == 'magic_affinity':
            name_table = 'ct_magic_affinity'
        elif name_catalog == 'status':
            name_table = 'ct_status'
        elif name_catalog == 'grimonio':
            name_table = 'ct_grimonio'
        else:
            raise SQLException(f"Catalogo {name_catalog} no existe")
        
        query = f"select name from reino.{name_table} where status = 1 and id = %s order by 1 asc;"
        data = {
            'id': id
        }
        result = SQL.retrivied_all_wcolumnsname(query,data)
        if result:
            return result[0]
        return None