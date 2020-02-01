from flask import Flask
app = Flask(__name__)


@app.route('/data/write', methods=['GET', 'POST'])
def store():
	return None