import psycopg2
import os

from utils.custom_errors import SQLException

class SQL:
    __instance = None
    conn = None

    def __new__(cls):
        if SQL.__instance is None:
            SQL.__instance = object.__new__(cls)
        return SQL.__instance

    @classmethod
    def get_data(cls, data):
        return SQL(**data)

    @classmethod
    def init(cls):
        if not cls.conn:
            cls.conn = psycopg2.connect(
                host=os.environ.get('HOST_SQL'),
                port=os.environ.get('PORT_SQL'),
                database=os.environ.get('DATABASE_SQL'),
                user=os.environ.get('USER_SQL'),
                password=os.environ.get('PASSWORD_SQL'),
            )
            cls.conn.autocommit = False
            return SQL()
        else:
            return SQL()

    @classmethod
    def execute(cls, command, values=None):
        try:
            if not values:
                raise Exception
            cur = cls.conn.cursor()
            cur.execute(command, list(values.values()))
            resp = cur.fetchone()[0]
            cur.close()
            values['id'] = resp
            return values
        except Exception as ex:
            print('error {}'.format(ex))
            cls.rollback()
            #cls.conn.close()
            raise SQLException('error sql')
    
    @classmethod
    def save(cls, command, values=None):
        try:
            if not values:
                raise Exception
            cur = cls.conn.cursor()
            cur.execute(command, list(values.values()))
            cur.close()
        except Exception as ex:
            print('error {}'.format(ex))
            cls.rollback()
            cls.close()
            raise SQLException('error sql')

    @classmethod
    def retrivied_all_wcolumnsname(cls, command, values=None):
        try:
            print("llego aqui si")
            cur = cls.conn.cursor()
            
            if values:
                cur.execute(command, list(values.values()))
            else:
                cur.execute(command)
            
            rows = [x for x in cur]
            cols = [x[0] for x in cur.description]
            items = []
            for row in rows:
                item = {}
                for prop, val in zip(cols, row):
                    item[prop] = val
                items.append(item)

            if items:
                return items
            else:
                return None
                
        except Exception as ex:
            print('error {}'.format(ex))
            cls.conn.close()

    @classmethod
    def commit(cls):
        if cls.conn:
            cls.conn.commit()

    @classmethod
    def rollback(cls):
        if cls.conn:
            cls.conn.rollback()

    @classmethod
    def close(cls):
        if cls.conn:
            cls.conn.close()
            cls.conn = None