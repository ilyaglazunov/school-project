#!/usr/bin/python
# -*- coding: utf-8 -*-
import requests
import json
import datetime

api_key = '0dc7e51f75b2bdb63577053fd67c127c'

country_code = 'us'

zip_code = input('Enter zip code : ')

complete_url = 'http://api.openweathermap.org/data/2.5/weather?zip=' \
    + zip_code + ',' + country_code + '&appid=' + api_key

response = requests.get(complete_url)

x = response.json()

if x['cod'] != '404':

    y = x['main']
    current_temperature = y['temp']
    current_temperature = current_temperature * 9 / 5 - 459.67
    current_temperature = round(current_temperature, 2)
    current_pressure = y['pressure']

    z = x['wind']

    wind_speed = z['speed']
    wind_direction = z['deg']
    print 'Name:                     KSU '
    print 'Current Temperature       ' + str(current_temperature) \
        + ' degree Farenheit' + '\nAtmospheric Pressure      ' \
        + str(current_pressure) + ' hPa' \
        + '\nWind Speed                ' + str(wind_speed) + 'mph' \
        + '\nWind Direction            ' + str(wind_direction) \
        + '\nTime of Report            ' + str(datetime.datetime.now())
else:
    print ' Zip Code Not Found '
