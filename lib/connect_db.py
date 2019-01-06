# coding:utf-8
import psycopg2
import psycopg2.extras
import datetime
import json
import uuid
from lib import nk_common,nk_log
from configparser import ConfigParser
from flask import Flask, request, redirect, url_for, jsonify

config = ConfigParser()
# config.read('~/Desktop/work/Flask/api_server/ini/config.ini')
config.read('ini/config.ini')

logger = nk_log.nk_Log(__name__)
logger.debug(config["name"]["value"])

connect_setting = "host=localhost port=5432 dbname=app_db user=app_user password=app_user"

_nkmods = nk_common.mods(__name__)


class connect_DB():
    def __init__(self, name):
        pass

    def get_data(self, id):
        sql = "SELECT * FROM tb_json where id='"+id+"'"
        result = execute_query(sql,[])
        if type(result) is list:
            return _nkmods.response("Succusess", result)
        else:
            return _nkmods.response("Error", str(result))

    def get_all_data(self,params):
        if _nkmods.get_dicdata(params,"so"):
            _so = _nkmods.get_dicdata(params,"so")
        else:
            _so = "modify_date"
        if _nkmods.get_dicdata(params,"ad"):
            _ad = _nkmods.get_dicdata(params,"ad")
        else:
            _ad = "desc"
        if _nkmods.get_dicdata(params,"gr"):
            _gr = _nkmods.get_dicdata(params,"gr")
        else:
            _gr = 100
        if _nkmods.get_dicdata(params,"pg"):
            _pg = _nkmods.get_dicdata(params,"pg")
        else:
            _pg = 0
        sql = "SELECT * FROM tb_json order by "+_so+" "+_ad+" limit %s offset %s"
        result = execute_query(sql,[_gr,_pg])
        if type(result) is list:
            return _nkmods.response("Succusess", result)
        else:
            logger.error(str(result))
            return _nkmods.response("Error", {"msg":"System error"})

    def get_parent_id(self, id):
        pass

    def get_child_id(self, paret_id):
        pass

    def insert_data(self, json_data):
        with psycopg2.connect(connect_setting) as conn:
            with conn.cursor() as cur:
                _today = datetime.datetime.today()
                _id = str(uuid.uuid4());
                sql = "INSERT INTO tb_json(id,parent_id,data,add_date,modify_date) values (%s,NULL,jsonb(%s),%s,%s)"
                try:
                    cur.execute(sql, [_id,json.dumps(json_data),_today,_today])
                except Exception as e:
                    logger.error(e)
                    return _nkmods.response("Error", {"msg":"System Error"})
        return connect_DB.get_data(self,_id)

    def delete_data(self, id):
        sql = "DELETE FROM tb_json where id='"+id+"'"
        result = execute_query(sql,[])
        if type(result) is list:
            return _nkmods.response("Succusess", result)
        else:
            return _nkmods.response("Error", str(result))


def fetchall2dict(results, colnames):
    records = []
    for row in results:
        record = {}
        for name in colnames:
            if type(row[name]) is datetime.datetime:
                record.update({name: str(row[name])})
            else:
                record.update({name: row[name]})
        records.append(record)
    return records

def execute_query(sql,option):
    with psycopg2.connect(connect_setting) as conn:
        with conn.cursor(cursor_factory=psycopg2.extras.DictCursor) as cur:
            try:
                cur.execute(sql,option)
                logger.debug("execute query="+str(cur.query))
                results = cur.fetchall()
                colnames = [col.name for col in cur.description]
                records = fetchall2dict(results, colnames)
                return records
            except psycopg2.DataError as e:
                return "Input Data Error."
            except Exception as e:
                return e
