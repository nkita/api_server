# coding:utf-8
from flask import Flask, request, redirect, url_for,jsonify
from lib import nk_log,connect_db
from configparser import ConfigParser

config = ConfigParser()
config.read('ini/config.ini')

# ログ初期設定

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
logger = nk_log.nk_Log(__name__)
logger.debug(config["name"]["value"])

conn = connect_db.connect_DB(__name__)
conn.get_data("4c6031fc-0206-11e9-8e9a-0242ac110002")

# root document
@app.route('/')
def index():
	logger.error("Hello World!")
	logger.debug("Hello World!")
	rsp = conn.get_all_data()
	return  jsonify(rsp)

@app.route('/data/<ID>',methods=['GET'])
def getdata(ID):
	#無害化処理
	#ID=nk_filter(ID)
	#todo file or directory
	logger.debug("Hello World!")
	rsp = conn.get_data(ID)
	return jsonify(rsp)

@app.route('/post/<DATA>',methods=['GET'])
def postdata(DATA):
	conn.insert_data(DATA)
	rsp = conn.get_all_data()
	return  jsonify(rsp)
"""
@app.route('/post', methods=['GET', 'POST'])
def post():
	title = "aa"
	logger.debug("Hello World POST!")
	return "post"
"""
# データベースのファイル一覧を取得
def getlist(ID):

	return "aaa"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0',port=7777)