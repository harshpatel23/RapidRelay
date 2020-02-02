from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('index.html')


@app.route('/weather/<city>')
def show_city_weather(city):
# query database
return None

if __name__ == '__main__':
    app.run()