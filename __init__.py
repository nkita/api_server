# coding:utf-8
from flask import Flask, request, redirect, url_for
from lib import nk_log,connect_db
from configparser import ConfigParser

config = ConfigParser()
config.read('ini/config.ini')

# ログ初期設定

app = Flask(__name__)
logger=nk_log.nk_Log(__name__)
logger.debug(config["name"]["value"])

print("aaaa")

# root document
@app.route('/')
def index():
	logger.error("Hello World!")
	logger.debug("Hello World!")
	return  "top"

@app.route('/id/<ID>',methods=['GET'])
def getdata(ID):
	#無害化処理
	#ID=nk_filter(ID)
	#todo file or directory
	logger.debug("Hello World!")
	
	return getlist(ID)
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
	app.run(host='0.0.0.0')