import pandas as pd
import json
import csv

# Load CSV file into a Pandas DataFrame
df1 = pd.read_csv('!Projects\BTC Algo\Data\Algo\Gold Price.csv')

# Remove the first row of the DataFrame
df1 = df1.iloc[1:]

# Remove any $, "" and commas from all columns
df1 = df1.replace({'$': '', ',': '', '"': '', ' ': ''}, regex=True)

# Replace any #N/A with the previous row's value
df1 = df1.fillna(method='ffill')

df1.to_csv('!Projects\BTC Algo\Algo\Refined Data\cleaned_gold.csv', index=False)

#####################################################################################################################################

# Load CSV file into a Pandas DataFrame
df2 = pd.read_csv('!Projects\BTC Algo\Data\Algo\Oil.csv', skiprows=4)

# Remove any $, "" and commas from all columns
df2 = df2.replace({'$': '', ',': '', '"': '', ' ': ''}, regex=True)

# Replace any #N/A with the previous row's value
df2 = df2.fillna(method='ffill')

df2.to_csv('!Projects\BTC Algo\Algo\Refined Data\cleaned_oil.csv', index=False)
#####################################################################################################################################
# load the json file
with open('!Projects\\BTC Algo\\Data\Algo\\total-bitcoins.json', 'r') as f:
    data = json.load(f)

# extract the data and convert to a DataFrame
df = pd.DataFrame(data['total-bitcoins'])
df['date'] = pd.to_datetime(df['x'], unit='ms')  # convert the x to a date
df['supply'] = df['y']  # extract the number next to "y"

# select only the date and supply columns
df = df[['date', 'supply']]

df['date'] = df['date'].astype(str)
df['date'] = df['date'].str.split(' ').str[0]
df['daily_increase'] = df['supply'].diff().fillna(0)

# save the DataFrame as a csv file
df.to_csv('!Projects\BTC Algo\Algo\Refined Data\BTC_supply.csv', index=False)

Supplydf = pd.read_csv('!Projects\BTC Algo\Algo\Refined Data\BTC_supply.csv', parse_dates=['date'], index_col='date', usecols=['date', 'daily_increase'])

#####################################################################################################################################
# create a range of dates from 2022-01-01 to 2022-12-31
date_range = pd.date_range(start='2010-07-17', end='2023-03-29', freq='D')

# create a dataframe with the date_range as its index
df = pd.DataFrame(index=date_range)

# read in the Bitcoin data
bitcoin_df = pd.read_csv('!Projects\BTC Algo\Data\Other\ImportBTCData.csv', parse_dates=['Date'], index_col='Date', usecols=['Date', 'Close'])

# read in the oil data
oil_df = pd.read_csv('!Projects\BTC Algo\Algo\Refined Data\cleaned_oil.csv', parse_dates=['Day'], index_col='Day')
oil_df = oil_df.rename(columns={'Cushing OK WTI Spot Price FOB  Dollars per Barrel': 'Oil Close'})

# read in the gold data
gold_df = pd.read_csv('!Projects\BTC Algo\Algo\Refined Data\cleaned_gold.csv', parse_dates=[' Date '], index_col=' Date ',usecols=[' Date ', 'Close'])
gold_df = gold_df.rename(columns={'Close': 'Gold Close'})

# concatenate the Bitcoin, oil, and gold dataframes into a single dataframe
dataframes = [bitcoin_df, oil_df, gold_df, Supplydf]
merged_df = pd.concat(dataframes, axis=1, join='outer')

# join the merged_df with the main df using the dates as the index
df = df.join(merged_df)
df['Oil Close'].fillna(method='ffill', inplace=True)
df['Gold Close'].fillna(method='ffill', inplace=True)
df['daily_increase'].fillna(method='ffill', inplace=True)

# save the final dataframe to a CSV file
df.to_csv('!Projects\BTC Algo\Algo\Refined Data\Merged_prices.csv')
