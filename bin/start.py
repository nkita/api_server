from flask import Flask, request, redirect, url_for

app = Flask(__name__)

# root document
@app.route('/')
def index():
	return  "top"

@app.route('/post', methods=['GET', 'POST'])
def post():
	title = "aa"
	return "post"

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
