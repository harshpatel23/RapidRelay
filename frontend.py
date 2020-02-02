from flask import Flask, render_template
import pymysql
import traceback


app = Flask(__name__)
server = 'localhost'
username = 'root'
password = ''
database = 'bugbox_db'
cursorclass = pymysql.cursors.DictCursor


@app.route('/')
def hello_world():
	return render_template('home.html')


@app.route('/weather/<city>/', methods=['GET'])
def show_city_weather(city):
	# query database
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()
	count_sql = 'SELECT COUNT(*) as c FROM weather_data WHERE city="'+city+'";'

	sql = 'SELECT * FROM weather_data where city="'+city+'" ORDER BY `TIME` DESC LIMIT 20;'
	print(sql)
	try:
		cursor.execute(count_sql)
		counts = cursor.fetchone()
		print(counts['c'])
		cursor.execute(sql)
		results = cursor.fetchall()
	except Exception as e:
		traceback.print_exc()
		db.rollback()

	db.close()
	return render_template("tables.html", data=results, count=counts['c'])


@app.route('/agriculture/', methods=['GET'])
def show_greehouse_data():
	# query database
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()
	count_sql = 'SELECT COUNT(*) as c FROM agriculture_data;'
	sql = 'SELECT * FROM agriculture_data ORDER BY `TIME` DESC LIMIT 20;'
	print(sql)
	try:
		cursor.execute(count_sql)
		counts = cursor.fetchone()
		cursor.execute(sql)
		results = cursor.fetchall()
	except Exception as e:
		traceback.print_exc()
		db.rollback()

	db.close()
	return render_template("tables.html", data=results, count=counts['c'])


@app.route('/air_quality/<city>/', methods=['GET'])
def show_city_air_quality(city):
	# query database
	db = pymysql.connect(server, username, password, database, cursorclass=cursorclass)
	cursor = db.cursor()
	count_sql = 'SELECT COUNT(*) as c FROM air_quality_data WHERE city="' + city + '";'
	sql = 'SELECT * FROM air_quality_data where city="'+city+'" ORDER BY `TIME` DESC LIMIT 20;'
	print(sql)
	try:
		cursor.execute(count_sql)
		counts = cursor.fetchone()
		cursor.execute(sql)
		results = cursor.fetchall()
	except Exception as e:
		traceback.print_exc()
		db.rollback()

	db.close()
	return render_template("tables.html", data=results, count=counts['c'])


if __name__ == '__main__':
	app.run(debug=True)
