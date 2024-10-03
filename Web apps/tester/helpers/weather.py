import requests

class WeatherApi:
    def __init__(self) -> None:
        self.base_url = 'https://api.weather.gov' 

    def get_point(self, lat:float, lon:float):
        endpoint = self.base_url + f'/points/{lat},{lon}'
        return requests.get(endpoint).json()
    
    def get_forecast(self, lat:float, lon:float):
        p = self.get_point(lat,lon)
        return requests.get(p['properties']['forecast']).json()
     


if  __name__ == '__main__':
    c = WeatherApi()
    print(c.get_forecast(26.96, -82.351))



    
