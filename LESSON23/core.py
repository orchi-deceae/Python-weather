from flask import Flask, render_template, request
from weather import getCurrWeather
from waitress import serve

app = Flask(__name__)    # The paper script

@app.route('/')
@app.route('/index')     # The remembering pathway, road, map and staircase to the .html file 

def index():
    return render_template('index.html')

@app.route('/weather')   # The remembering pathway, road, map and staircase to the .html file 

def get_weather():
    city = request.args.get('city')

    # Checks for empty strings or string with only spaces
    if not bool(city.strip()):
        city = 'oyo'

    weather_data = getCurrWeather(city)

    if not weather_data['cod']==200:
        return render_template('city-not-found.html')

    return render_template(
        "weather.html",
        title=weather_data['name'],
        status=weather_data['weather'][0]['description'],
        temp=f'{weather_data['main']['temp']:.1f}',
        feels_like=f'{weather_data['main']['feels_like']:.1f}'
    )

# This is were it starts                         # this is the only page that is loading
if __name__ == '__main__':
    serve(app, host='0.0.0.0', port=8000)
    
# Everytime you reload the browser you reload the pathway-ed .html