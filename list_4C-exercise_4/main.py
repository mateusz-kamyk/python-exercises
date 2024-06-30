#!/usr/bin/env python3

import requests

api_key = "89c1cc0e8c7e3a2724cc9f45e34f47ff"

def user_input():
    city = str(input("Please provide city: "))
    return city

def check_city_id(city, api_key):
    city_id_request = requests.get(f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=5&appid={api_key}")
    if city_id_request.status_code == 200:
        response = city_id_request.json()
        lat = response[0]['lat']
        lon = response[0]['lon']
    else:
        print("Check API request.")
    return lat, lon

def check_weather(lat, lon, api_key):
    weather_request = requests.get(f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={api_key}")
    if weather_request.status_code == 200:
        weather_response = weather_request.json()
    else:
        print("Check API request.")
    return weather_response

if __name__=="__main__":
    city = user_input()
    lat, lon = check_city_id(city, api_key)
    weather = check_weather(lat, lon, api_key)
    print(weather)