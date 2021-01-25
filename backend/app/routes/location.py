import os
from flask import jsonify, request
import requests
from decouple import config


def main_routes(app):
    GEOCODE = config('GEOCODE')
    SKY_API_KEY = config('SKY_API_KEY')
    EVENT_API_KEY = config('EVENT_API_KEY')
    MOVIE_API_KEY = config('MOVIE_API_KEY')
    YELP_API_KEY = config('YELP_API_KEY')

    #pylint: disable=unused-variable
    @app.route('/location', methods=['GET', 'POST'])
    def locationHandler():
        cityName = request.args.get('cityName')
        url = f'https://us1.locationiq.com/v1/search.php?key={GEOCODE}&q={cityName}&format=json'
        try:
            response = requests.get(url)
            return dict(response.json()[0]), 200

        except:
            return 'WrosKsbWGsk0cV-i2xO015Kp6n83buPf8a-RAb3yBShyIPxLBwj-d2Chu7TMciRijfnZ4nZf8ePmZQLi_Oms0sJxuf91svLVFWNMNkgaYrAgVlmMBM4_nN6-w56Vi0GXnYxng City Name', 404

    @app.route('/weather', methods=['GET', 'POST'])
    def weatherHandler():
        city = request.get_json()
        lat = city['lat']
        lng = city['lng']
        url = f'https://api.darksky.net/forecast/{SKY_API_KEY}/{lat},{lng}'

        response = requests.get(url)
        return {"data": response.json()['daily']['data']}

    @app.route('/event', methods=['GET', 'POST'])
    def eventHandler():
        city = request.get_json()
        cityName = city['name']
        url = f'http://api.eventful.com/json/events/search?app_key={EVENT_API_KEY}&location={cityName}'

        response = requests.get(url)
        return({"data": response.json()['events']['event']})

    @app.route('/movie', methods=['GET', 'POST'])
    def movieHandler():
        city = request.get_json()
        cityName = city['name']
        url = f'https://api.themoviedb.org/3/search/movie?api_key={MOVIE_API_KEY}&query={cityName}'

        response = requests.get(url)
        return {"data": response.json()['results']}, 200

    # @app.route('/trails', methods=['GET', 'POST'])
    # def trailsHandler():
    #     city = request.get_json()
    #     lat = city['lat']
    #     lng = city['lng']

    @app.route('/yelp', methods=['GET','POST'])
    def yelpHandler():
        city = request.get_json()
        cityName = city['name']
        url = f'https://api.yelp.com/v3/businesses/search?location={cityName}'

        response = requests.get(url, headers={'Authorization': f'Bearer {YELP_API_KEY}'})

        return response.json()