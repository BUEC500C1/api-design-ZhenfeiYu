import requests
import csv

def getairportinfo(name):
    with open('airports.csv','r+') as f:
        data = csv.reader(f)
        airport = [row[3] for row in data]
    with open('airports.csv','r+') as f:
        data = csv.reader(f)
        location = [row[10] for row in data]
    location_re = location[airport.index(name)]
    print('The airport is in',location_re,'.')
    return location_re

def getweatherinfo(info):
    print('Temperature: ', info['main']['temp'], '\n'
          'Feels like: ', info['main']['feels_like'], '\n'
          'Max temperature: ', info['main']['temp_max'], '\n'
          'Min temperature: ', info['main']['temp_min'], '\n'
          'Humidity :',info['main']['humidity'], '\n'
          'Pressure :', info['main']['pressure'], '\n'
          'Weather :', info['weather'][0]['main'])
  
def main():
    name = input('Please enter the airport name : ') 
    location = getairportinfo(name)
    url = 'https://api.openweathermap.org/data/2.5/weather?q={}&appid=6d9fd9987ade1517bae7f67207234ede'.format(location)
    res = requests.get(url)
    info = res.json()
    getweatherinfo(info)  

if __name__ == "__main__":
    main()
