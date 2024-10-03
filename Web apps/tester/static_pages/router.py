from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from helpers.catapi import CatApi
from helpers.weather import WeatherApi


static_pages_router = APIRouter()
templates = Jinja2Templates(directory=".")

@static_pages_router.get('/')
def index(request: Request):
    return templates.TemplateResponse(
        'static_pages/templates/index.html',
        context={'request': request })

@static_pages_router.get('/api')
def api(request: Request):
    c = CatApi()
    result= c.get_facts()
    return templates.TemplateResponse(
        'static_pages/templates/api.html',
        context={'request': request,'facts': result })

@static_pages_router.get('/weather/{lat},{lon}')
def weather(request: Request, lat:float, lon:float):
    w = WeatherApi()
    forecast = w.get_forecast(lat,lon)
    return templates.TemplateResponse(
        'static_pages/templates/weather.html',
        context={'request': request,'forecast': forecast })

@static_pages_router.get('/weatherHourly/{lat},{lon}')
def forecastHourly(request: Request, lat:float, lon:float):
    w = WeatherApi()
    forecastHourly = w.get_forecastHourly(lat,lon)
    return templates.TemplateResponse(
        'static_pages/templates/hourly.html',
        context={'request': request,'forecastHourly': forecastHourly })