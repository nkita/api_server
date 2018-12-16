# coding:utf-8
from flask import Flask, request, redirect, url_for
#from ../lib/nk_loggin import loggin

app = Flask(__name__)


# root document
@app.route('/<ID>/detail')
def get():
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
