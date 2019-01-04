# coding:utf-8

#  common class
#
import json
from flask import Flask, request, redirect, url_for, jsonify
from lib import nk_log
from configparser import ConfigParser

config = ConfigParser()
config.read('ini/config.ini')

logger = nk_log.nk_Log(__name__)
logger.debug(config["name"]["value"])

class mods():
    def __init__(self,str):
        pass
    def chk_json(self,str):
        try:
            json.loads(str)
        except ValueError as e:
            print(e)
            return False
        except Exception as e:
            print(e)
            return False
        return True
        
    def response(self,status,data):
        if type(data) is list:
            rsp = {"info": {"status": status, "action": "all","disp_count": len(data)}, "records": data}
        else:
            rsp = {"info": {"status": status, "action": "all","disp_count": "-"}, "records": data}
        return jsonify(rsp)

    def get_dicdata(self,dictdata,key):
        try:
            if key not in dictdata:
                return False    
            if key == 'gr':
                return int(dictdata[key])
            if key == 'pg':
                return int(dictdata[key])
            return dictdata[key]

        except Exception as e:
            logger.error(e)
            return False
