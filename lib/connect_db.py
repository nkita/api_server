# coding:utf-8
import psycopg2 
from configparser import ConfigParser
config = ConfigParser()
#config.read('~/Desktop/work/Flask/api_server/ini/config.ini')
config.read('../ini/config.ini')

connect_setting = "host=localhost port=5432 dbname=app_db user=postgres password=postgres"

class connect_DB():
    def __init__(self,name):
        pass
    def get_data(self,id):
        with psycopg2.connect(connect_setting) as conn: 
            with conn.cursor() as cur:
                sql =  "SELECT data FROM tb_json where id='"+id+"'"
                cur.execute(sql)
                for row  in cur:
                    data = row[0]
                print response_format("aaa");

    def get_parent_id(self,id):
        pass
    def get_child_id(self,paret_id):
        pass


def response_format(str):
    test = {"aaa":"bbb"}
    return test