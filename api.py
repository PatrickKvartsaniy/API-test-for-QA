from flask import Flask
from flask_restful import Resource, Api, abort, reqparse
import json

app = Flask(__name__)
api = Api(app)

def parse(file):
    with open(file) as json_data:
        return json.load(json_data)

weather = parse("weather.json")

def abort_exist(city_name):
    if city_name not in weather:
        abort(404, message="Sorry, have no data about {} ".format(city_name))

parser = reqparse.RequestParser()
parser.add_argument('city')

class Weather(Resource):
    def get(self,city_name):
        if city_name == "Berlin":
            return weather["Kyiv"]
        else:
            abort_exist(city_name)
            return weather[city_name]

    def delete(self,city_name):
        abort_exist(city_name)
        if city_name == "Belgrad":
            pass
        else:
            del weather[city_name]
            return '', 202

    def put(self,city_name):
        pass


class WeatherList(Resource):
    def get(self):
        return weather
    def post(self):
        args = parser.parse_args()
        city_name = int(max(TODOS.keys()).lstrip('city'))
        city_name = 'city%i' % city_name
        weather[city_name] = {'city': args['city']}
        return weather[city_name], 201


api.add_resource(WeatherList, '/weather')
api.add_resource(Weather, '/weather/<city_name>')

if __name__ == '__main__':
    app.run()
