import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import pandas as pd
import csv

# URL of the webpage to scrape
url = "https://coincodex.com/crypto/bitcoin/historical-data/"

# Get the date of yesterday
yesterday = datetime.now().date() - timedelta(days=1)

# Convert the date to a string with the format "MMM DD, YYYY"
date_str = yesterday.strftime("%b %d, %Y")

# Make a GET request to the webpage
response = requests.get(url)

# Pause for 5 seconds
time.sleep(2)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all table cells with class "text-right"
value_cells = soup.find_all("td", class_="text-right")

# Get the 2nd value cell
value_cell = value_cells[2]

# Extract the value as a string
value_str = value_cell.get_text(strip=True)

# Convert the value string to a float (assuming it's a numeric value)
value = float(value_str.replace("$", "").replace(",", ""))

# Print the value
print(value)

# Read in the CSV file
df = pd.read_csv('input_file.csv')

# Reverse the order of the rowsimport requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta
import time
import csv

# URL of the webpage to scrape
url = "https://coincodex.com/crypto/bitcoin/historical-data/"

# Get the date of yesterday
yesterday = datetime.now().date() - timedelta(days=1)

# Convert the date to a string with the format "MMM DD, YYYY"
date_str = yesterday.strftime("%b %d, %Y")

# Make a GET request to the webpage
response = requests.get(url)

# Pause for 2 seconds
time.sleep(2)

# Parse the HTML content using Beautiful Soup
soup = BeautifulSoup(response.content, "html.parser")

# Find all table cells with class "text-right"
value_cells = soup.find_all("td", class_="text-right")

# Get the 2nd value cell
value_cell = value_cells[2]

# Extract the value as a string
value_str = value_cell.get_text(strip=True)

# Convert the value string to a float (assuming it's a numeric value)
value = float(value_str.replace("$", "").replace(",", ""))

# Print the value
print(value)

# Open the CSV file and read the data into a list
with open('D:\Coding\!Projects\BTC Algo\Data\ImportBTCData.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    rows = list(reader)

# Reverse the order of the rows
rows.reverse()

# Insert the new data at the end of the list
new_row = [date_str, '', '', '', value]
rows.append(new_row)

# Write the updated rows to the CSV file
with open('D:\Coding\!Projects\BTC Algo\Data\ImportBTCData.csv', mode='w', newline='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(rows)
df = df.iloc[::-1]

date_str = yesterday.strftime('%Y-%m-%d')
date_obj = datetime.strptime(date_str, '%Y-%m-%d')
new_date_str = datetime.strftime(date_obj, '%b-%d-%Y')
