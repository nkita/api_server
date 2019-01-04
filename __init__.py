# coding:utf-8
import json
from flask import Flask, request, redirect, url_for,jsonify
from lib import nk_log,nk_common,connect_db
from configparser import ConfigParser

config = ConfigParser()
config.read('ini/config.ini')

# ログ初期設定

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
logger = nk_log.nk_Log(__name__)
_nkmods = nk_common.mods(__name__)
logger.debug(config["name"]["value"])
conn = connect_db.connect_DB(__name__)

# gr(get_row) : default=100 (max 10,50,100)
# pg(page) : default=1 (1,2,3 ...)
# so(sort) : default=modify_date sort(add_date,modify_date)
# ad(asc or desc): default=des (asc or desc)
# sh(search) : search=keyword

param = ['gr','pg','so','ad','sh']
param_value = {}

# root document 
@app.before_request
def _before_request():
	#get parameter and filter
	param_value = {}
	for row in param:
		val = "null"
		try:
			val = request.args.get(row)
		except Exception as e:
			logger.error(e)
			pass
		if val != "null":
			param_value.update({row:val})
	request._param_value_ = param_value

@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return  conn.get_all_data(request._param_value_)
	elif request.method == 'POST':
		try:
			json_data = request.json
			conn.insert_data(json_data)
			return  _nkmods.response(200, "Success")
		except Exception as e:
			logger.error(e)
			return _nkmods.response(500, "[Error] Please input a JSON data. Please set the  'application/json' for Body content type.")
	else:
		return "Not found order"

@app.route('/<ID>',methods=['GET','DELETE','PUT'])
def delete(ID):
	if request.method == 'GET':
		rsp = conn.get_data(ID)
		return rsp
	elif request.method == 'DELETE':
		try:
			conn.delete_data(ID)
			return _nkmods.response(500,"Success")
		except Exception as e:
			logger.error(e)
			return _nkmods.response(500,"Error")
	elif request.method == 'PUT':
		return _nkmods.response(500,"工事中")
	else:
		return _nkmods.response(500, "Not found order")

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=7777)
