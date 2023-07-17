import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import math

# Load CSV file into a Pandas DataFrame
dfALL = pd.read_csv('!Projects\BTC Algo\Algo\Refined Data\Merged_prices.csv')
dfALL = dfALL.fillna(0)

dfALL['Gold Close'] = dfALL['Gold Close'].str.replace('$', '', regex=False).astype(float)
dfALL['Oil Close'] = dfALL['Oil Close'].astype(float)
dfALL['Close'] = dfALL['Close'].astype(float)
dfALL['daily_increase'] = dfALL['daily_increase'].astype(float)

print(dfALL)

BTC_Price = dfALL.iloc[:, 1]
Oil_Price = dfALL.iloc[:, 2]
Gold_Price = dfALL.iloc[:, 3]
Output_Price = dfALL.iloc[:, 4]

CoOut = 0.22
CoG = -1.63
CoOil = -2.93
#CoNews = 0.86

# Create an empty list to store the results
BTC_ALGO_PRICES = []

# Loop through the rows in the DataFrame
for index, row in dfALL.iterrows():
    # Get the values of the output, gold, and oil prices for this row
    Output_Price = row['daily_increase']
    Gold_Price = row['Gold Close']
    Oil_Price = row['Oil Close']

    # Calculate the logarithms of the output, gold, and oil prices
    log_Output = np.log(Output_Price)
    log_Gold = np.log(Gold_Price)
    log_Oil = np.log(Oil_Price)

    # Calculate the BTC_ALGO_PRICE using the logarithmic values
    BTC_ALGO_PRICE = BTC_Price + CoOut * log_Output + CoG * log_Gold + CoOil * log_Oil

    # Append the result to the list
    BTC_ALGO_PRICES.append(BTC_ALGO_PRICE)

# Print out the list of BTC_ALGO_PRICES
#print(BTC_ALGO_PRICES)



# create a new DataFrame with Date and BTC_ALGO_PRICE columns
df = pd.DataFrame({'Date': dfALL.iloc[:, 0], 'BTC_ALGO_PRICE': BTC_ALGO_PRICE})

# Create a new column in the DataFrame with the predicted prices shifted by one day
df['Predicted_Price'] = df['BTC_ALGO_PRICE'].shift(-1)

# Plot the actual BTC price and the predicted prices
fig, ax = plt.subplots()
ax.plot(dfALL.iloc[:, 0], dfALL['Close'], label='Actual BTC Price')
ax.plot(df.iloc[:-1, 0], df['Predicted_Price'][:-1], label='Predicted Price')
ax.legend()

# Set the axis labels and title
ax.set_xlabel('Date')
ax.set_ylabel('Price')
ax.set_title('BTC Prediction Using Algorithm')

plt.show()
