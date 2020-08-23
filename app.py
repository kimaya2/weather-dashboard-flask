import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config['openweathermap']['api']

def get_weather_results(city, API_key):

    API_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_key)
    r = requests.get(API_url)
    return r.json()

@app.route('/')
def waether_dashboard():
    return render_template("home.html")

@app.route("/results", methods = ['POST'])
def render_results():
    city = request.form['City']
    data = get_weather_results(city, get_api_key())

    temp = "{0:.2f}".format(data['main']['temp'])
    humidity = "{0:.2f}".format(data['main']['humidity'])
    pressure = "{0:.2f}".format(data['main']['pressure'])
    
    location = data['name']

    return render_template("results.html", location = location, temp = temp, humidity = humidity, pressure = pressure)

if __name__ == "__main__":
    app.run()

