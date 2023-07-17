import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import BSpline

############################################################################################# 2009-2013 Cycle using ATH
# Load data
df1H = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2009.csv')
max_close1H = max(df1H['Close'])
df1H['Close'] /= max_close1H

df1H['Date'] = pd.to_datetime(df1H['Date'])
x = df1H['Date'].values.astype(float)

# Fit B-spline
x_smooth1H = np.linspace(x.min(), x.max(), 100)

################################ 2009-2013 Cycle using ATL
# Load data
df1L = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2009.csv')
max_close1L = max(df1L['Close'])
df1L['Close'] /= max_close1L

df1L['Date'] = pd.to_datetime(df1L['Date'])
x = df1L['Date'].values.astype(float)

# Fit B-spline
x_smooth1L = np.linspace(x.min(), x.max(), 100)

############################################################################################# 2013-2017 Cycle using ATH
# Load data
df2H = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2013.csv')
max_close2H = max(df2H['Close'])
df2H['Close'] /= max_close2H

df2H['Date'] = pd.to_datetime(df2H['Date'])
x = df2H['Date'].values.astype(float)

# Fit B-spline
x_smooth2H = np.linspace(x.min(), x.max(), 100)

################################ 2009-2013 Cycle using ATL
# Load data
df2L = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2013.csv')
max_close2L = max(df2L['Close'])
df2L['Close'] /= max_close2L

df2L['Date'] = pd.to_datetime(df2L['Date'])
x = df2L['Date'].values.astype(float)

# Fit B-spline
x_smooth2L = np.linspace(x.min(), x.max(), 100)

############################################################################################# 2017-2021 Cycle using ATH
# Load data
df3H = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2017.csv')
max_close3H = max(df3H['Close'])
df3H['Close'] /= max_close3H

df3H['Date'] = pd.to_datetime(df3H['Date'])
x = df3H['Date'].values.astype(float)

# Fit B-spline
x_smooth3H = np.linspace(x.min(), x.max(), 1000)

################################ 2017-2021 Cycle using ATL
# Load data
df3L = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2017.csv')
max_close3L = max(df3L['Close'])
df3L['Close'] /= max_close3L

df3L['Date'] = pd.to_datetime(df3L['Date'])
x = df3L['Date'].values.astype(float)

# Fit B-spline
x_smooth3L = np.linspace(x.min(), x.max(), 1000)

############################################################################################# 2021-2025 Cycle using ATH
# Load data
df4H = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATH\cycle_2021.csv')
max_close4H = max(df4H['Close'])
df4H['Close'] /= max_close4H

df4H['Date'] = pd.to_datetime(df4H['Date'])
x = df4H['Date'].values.astype(float)

# Fit B-spline
x_smooth4H = np.linspace(x.min(), x.max(), 1000)

################################ 2017-2021 Cycle using ATL
# Load data
df4L = pd.read_csv('!Projects\BTC Algo\Graph\Broken Up Cycles\ATL\cycle_2021.csv')
max_close4L = max(df4L['Close'])
df4L['Close'] /= max_close4L

df4L['Date'] = pd.to_datetime(df4L['Date'])
x = df4L['Date'].values.astype(float)

# Fit B-spline
x_smooth4L = np.linspace(x.min(), x.max(), 1000)

##########################################################################################  PLOT EVERYTHING
# Fit B-spline
k = 3
spline1H = BSpline(df1H['Date'], df1H['Close'], k)
spline1L = BSpline(df1L['Date'], df1L['Close'], k)
spline2H = BSpline(df2H['Date'], df2H['Close'], k)
spline2L = BSpline(df2L['Date'], df2L['Close'], k)
spline3H = BSpline(df3H['Date'], df3H['Close'], k)
spline3L = BSpline(df3L['Date'], df3L['Close'], k)
spline4H = BSpline(df4H['Date'], df4H['Close'], k)
spline4L = BSpline(df4L['Date'], df4L['Close'], k)

# Plot data and B-spline
fig, axs = plt.subplots(figsize=(10,10))
plt.plot(x_smooth1H, spline1H(x_smooth1H), label='B-spline ATH 2009-2013 Cycle')
plt.plot(x_smooth2H, spline2H(x_smooth2H), label='B-spline ATH 2013-2017 Cycle')
plt.plot(x_smooth3H, spline3H(x_smooth3H), label='B-spline ATH 2017-2021 Cycle')
plt.plot(x_smooth4H, spline4H(x_smooth4H), label='B-spline ATH 2021-2025 Cycle')
plt.ylabel('Normalized Close Price')
plt.title('BTC ATH B-Spline Cycle Equations')
plt.legend()

fig, axs = plt.subplots(figsize=(10,10))
plt.plot(x_smooth1L, spline1L(x_smooth1L), label='B-spline ATL 2009-2013 Cycle')
plt.plot(x_smooth2L, spline2L(x_smooth2L), label='B-spline ATL 2013-2017 Cycle')
plt.plot(x_smooth3L, spline3L(x_smooth3L), label='B-spline ATL 2017-2021 Cycle')
plt.plot(x_smooth4L, spline4L(x_smooth4L), label='B-spline ATL 2021-2025 Cycle')
plt.ylabel('Normalized Close Price')
plt.title('BTC ATL B-Spline Cycle Equations')

############################################################################################################################################################## Spline Analysis
# Obtain B-spline coefficients for each spline
coeffs1H = spline1H.c
coeffs1L = spline1L.c
coeffs2H = spline2H.c
coeffs2L = spline2L.c
coeffs3H = spline3H.c
coeffs3L = spline3L.c
coeffs4H = spline4H.c
coeffs4L = spline4L.c


# define a list of tuples with coefficient arrays and cycle year ranges
coeffs_list1 = [(coeffs1H, '2009-2013', 'ATH'), (coeffs2H, '2013-2017', 'ATH'),
               (coeffs3H, '2017-2021', 'ATH'), (coeffs4H, '2021-2025', 'ATH')]

# loop through the list and compare the coefficients using the Euclidean distance
for i in range(len(coeffs_list1)):
    for j in range(i+1, len(coeffs_list1)):
        # find the length of the longer coefficient array
        max_len = max(len(coeffs_list1[i][0]), len(coeffs_list1[j][0]))

        # create new arrays with zeros for missing points
        new_coeffs_i = np.zeros(max_len)
        new_coeffs_j = np.zeros(max_len)

        # copy the original coefficients to the new arrays
        new_coeffs_i[:len(coeffs_list1[i][0])] = coeffs_list1[i][0]
        new_coeffs_j[:len(coeffs_list1[j][0])] = coeffs_list1[j][0]

        # compare the coefficients using the Euclidean distance
        distance = round(np.linalg.norm(new_coeffs_i - new_coeffs_j), 2)

        # print the distance
        print(f"Euclidean distance between {coeffs_list1[i][1]} Cycle ({coeffs_list1[i][2]}) and {coeffs_list1[j][1]} Cycle ({coeffs_list1[j][2]}): {distance}")

# define a list of tuples with coefficient arrays and cycle year ranges
coeffs_list2 = [(coeffs1L, '2009-2013', 'ATL'), (coeffs2L, '2013-2017', 'ATL'),
               (coeffs3L, '2017-2021', 'ATL'), (coeffs4L, '2021-2025', 'ATL')]

# loop through the list and compare the coefficients using the Euclidean distance
for i in range(len(coeffs_list2)):
    for j in range(i+1, len(coeffs_list2)):
        # find the length of the longer coefficient array
        max_len = max(len(coeffs_list2[i][0]), len(coeffs_list2[j][0]))

        # create new arrays with zeros for missing points
        new_coeffs_i = np.zeros(max_len)
        new_coeffs_j = np.zeros(max_len)

        # copy the original coefficients to the new arrays
        new_coeffs_i[:len(coeffs_list2[i][0])] = coeffs_list2[i][0]
        new_coeffs_j[:len(coeffs_list2[j][0])] = coeffs_list2[j][0]

        # compare the coefficients using the Euclidean distance
        distance = round(np.linalg.norm(new_coeffs_i - new_coeffs_j), 2)

        # print the distance
        print(f"Euclidean distance between {coeffs_list2[i][1]} Cycle ({coeffs_list2[i][2]}) and {coeffs_list2[j][1]} Cycle ({coeffs_list2[j][2]}): {distance}")

plt.legend()
plt.show()