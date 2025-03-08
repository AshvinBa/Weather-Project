from flask import Flask, render_template, request
import requests
from datetime import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        city_name = request.form.get('name', '')
        api_key = 'b56dfe46f0495d2110b0d04dd84392a9'  # Replace with your API key
        url = f'http://api.openweathermap.org/data/2.5/weather?q={city_name}&units=metric&APPID={api_key}'
        
        try:
            response = requests.get(url).json()
            
            weather_data = {
                'temp': response['main']['temp'],
                'weather': response['weather'][0]['description'],
                'min_temp': response['main']['temp_min'],
                'max_temp': response['main']['temp_max'],
                'icon': response['weather'][0]['icon'],
                'wind_spd': f"{response['wind']['speed']} m/s",
                'sunrise': datetime.fromtimestamp(response['sys']['sunrise']).strftime('%H:%M'),
                'sunset': datetime.fromtimestamp(response['sys']['sunset']).strftime('%H:%M'),
                'humidity': f"{response['main']['humidity']}%",
                'pressure': f"{response['main']['pressure']} hPa",
                'sea_lvl': response['main'].get('sea_level', 'N/A'),
                'grd_lvl': response['main'].get('grnd_level', 'N/A'),
                'city_name': city_name.title()
            }
            
            return render_template('index.html', **weather_data)
        except Exception as e:
            return render_template('index.html', error="City not found or API error")
            
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)

















# from flask import Flask, render_template, request
# import requests  # pip install requests

# app = Flask(__name__)

# @app.route('/', methods = ['GET','POST'])
# def index():
#     if request.method == 'POST':
#         city_name = request.form['name']
#         url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=b56dfe46f0495d2110b0d04dd84392a9'
#         response = requests.get(url.format(city_name)).json()
        
#         temp = response['main']['temp']
#         weather = response['weather'][0]['description']
#         min_temp = response['main']['temp_min']
#         max_temp = response['main']['temp_max']
#         icon = response['weather'][0]['icon']
#         wind_spd = response['wind']['speed']
#         sunrise = response['sys']['sunrise']
#         sunset = response['sys']['sunset']
#         humidity = response['main']['humidity']
#         pressure = response['main']['pressure']
#         sea_lvl = response['main']['sea_level']
#         grd_lvl =response['main']['grnd_level']
        
#         print(temp,weather,min_temp,max_temp,icon)
#         return render_template('index.html', temp = temp, weather = weather, min_temp = min_temp, max_temp = max_temp, icon = icon, city_name = city_name , wind_spd = wind_spd , sunrise = sunrise, sunset = sunset, humidity = humidity, pressure = pressure, sea_lvl = sea_lvl, grd_lvl = grd_lvl)
#     else:
#         return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug = True)
























# src="https://maps.googleapis.com/maps/api/js?key={{ AIzaSyDqUtx9tnNnjDAN3QknrunSpWw9Y3FOrj0 }}&callback=initMap">
# Weathor Api : b56dfe46f0495d2110b0d04dd84392a9





# from flask import Flask, render_template, request
# import requests # pip install requests

# app = Flask(__name__) #Initialise app

# @app.route('/', methods = ['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         city_name = request.form['name']

#         url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&APPID=YOUR_API_KEY'
#         response = requests.get(url.format(city_name)).json()
        
#         temp = response['main']['temp']
#         weather = response['weather'][0]['description']
#         min_temp = response['main']['temp_min']
#         max_temp = response['main']['temp_max']
#         icon = response['weather'][0]['icon']
        
#         print(temp,weather,min_temp,max_temp,icon)
#         return render_template('index.html',temp=temp,weather=weather,min_temp=min_temp,max_temp=max_temp,icon=icon, city_name = city_name)
#     else:
#         return render_template('index.html')



# if __name__ == '__main__':
#     app.run(debug=True)