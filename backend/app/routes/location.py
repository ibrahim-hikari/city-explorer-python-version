import os
from flask import jsonify, request
import requests
from decouple import config


def main_routes(app):
    GEOCODE = config('GEOCODE')
    SKY_API = config('SKY_API')

    @app.route('/location', methods=['GET', 'POST'])
    def locationHandler():
        cityName = request.args.get('cityName')
        print('\ncityName\t', GEOCODE)
        url = f'https://us1.locationiq.com/v1/search.php?key={GEOCODE}&q={cityName}&format=json'
        try:
            response = requests.get(url)
            return dict(response.json()[0]), 200

        except:
            return 'Wrong City Name', 404

    @app.route('/weather', methods=['GET', 'POST'])
    def weatherHandler():
        city = request.get_json()
        lat = city['lat']
        lng = city['lng']
        print('city\t', city)
        print('city lat\t', city['lat'])
        url = f'https://api.darksky.net/forecast/{SKY_API}/{lat},{lng}'

        response = requests.get(url)
        # print(response.json()['daily'])
        return {"data": response.json()['daily']['data']}
