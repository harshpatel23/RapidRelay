from flask import Flask, render_template
import pymysql

app = Flask(__name__)
server = 'localhost'
username = 'root'
password = ''
database = 'bugbox_db'
cursorclass = pymysql.cursors.DictCursor


@app.route('/')
def hello_world():
	return render_template('base.html')


@app.route('/weather/<city>/', methods=['GET'])
def show_city_weather(city):
	# query database
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()
	sql = 'SELECT * FROM weather_data where city="'+city+'" SORT BY TIME DESC LIMIT 10;'
	try:
		cursor.execute(sql)
		results = cursor.fetchall()
	except Exception as e:
		traceback.print_exc()
		db.rollback()

	db.close()
	return render_template("tables.html", context={'data': results})


if __name__ == '__main__':
	app.run(debug= True)