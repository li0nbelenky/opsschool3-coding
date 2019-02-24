import requests

# api request for getting weather data per city
def getWeatherJson(city):
    weather = requests.get(
        'https://api.openweathermap.org/data/2.5/weather?q={0}&APPID=7418bc16a06c1ade22fb491105145a28'.format(
            city))
    return weather.json()

# retrieve city temperature from  json file
def getTempratureInCity(weatherJson):
    return weatherJson['main']['temp']

# retrieve city Country from  json file
def getCountryOfCity(weatherJson):
    return weatherJson['sys']['country']


if __name__ == "__main__":
    ipinfo_json = requests.get('https://ipinfo.io/json').json()      # get City Location  according to my IP.
    cityLocation = ipinfo_json["city"]

    weather_Json = getWeatherJson(cityLocation)

    temp = getTempratureInCity(weather_Json)

    cities = ('Madrid', 'Colombo', 'Edinburgh', 'Moscow', 'Sofia', 'Eilat', 'Belfast', 'Dublin', 'Bogota', 'Paris')

    with open("C:\Ex2output.txt", "w") as text_file:
        text_file.write("The weather in {0} is {1}\n\n\n".format(cityLocation, temp))

        for city in cities:
            weather_Json = getWeatherJson(city)
            country = getCountryOfCity(weather_Json)
            temp2 = getTempratureInCity(weather_Json)
            text_file.write("The weather in {0} , {1} is {2} degrees (F).\n".format(city, country ,temp2))