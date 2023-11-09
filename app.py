#weather app

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")
@app.route("/weatherapp", methods = ['POST', 'GET'])
def get_weatherdata():
    try:
        city = request.form.get("city")
        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=2e18e4ef351fba6f290c44d99284aa3c&units=metric"
        response = requests.get(url)
        data = response.json()
        temp = data['main']['temp']
        return f"city : {city},\n temperature:{temp}"
    except:
        return f"City not found! try some other city"

if __name__ == '__main__':
    app.run(host = '0.0.0.0')
    
