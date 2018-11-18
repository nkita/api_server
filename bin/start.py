# coding:utf-8
from flask import Flask, request, redirect, url_for
import logging
from logging import getLogger, StreamHandler, Formatter

app = Flask(__name__)
logger = getLogger(__name__)
logger.setLevel(logging.DEBUG)
stream_handler = StreamHandler()
stream_handler.setLevel(logging.DEBUG)
handler_format = Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(handler_format)
logger.addHandler(stream_handler)


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
