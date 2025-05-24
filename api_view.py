#import response
#import pandas
#import sqlalchemy 
import requests
import json


#url = 'https://www.alphavantage.co/documentation/' #economic indicators 

"""
header = {"Content-Type": "application/json"
          "Accept- Encoding": "deflate"}
'
"""

#responce = requests.get('https://www.alphavantage.co/documentation/')

#restart- following alphaVantage reqest code

url = 'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=FGGNU5J3ZHVRGBWB'

r = requests.get(url)
data = r.json()

#print(data)
print(json.dumps(data, indent=4))