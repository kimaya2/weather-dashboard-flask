import requests
import configparser
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def waether_dashboard():
    return render_template("home.html")

@app.route("/results", methods = ['POST'])
def render_results():
    city = request.form['City']
    return "City: " + city

if __name__ == "__main__":
    app.run()

def get_api_key():
    config = configparser.ConfigParser()
    config.read("config.ini")
    return config['openweathermap']['api']

def get_weather_results(city, API_key):

    API_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, API_key)
    r = requests.get(API_url)
    return r.json()

print(get_weather_results("Pune",get_api_key()))
