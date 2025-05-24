import requests 
import pandas as pd

#Fetch CPI data 
url = 'https://www.alphavantage.co/query?function=CPI&interval=monthly&apikey=FGGNU5J3ZHVRGBWB'
response = requests.get(url)
data = response.json()

#Convert to DataFrame 
df = pd.DataFrame(data["data"])

#Save to CSV 
df.to_csv("cpi_data.csv", index=False)
