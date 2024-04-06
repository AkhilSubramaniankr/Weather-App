import requests

def get_weather(city):
    api_key = 'f712556d541664bde8994e86357855e4'
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    
    response = requests.get(url)
    data = response.json()
    
    if data['cod'] == 200:
        weather_description = data['weather'][0]['description']
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        wind_speed = data['wind']['speed']
        
        print(f'Weather in {city}:')
        print(f'Description: {weather_description}')
        print(f'Temperature: {temperature}°C')
        print(f'Humidity: {humidity}%')
        print(f'Wind Speed: {wind_speed} m/s')
    else:
        print('City not found. Please try again.')

if __name__ == "__main__":
    city = input("Enter a city name: ")
    get_weather(city)
