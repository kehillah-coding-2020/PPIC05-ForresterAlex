#!/usr/bin/env python3
#
# p. 183
#

import requests
import json

url = 'https://api.worldtradingdata.com/api/v1/stock'
params = {
  'symbol': 'SNAP,TWTR,VOD.L',
  'api_token': 'Itvh5Re55wLYkJ7bfHS3yZPy96wGuaVSkV3pLLCkbfRyTMtzm8MbgaAD3cEE'
}
response = requests.request('GET', url, params=params)
response.json()

"""
5.20 Use the 'stockCorrelate' function to find out if there is a
correlation between your two favorite companies.
"""



"""
5.21 Write a function that will graph the closing prices for a stock. Your
function should accept a beginning date and an ending date along with
the ticker symbol for a stock.
"""



"""
5.22 Write a function that will graph the high, low, and closing prices
for a stock. Your function should accept a beginning date and an
ending date along with the ticker symbol for a stock.
"""



"""
5.23 Write a function that accepts a company name as a parameter and
returns the ticker symbol for the company. You will need to look at
the Yahoo website.
"""



"""
5.24 Find out if there is a correlation between volume and price for a
company of your choice.
"""



"""
5.25 Write a function that will determine the correlation between two
stocks for a given date range.
"""



"""
5.26 Wrtie a function that will accept a list of stocks as a parameter and
will return the two stocks from the list that are most highly
correlated.
"""
