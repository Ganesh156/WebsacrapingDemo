import pandas as pd
from bs4 import BeautifulSoup
import requests

page = requests.get('Use URL of National whether forecasting of any particular place')
soup = BeautifulSoup(page.content,'html.parser')#Using BeautifulSoup package scraping the content of the URL and parsing the HTML page
week = soup.find(id='seven-day-forecast-body') # Scraping any 'id'(in <div>) of the webpage.
items=(week.find_all(class_='tombstone-container'))   # It will scrap classes which comes under 'id'(using week variable)

# Getting only text insted of fetching tags of HTML.
'''print(items[0].find(class_='period-name').get_text())
print(items[0].find(class_='short-desc').get_text())
print(items[0].find(class_='temp').get_text())
'''
# Getting multiple data by using for loop.
period_names = [item.find(class_='period-name').get_text() for item in items]
short_description = [item.find(class_='short-desc').get_text() for item in items]
tempareture = [item.find(class_='temp').get_text() for item in items]
'''print(period_names)
print(short_description)
print(tempareture)
'''

# Structuring data using pandas libraries.
weather_stuff = pd.DataFrame(
    {
        'period':period_names,
        'Short_description':short_description,
        'Temperatures':tempareture
     })
print(weather_stuff)

# Creating 'CSV' file.
weather_stuff.to_csv('result.csv')