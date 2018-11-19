# coding:utf-8
from flask import Flask, request, redirect, url_for
from lib import nk_log

# ログ初期設定

app = Flask(__name__)
logger=nk_log.nk_Log(__name__)

# root document
@app.route('/')
def index():
	logger.error("Hello World!")
	logger.debug("Hello World!")
	return  "top"

@app.route('/post', methods=['GET', 'POST'])
def post():
	title = "aa"
	logger.debug("Hello World POST!")
	return "post"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')