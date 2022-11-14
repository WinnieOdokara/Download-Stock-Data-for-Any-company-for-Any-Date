# It would be possible to extract the data using Selenium and 'get element' as well

import requests # To download file with python
from datetime import datetime
import time

# Information the user has to insert
ticker = input("Enter the ticker symble (stock symbol) ")
from_date = input('Enter start date in yyyy/mm/dd format: ')
to_date = input('Enter end date in yyyy/mm/dd format: ')

from_datetime = datetime.strptime(from_date, '%Y/%m/%d')
to_datetime = datetime.strptime(to_date, '%Y/%m/%d')

from_epoch = int(time.mktime(from_datetime.timetuple()))
to_epoch = int(time.mktime(to_datetime.timetuple()))


url = f"https://query1.finance.yahoo.com/v7/finance/download/{ticker}?period1={from_epoch}&period2={to_epoch}&interval=1mo&events=history&includeAdjustedClose=true"

# Impersonates a browser to allow the download of a file by a script
headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36"}

content = requests.get(url, headers=headers).content
print(content)

# Create an empty file to write the data bytes  
with open('data.csv', 'wb') as file: # 'wb': opens a file for writing only in binary format. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.
  file.write(content)
  
# The file is ready for download and to be open on the spreadsheet


#url = f"https://query1.finance.yahoo.com/v7/finance/download/MSFT?period1=511056000&period2=1668384000&interval=1d&events=history&includeAdjustedClose=true

# period1=511056000: time in seconds (timestamp) of the date I wish to start at
# period2=1668384000: timestamp of the date I wish to end at
  # Epoch: to convert the number of seconds passed from a date to another date

# &interval=: d (day), wk (week), mo (month)
  # Ex.: 1m, 5m, 15m, 30m, 90m, 1h, 1d, 5d, 1wk, 1mo, 3mo

  
