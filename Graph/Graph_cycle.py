import pandas as pd
import matplotlib.pyplot as plt

# Read the four CSV files into pandas dataframes
df1 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATH/cycle_2009.csv')
df2 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATH/cycle_2013.csv')
df3 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATH/cycle_2017.csv')
df4 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATH/cycle_2021.csv')

x = 5 ## Dates that can be shown

# Create a figure and four subplots for each cycle
fig, axs = plt.subplots(nrows=4, figsize=(10,10))

# add a title to the figure
fig.suptitle('Price History of Bitcoin over multiple cycles (ATH to ATH)')

################################################################################################ Plot the 7-day moving average for each cycle on a separate subplot
axs[0].plot(df1['Date'], df1['Close'].rolling(window=1).mean())
axs[0].set_title('2009-2013 Cycle')
axs[0].axvline(df1.index[200], color = "gray")  # Vertical line at row 100
axs[0].axvline(df1.index[400], color = "red")
axs[0].axvline(df1.index[600], color = "gray")
axs[0].axvline(df1.index[1000], color = "green")
axs[0].axvline(df1.index[1100], color = "blue")
axs[0].set_xticks([])
axs[0].set_xticks(range(0, len(df1), len(df1)//x))

axs[1].plot(df2['Date'], df2['Close'].rolling(window=1).mean())
axs[1].set_title('2013-2017 Cycle')
axs[1].axvline(df2.index[200], color = "gray")  # Vertical line at row 100
axs[1].axvline(df2.index[400], color = "red")
axs[1].axvline(df2.index[600], color = "gray")
axs[1].axvline(df2.index[1000], color = "green")
axs[1].axvline(df2.index[1100], color = "blue")
axs[1].set_xticks([])
axs[1].set_xticks(range(0, len(df2), len(df2)//x))

axs[2].plot(df3['Date'], df3['Close'].rolling(window=1).mean())
axs[2].set_title('2017-2021 Cycle')
axs[2].axvline(df3.index[200], color = "gray")  # Vertical line at row 100
axs[2].axvline(df3.index[400], color = "red")
axs[2].axvline(df3.index[600], color = "gray")
axs[2].axvline(df3.index[1000], color = "green")
axs[2].axvline(df3.index[1100], color = "blue")
axs[2].set_xticks([])
axs[2].set_xticks(range(0, len(df3), len(df3)//x))

axs[3].plot(df4['Date'], df4['Close'].rolling(window=1).mean())
axs[3].set_title('2021-2025 Cycle')
axs[3].axvline(df4.index[200], color = "gray")  # Vertical line at row 100
axs[3].axvline(df4.index[400], color = "red")
#axs[3].axvline(df4.index[600], color = "gray")
axs[3].set_xticks([])
axs[3].set_xticks(range(0, len(df4), len(df4)//x))

# Set y-axis limits for each subplot
for ax in axs:
    ax.set_yscale('log')
    ax.set_ylabel('Price ($)')

fig.subplots_adjust(hspace=0.443)
fig.subplots_adjust(top=0.917)
fig.subplots_adjust(left=0.076)
fig.subplots_adjust(bottom=0.067)
fig.subplots_adjust(right=0.974)

########################################################################################### Compute the ROI for each cycle, If invested from the ATH
cycle_roi1 = []
first_price = df1.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi1 = ((df1['Close'] - first_price) / first_price)*100
cycle_roi1.append(roi1)

cycle_roi2 = []
first_price = df2.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi2 = ((df2['Close'] - first_price) / first_price)*100
cycle_roi2.append(roi2)

cycle_roi3 = []
first_price = df3.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi3 = ((df3['Close'] - first_price) / first_price)*100
cycle_roi3.append(roi3)

cycle_roi4 = []
first_price = df4.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi4= ((df4['Close'] - first_price) / first_price)*100
cycle_roi4.append(roi4)

########################################################################################################### Create a scatterplot with 4 subplots for the ROI History from ATH
fig, axs = plt.subplots(2, 2)

# add a title to the figure
fig.suptitle('ROI History of Bitcoin over multiple cycles (ATH to ATH)')

# Create scatter plot 1
axs[0, 0].scatter(df1['Date'], cycle_roi1, s=25, alpha=0.5, color = "gray")
axs[0, 0].set_title('2009-2013 Cycle')
axs[0, 0].set_xticks([])
axs[0, 0].axvline(df2.index[200], color = "gray")  # Vertical line at row 100
axs[0, 0].axvline(df2.index[400], color = "red")
axs[0, 0].axvline(df2.index[600], color = "gray")
axs[0, 0].axvline(df2.index[1000], color = "green")
axs[0, 0].axvline(df2.index[1100], color = "blue")
axs[0, 0].set_xticks([])
axs[0, 0].set_xticks(range(0, len(df1), len(df1)//x))


# Create scatter plot 2
axs[0, 1].scatter(df2['Date'], cycle_roi2, s=25, alpha=0.5, color = "gray")
axs[0, 1].set_title('2013-2017 Cycle')
axs[0, 1].set_xticks([])
axs[0, 1].axvline(df2.index[200], color = "gray")  # Vertical line at row 100
axs[0, 1].axvline(df2.index[400], color = "red")
axs[0, 1].axvline(df2.index[600], color = "gray")
axs[0, 1].axvline(df2.index[1000], color = "green")
axs[0, 1].axvline(df2.index[1100], color = "blue")
axs[0, 1].set_xticks([])
axs[0, 1].set_xticks(range(0, len(df2), len(df2)//x))

# Create scatter plot 3
axs[1, 0].scatter(df3['Date'], cycle_roi3, s=25, alpha=0.5, color = "gray")
axs[1, 0].set_title('2017-2021 Cycle')
axs[1, 0].set_xticks([])
axs[1, 0].axvline(df2.index[200], color = "gray")  # Vertical line at row 100
axs[1, 0].axvline(df2.index[400], color = "red")
axs[1, 0].axvline(df2.index[600], color = "gray")
axs[1, 0].axvline(df2.index[1000], color = "green")
axs[1, 0].axvline(df2.index[1100], color = "blue")
axs[1, 0].set_xticks([])
axs[1, 0].set_xticks(range(0, len(df3), len(df3)//x))

# Create scatter plot 4
axs[1, 1].scatter(df4['Date'], cycle_roi4, s=25, alpha=0.5, color = "gray")
axs[1, 1].set_title('2021-2025 Cycle')
axs[1, 1].set_xticks([])
axs[1, 1].axvline(df2.index[200], color = "gray")  # Vertical line at row 100
axs[1, 1].axvline(df2.index[400], color = "red")
axs[1, 1].axvline(df2.index[600], color = "gray")
axs[1, 1].axvline(df2.index[1000], color = "green")
axs[1, 1].axvline(df2.index[1100], color = "blue")
axs[1, 1].set_xticks([])
axs[1, 1].set_xticks(range(0, len(df4), len(df4)//x))

fig.subplots_adjust(hspace=0.4)
fig.subplots_adjust(top=0.85)
fig.subplots_adjust(wspace=0.088)
fig.subplots_adjust(left=0.05)
fig.subplots_adjust(bottom=0.08)
fig.subplots_adjust(right=0.95)


########################################################################################### Compute the ROI for each cycle, If invested from the ATL
###########################################################################################################
# Read the four CSV files into pandas dataframes
df11 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATL/cycle_2009.csv')
df21 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATL/cycle_2013.csv')
df31 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATL/cycle_2017.csv')
df41 = pd.read_csv('!Projects/BTC Algo/Graph/Broken Up Cycles/ATL/cycle_2021.csv')



# Create a figure and four subplots for each cycle
fig, axs = plt.subplots(nrows=4, figsize=(10,10))

# add a title to the figure
fig.suptitle('Price History of Bitcoin over multiple cycles (ATL to ATL)')

################################################################################################ Plot the 7-day moving average for each cycle on a separate subplot
axs[0].plot(df11['Date'], df11['Close'].rolling(window=1).mean())
axs[0].set_title('2009-2013 Cycle')
axs[0].axvline(df11.index[200], color = "gray")  # Vertical line at row 100
axs[0].axvline(df11.index[400], color = "red")
axs[0].axvline(df11.index[600], color = "gray")
axs[0].axvline(df11.index[1000], color = "green")
axs[0].axvline(df11.index[1100], color = "blue")
axs[0].set_xticks([])
axs[0].set_xticks(range(0, len(df11), len(df11)//x))

axs[1].plot(df21['Date'], df21['Close'].rolling(window=1).mean())
axs[1].set_title('2013-2017 Cycle')
axs[1].axvline(df21.index[200], color = "gray")  # Vertical line at row 100
axs[1].axvline(df21.index[400], color = "red")
axs[1].axvline(df21.index[600], color = "gray")
axs[1].axvline(df21.index[1000], color = "green")
axs[1].axvline(df21.index[1100], color = "blue")
axs[1].set_xticks([])
axs[1].set_xticks(range(0, len(df21), len(df21)//x))

axs[2].plot(df31['Date'], df31['Close'].rolling(window=1).mean())
axs[2].set_title('2017-2021 Cycle')
axs[2].axvline(df31.index[200], color = "gray")  # Vertical line at row 100
axs[2].axvline(df31.index[400], color = "red")
axs[2].axvline(df31.index[600], color = "gray")
axs[2].axvline(df31.index[1000], color = "green")
axs[2].axvline(df31.index[1100], color = "blue")
axs[2].set_xticks([])
axs[2].set_xticks(range(0, len(df31), len(df31)//x))

axs[3].plot(df41['Date'], df41['Close'].rolling(window=1).mean())
axs[3].set_title('2021-2025 Cycle')
#axs[3].axvline(df41.index[200], color = "gray")  # Vertical line at row 100
#axs[3].axvline(df41.index[400], color = "red")
#axs[3].axvline(df41.index[600], color = "gray") bnot there yet
axs[3].set_xticks([])
axs[3].set_xticks(range(0, len(df41), len(df41)//x))

# Set y-axis limits for each subplot
for ax in axs:
    ax.set_yscale('log')
    ax.set_ylabel('Price ($)')

fig.subplots_adjust(hspace=0.443)
fig.subplots_adjust(top=0.917)
fig.subplots_adjust(left=0.076)
fig.subplots_adjust(bottom=0.067)
fig.subplots_adjust(right=0.974)

#####################################################################################

cycle_roi11 = []
first_price = df11.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi11 = ((df11['Close'] - first_price) / first_price)*100
cycle_roi11.append(roi11)

cycle_roi21 = []
first_price = df21.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi21 = ((df21['Close'] - first_price) / first_price)*100
cycle_roi21.append(roi21)

cycle_roi31 = []
first_price = df31.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi31 = ((df31['Close'] - first_price) / first_price)*100
cycle_roi31.append(roi31)

cycle_roi41 = []
first_price = df41.iloc[0]['Close']
# Compute the ROI of all other data points relative to the first price
roi41 = ((df41['Close'] - first_price) / first_price)*100
cycle_roi41.append(roi41)

########################################################################################################### Create a scatterplot with 4 subplots for the ROI History from ATH
fig, axs = plt.subplots(2, 2)

# add a title to the figure
fig.suptitle('ROI History of Bitcoin over multiple cycles (ATL to ATL)')

# Create scatter plot 1
axs[0, 0].scatter(df11['Date'], cycle_roi11, s=25, alpha=0.5, color = "gray")
axs[0, 0].set_title('2009-2013 Cycle')
axs[0, 0].set_xticks([])
axs[0, 0].axvline(df11.index[200], color = "gray")  # Vertical line at row 100
axs[0, 0].axvline(df11.index[400], color = "red")
axs[0, 0].axvline(df11.index[600], color = "gray")
axs[0, 0].axvline(df11.index[1000], color = "green")
axs[0, 0].axvline(df11.index[1100], color = "blue")


# Create scatter plot 2
axs[0, 1].scatter(df21['Date'], cycle_roi21, s=25, alpha=0.5, color = "gray")
axs[0, 1].set_title('2013-2017 Cycle')
axs[0, 1].set_xticks([])
axs[0, 1].axvline(df21.index[200], color = "gray")  # Vertical line at row 100
axs[0, 1].axvline(df21.index[400], color = "red")
axs[0, 1].axvline(df21.index[600], color = "gray")
axs[0, 1].axvline(df21.index[1000], color = "green")
axs[0, 1].axvline(df21.index[1100], color = "blue")

# Create scatter plot 3
axs[1, 0].scatter(df31['Date'], cycle_roi31, s=25, alpha=0.5, color = "gray")
axs[1, 0].set_title('2017-2021 Cycle')
axs[1, 0].set_xticks([])
axs[1, 0].axvline(df31.index[200], color = "gray")  # Vertical line at row 100
axs[1, 0].axvline(df31.index[400], color = "red")
axs[1, 0].axvline(df31.index[600], color = "gray")
axs[1, 0].axvline(df31.index[1000], color = "green")
axs[1, 0].axvline(df31.index[1100], color = "blue")

# Create scatter plot 4
axs[1, 1].scatter(df41['Date'], cycle_roi41, s=25, alpha=0.5, color = "gray")
axs[1, 1].set_title('2021-2025 Cycle')
axs[1, 1].set_xticks([])
axs[1, 1].axvline(df21.index[200], color = "gray")  # Vertical line at row 100
axs[1, 1].axvline(df21.index[400], color = "red")
axs[1, 1].axvline(df21.index[600], color = "gray")
axs[1, 1].axvline(df2.index[1000], color = "green")
axs[1, 1].axvline(df2.index[1100], color = "blue")

# Adjust layout
plt.tight_layout()

plt.show()