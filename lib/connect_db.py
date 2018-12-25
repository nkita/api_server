# coding:utf-8
import psycopg2, json
from configparser import ConfigParser
from flask import Flask, request, redirect, url_for,jsonify

config = ConfigParser()
#config.read('~/Desktop/work/Flask/api_server/ini/config.ini')
config.read('../ini/config.ini')

connect_setting = "host=localhost port=5432 dbname=app_db user=app_user password=app_user"

class connect_DB():
    def __init__(self,name):
        pass
    def get_data(self,id):
        with psycopg2.connect(connect_setting) as conn: 
            with conn.cursor() as cur:
                sql =  "SELECT data FROM tb_json where id='"+id+"'"
                try:
                    cur.execute(sql)
                    for row  in cur:
                        data = row[0]
                        rsp = response_format(200,data)
                        return rsp
                    return response_format(404,"No Data")
                except Exception as e:
                    rsp = response_format(500,"System Error")
                    #todo
                    # log e
                    return rsp
    def get_all_data(self):
        with psycopg2.connect(connect_setting) as conn: 
            with conn.cursor() as cur:
                sql =  "SELECT * FROM tb_json limit 100"
                try:
                    cur.execute(sql)
                    results = cur.fetchall()
                    dict_result = []
                    for row in results:
                        print(row,type(row))

#                    rsp = rsponse_format(200,cur.fetchall())
                    return cur.fetchall()
                except Exception as e:
                    rsp = response_format(500,"System Error")
                    #todo
                    # log e
                    return rsp
    def get_parent_id(self,id):
        pass
    def get_child_id(self,paret_id):
        pass
    def insert_data(self,data):
        with psycopg2.connect(connect_setting) as conn: 
            with conn.cursor() as cur:
                sql =  "INSERT INTO tb_json(id,parent_id,data) values (uuid_generate_v1(),NULL,jsonb(%s))"
                try:
                    cur.execute(sql, [json.dumps(data)])
                except Exception as e:
                    rsp = response_format(500,"System Error")
                    print(e)
                    return e
                    #todo
                    # log e
        return "aaa"


def response_format(status,data):
    rsp = {"status":status,"data":data}
    return rsp