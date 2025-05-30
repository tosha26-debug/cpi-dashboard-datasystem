import requests 
import pandas as pd

BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"
SYMBOLS = ['AAPL', 'TSLA', 'V', 'CRM', 'ABNB']
LIMIT = 300

def fetch_ohlc(symbol):
    """ Fetch and clean OHLC data for given symbol. """
    url = f"{BASE_URL}/v0/ohlc/{symbol}"
    params = {"skip": 0, "limit": LIMIT}
    response = requests.get(url, params=params)
    response.raise_for_status()
    
    data = response.json()
    df = pd.DataFrame(data)
    
    if df.empty:
        print(f"No data found for {symbol}")
        return df
    
    df ['symbol_id'] = symbol 
    df.rename(columns={
        'timestamp_ms' : 'timestamp',
        'adj_high': 'high',
        'adj_low': 'low',
        'adj_close' : 'close',
        'adj_open': 'open'
        
    }, inplace=True)
    
    df['timestamp'] = pd.to_datetime(df['timestamp'], unit='ms').dt.strftime('%Y%m%d')

    
    columns_to_keep = ['symbol_id', 'timestamp', 'volume', 'high', 'close', 'low', 'open']
    return df[columns_to_keep]

def fetch_all_symbols(symbols):
    """Fetch OHLC data for all symbols and return a combined DataFrame"""
    all_dfs = [fetch_ohlc(symbol) for symbol in symbols ]
    final_df = pd.concat(all_dfs, ignore_index=True)
    return final_df

if __name__ == "__main__":
    df_all = fetch_all_symbols(SYMBOLS)
    print(df_all.head())    #preview results 
    
    
















# # -*- coding: utf-8 -*-
# """df_ohlc_cleaned.ipynb

# Automatically generated by Colab.

# Original file is located at
#     https://colab.research.google.com/drive/1zdX9Vy3MOBlV3OQHm0TloLW7qwUYpSro
# """

# import requests
# import pandas as pd
# #from IPython.display import display



# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# symbols = ['APPL', 'TSLA', 'V']

# all_data = []

# for symbol in symbols:

#     SYMBOLS_ENDPOINT = f"{BASE_URL}/v0/symbols/"
#     TIMESTAMP_ENDPOINT = f"{BASE_URL}/v0/symbols/"
#     EXCHANGE_ENDPOINT = f"{BASE_URL}/v0/symbols/"
#     BALANCE_SHEET_ENDPOINT = f"{BASE_URL}/v0/balance_sheet/V"
#     CASH_FLOW_ENDPOINT = f"{BASE_URL}/v0/symbols/"
#     INCOME_STATEMENT = f"{BASE_URL}/v0/symbols/"
#     OHLC_STATEMENT = f"{BASE_URL}/v0/ohlc/AAPL"
#     OPERATION_STATEMENT = f"{BASE_URL}/v0/symbols/"

# # BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"


# # # Endpoint for retrieving symbols
# # SYMBOLS_ENDPOINT = f"{BASE_URL}/v0/symbols/"


# # params = {"skip": 0, "limit": 100}
# # response = requests.get(SYMBOLS_ENDPOINT, params=params)
# # response.raise_for_status()  # Raise an exception for bad status codes
# # data = response.json()
# # df_symbols = pd.DataFrame(data)

# params = {"skip": 0, "limit": 100}
# response = requests.get(OHLC_STATEMENT, params=params)
# response.raise_for_status()  # Raise an exception for bad status codes
# data = response.json()
# df_ohlc_statement = pd.DataFrame(data)
# #from IPython.display import display
# print(df_ohlc_statement)

# df_ohlc_statement.rename(columns ={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'

# }, inplace=True)


# #from IPython.display import display
# print(df_ohlc_statement)

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp', 'exchange_id', 'volume', 'high', 'close', 'low', 'open']  # Replace with the columns you want to keep

# # Keep only the specified columns
# df_ohlc_statement = df_ohlc_statement[columns_to_keep]

# # Display the updated dataframe
# print(df_ohlc_statement)

# df_ohlc_statement['timestamp'] = pd.to_datetime(df_ohlc_statement['timestamp'], unit='ms')
# df_ohlc_statement['timestamp'] = df_ohlc_statement['timestamp'].dt.strftime('%Y%m%d')
# print(df_ohlc_statement)

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbol_ids you want to retrieve data for
# symbols = ['AAPL', 'TSLA', 'V', 'CRM', 'ABNB']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"

#     # Fetch the data from the API
#     params = {"skip": 0, "limit": 100}
#     response = requests.get(ohlc_endpoint, params=params)
#     response.raise_for_status()  # Raise an exception for bad status codes

#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# final_df = pd.concat(all_data, ignore_index=True)

# final_df.rename(columns ={
#     'timestamp_ms': 'date',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'

# }, inplace=True)


# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'date', 'exchange_id', 'volume', 'high', 'close', 'low', 'open']  # Replace with the columns you want to keep

# # Keep only the specified columns
# final_df = final_df[columns_to_keep]


# final_df['date'] = pd.to_datetime(final_df['date'], unit='ms')
# final_df['date'] = final_df['date'].dt.strftime('%Y%m%d')
# print(final_df)

# # Display the final DataFrame
# print(final_df)

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['AAPL', 'TSLA', 'V', 'CRM', 'ABNB']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# final_df = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_ohlc_statement.rename(columns={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'
# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_ohlc_statement['timestamp'] = pd.to_datetime(df_ohlc_statement['timestamp'], unit='ms')
# df_ohlc_statement['timestamp'] = df_ohlc_statement['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','volume', 'high', 'close', 'low', 'open']
# df_ohlc_statement = df_ohlc_statement[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_ohlc_statement)

# # Loop through the symbols and check the response for each symbol
# for symbol in symbols:
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 100}
#     response = requests.get(ohlc_endpoint, params=params)
#     print(f"Response for {symbol}: {response.status_code}")
#     print(response.json())  # Print the full response for debugging

# """## **DF_AAPL**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['AAPL']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_AAPL = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_AAPL.rename(columns={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'
# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_AAPL['timestamp'] = pd.to_datetime(df_AAPL['timestamp'], unit='ms')
# df_AAPL['timestamp'] = df_AAPL['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','volume', 'high', 'close', 'low', 'open']
# df_AAPL = df_AAPL[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_AAPL)

# """## **df_CRM**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['CRM']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_CRM = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_CRM.rename(columns={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'
# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_CRM['timestamp'] = pd.to_datetime(df_CRM['timestamp'], unit='ms')
# df_CRM['timestamp'] = df_CRM['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','volume', 'high', 'close', 'low', 'open']
# df_CRM = df_CRM[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_CRM)

# """# **df_TSLA**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['TSLA']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_TSLA = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_TSLA.rename(columns={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'
# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_TSLA['timestamp'] = pd.to_datetime(df_TSLA['timestamp'], unit='ms')
# df_TSLA['timestamp'] = df_TSLA['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','volume', 'high', 'close', 'low', 'open']
# df_TSLA = df_TSLA[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_TSLA)

# """## **df_V**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['V']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_V = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_V.rename(columns={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'
# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_V['timestamp'] = pd.to_datetime(df_V['timestamp'], unit='ms')
# df_V['timestamp'] = df_V['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','volume', 'high', 'close', 'low', 'open']
# df_V = df_V[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_V)

# """## **df_ABNB**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['ABNB']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_ABNB = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_ABNB.rename(columns={
#     'timestamp_ms': 'timestamp',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open'
# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_ABNB['timestamp'] = pd.to_datetime(df_ABNB['timestamp'], unit='ms')
# df_ABNB['timestamp'] = df_ABNB['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','volume', 'high', 'close', 'low', 'open']
# df_ABNB = df_ABNB[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_ABNB)

# """## **df_all**"""

# # Store all individual DataFrames in a list
# dfs = [df_AAPL, df_CRM, df_TSLA, df_V, df_ABNB]  # Add other DataFrames as needed

# # Concatenate all DataFrames into one
# df_all = pd.concat(dfs, ignore_index=True)

# # Display the combined DataFrame
# print(df_all)

# """## **df_AAPL_8**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['AAPL']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_AAPL_8 = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_AAPL_8.rename(columns={
#     'timestamp_ms': 'timestamp',

# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_AAPL_8['timestamp'] = pd.to_datetime(df_AAPL_8['timestamp'], unit='ms')
# df_AAPL_8['timestamp'] = df_AAPL_8['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','ADJ_RSI_14', 'ADJ_MACD', 'ADJ_EMA_50', 'ADJ_SMA_50', 'ADJ_ATR_14', 'ADJ_OBV', 'ADJ_VWAP', 'ADJ_CCI_14']
# df_AAPL_8 = df_AAPL_8[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_AAPL_8)

# """## **df_TSLA_8**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['TSLA']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_TSLA_8 = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_TSLA_8.rename(columns={
#     'timestamp_ms': 'timestamp',

# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_TSLA_8['timestamp'] = pd.to_datetime(df_TSLA_8['timestamp'], unit='ms')
# df_TSLA_8['timestamp'] = df_TSLA_8['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','ADJ_RSI_14', 'ADJ_MACD', 'ADJ_EMA_50', 'ADJ_SMA_50', 'ADJ_ATR_14', 'ADJ_OBV', 'ADJ_VWAP', 'ADJ_CCI_14']
# df_TSLA_8 = df_TSLA_8[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_TSLA_8)

# """## **df_CRM_8**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['CRM']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_CRM_8 = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_CRM_8.rename(columns={
#     'timestamp_ms': 'timestamp',

# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_CRM_8['timestamp'] = pd.to_datetime(df_CRM_8['timestamp'], unit='ms')
# df_CRM_8['timestamp'] = df_CRM_8['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','ADJ_RSI_14', 'ADJ_MACD', 'ADJ_EMA_50', 'ADJ_SMA_50', 'ADJ_ATR_14', 'ADJ_OBV', 'ADJ_VWAP', 'ADJ_CCI_14']
# df_CRM_8 = df_CRM_8[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_CRM_8)

# """## **df_V_8**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['V']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_V_8 = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_V_8.rename(columns={
#     'timestamp_ms': 'timestamp',

# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_V_8['timestamp'] = pd.to_datetime(df_V_8['timestamp'], unit='ms')
# df_V_8['timestamp'] = df_V_8['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','ADJ_RSI_14', 'ADJ_MACD', 'ADJ_EMA_50', 'ADJ_SMA_50', 'ADJ_ATR_14', 'ADJ_OBV', 'ADJ_VWAP', 'ADJ_CCI_14']
# df_V_8 = df_V_8[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_V_8)

# """## **df_ABNB_8**"""

# import requests
# import pandas as pd
# #from IPython.display import display

# # Base URL for the API
# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# # List of symbols you want to retrieve data for
# symbols = ['ABNB']  # Add any other symbols you want to include

# # Empty list to store data
# all_data = []

# # Loop through each symbol and fetch the data
# for symbol in symbols:
#     # Construct the endpoint for OHLC data
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     # Fetch the data from the API
#     response = requests.get(ohlc_endpoint, params=params)

#     print(f"Response for {symbol}:{response.status_code}")
#     response.raise_for_status()  # Raise an exception for bad status codes
#     print(response.json())

#     df_symbols = pd.DataFrame(data)
#     # Convert the response JSON to a DataFrame
#     data = response.json()
#     df_ohlc_statement = pd.DataFrame(data)

#     # Add the symbol_id to the DataFrame
#     df_ohlc_statement['symbol_id'] = symbol

#     # Append the data to the all_data list
#     all_data.append(df_ohlc_statement)

# # Concatenate all the DataFrames into one
# df_ABNB_8 = pd.concat(all_data, ignore_index=True)

# # Rename columns to match your desired format
# df_ABNB_8.rename(columns={
#     'timestamp_ms': 'timestamp',

# }, inplace=True)

# # Convert timestamp from milliseconds to datetime and format to yyyymmdd
# df_ABNB_8['timestamp'] = pd.to_datetime(df_ABNB_8['timestamp'], unit='ms')
# df_ABNB_8['timestamp'] = df_ABNB_8['timestamp'].dt.strftime('%Y%m%d')

# # Specify the columns you want to keep
# columns_to_keep = ['symbol_id', 'timestamp','ADJ_RSI_14', 'ADJ_MACD', 'ADJ_EMA_50', 'ADJ_SMA_50', 'ADJ_ATR_14', 'ADJ_OBV', 'ADJ_VWAP', 'ADJ_CCI_14']
# df_ABNB_8 = df_ABNB_8[columns_to_keep]

# # Display the cleaned DataFrame
# print(df_ABNB_8)

# """## **df_all_8**"""

# # Store all individual DataFrames in a list
# dfs = [df_AAPL_8, df_CRM_8, df_TSLA_8, df_V_8, df_ABNB_8]  # Add other DataFrames as needed

# # Concatenate all DataFrames into one
# df_all_8 = pd.concat(dfs, ignore_index=True)

# # Display the combined DataFrame
# print(df_all_8)

# """## Sukush's approach to get the df_all

# """

# import requests
# import pandas as pd

# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# symbols = ['AAPL', 'V', 'ABNB', 'CRM', 'TSLA']
# variables = {}
# df_all = []
# for symbol in symbols:
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     response = requests.get(ohlc_endpoint, params=params)
#     response.raise_for_status()  # Raise an exception for bad status codes
#     variables[f'df_{symbol}'] = pd.DataFrame(response.json())

#     df_all.append(variables[f'df_{symbol}'] )

# df_all = pd.concat(df_all, ignore_index=True)

# #transformation
# df_all.rename(columns={
#     'timestamp_ms': 'date',
#     'adj_high': 'high',
#     'adj_low': 'low',
#     'adj_close': 'close',
#     'adj_open': 'open',
#     'symbol_id': 'symbol'
# }, inplace=True)

# #datetime
# df_all['date'] = pd.to_datetime(df_all['date'], unit='ms').dt.normalize()

# columns_to_keep = ['symbol', 'date','volume', 'high', 'close', 'low', 'open']
# df_all = df_all[columns_to_keep]

# df_all

# import requests
# import pandas as pd

# BASE_URL = "https://api-sntj.grakzjc49jfnj.ap-southeast-2.cs.amazonlightsail.com"

# symbols = ['AAPL', 'V', 'ABNB', 'CRM', 'TSLA']
# variables = {}
# df_all_ta = []
# for symbol in symbols:
#     ohlc_endpoint = f"{BASE_URL}/v0/ohlc/{symbol}"
#     params = {"skip": 0, "limit": 300}

#     response = requests.get(ohlc_endpoint, params=params)
#     response.raise_for_status()  # Raise an exception for bad status codes
#     variables[f'df_{symbol}'] = pd.DataFrame(response.json())

#     df_all_ta.append(variables[f'df_{symbol}'] )

# df_all_ta = pd.concat(df_all_ta, ignore_index=True)

# #transformation
# df_all_ta.rename(columns={
#     'timestamp_ms': 'date',
#     'symbol_id': 'symbol'
# }, inplace=True)

# #datetime
# df_all_ta['date'] = pd.to_datetime(df_all_ta['date'], unit='ms').dt.normalize()

# columns_to_keep = ['symbol', 'date', 'ADJ_RSI_14', 'ADJ_MACD', 'ADJ_EMA_50', 'ADJ_SMA_50', 'ADJ_ATR_14', 'ADJ_OBV', 'ADJ_VWAP', 'ADJ_CCI_14']
# df_all_ta = df_all_ta[columns_to_keep]

# df_all_ta






# import pandas as pd


# df = df_all