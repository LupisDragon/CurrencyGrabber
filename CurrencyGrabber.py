'''
This program grabs data from bitfinex's ticker, displays the data, and refreshes every minute.
Written by Ian Schwartz

gui option: http://atlastk.org/api
NOTE: The GUI also needs installing (pip install atlastk)
'''

import requests #needs manual install (pip install requests)
import time
import json

url = "https://api.bitfinex.com/v1/pubticker/btcusd" #This MAY need moving in the future, but for right now, this is all we're concerned with (BTC to USD)

response = requests.request("GET", url) #Get the data
txt = response.text #We're only interested in the text area of the response (returns as string type)
'''
Format: '{"mid":"11831.5","bid":"11831.0","ask":"11832.0","last_price":"11834.0",
"low":"11038.0","high":"12065.0","volume":"21643.99217458751402","timestamp":"1562250150.539342"}'
'''
jtxt = json.loads(txt) #convert into an array of strings
'''
Format: {'mid': '11831.5', 'bid': '11831.0', 'ask': '11832.0', 'last_price': '11834.0', 
'low': '11038.0', 'high': '12065.0', 'volume': '21643.99217458751402', 'timestamp': '1562250150.539342'}
'''

#For now, we'll print to the console, later to a GUI
print("Current Data of BTC to USD\n\nLow:\t\t" + jtxt['low'] + 
    "\nMid:\t\t" + jtxt['mid'] +
    "\nHigh:\t\t" + jtxt['high'] +
    "\nLast Price:\t" + jtxt['last_price'] +
    "\nBid:\t\t" + jtxt['bid'] +
    "\nAsk:\t\t" + jtxt['ask'] +
    "\nVolume:\t\t" + jtxt['volume'] +
    "\nTimestamp:\t" + jtxt['timestamp'] +
    "\n"
    )

currenttime = time.localtime()
lasttime = currenttime #lasttime represents the last time the data was updated
hr = lasttime.tm_hour #for AM/PM display purposes. Otherwise, generally useless.
minute = lasttime.tm_min #this makes it easier to see when the data needs refreshing
ender = "" # 0(midnight) - 11: AM, 12-23: PM

#For display purposes, is it AM or PM?
if (hr > 12):
    ender = "PM"
    hr -= 12
elif (hr == 12):
    ender = "PM"
else:
    ender = "AM"

#For display purposes, do we need to add a leading zero to the minute? (needed when minute is 0-9)
if (minute < 10):
    print("Last Update: " + str(hr) + ":0" + str(lasttime.tm_min) + " " + ender)
else:
    print("Last Update: " + str(hr) + ":" + str(lasttime.tm_min) + " " + ender)

while True:
    currenttime = time.localtime()
    minute = currenttime.tm_min
    
    if ((currenttime.tm_min > lasttime.tm_min) or (currenttime.tm_min == 0 and lasttime.tm_min == 59)): #data needs updating
        response = requests.request("GET", url)
        txt = response.text
        jtxt = json.loads(txt)
        
        print("\nCurrent Data of BTC to USD\n\nLow:\t\t" + jtxt['low'] + 
            "\nMid:\t\t" + jtxt['mid'] +
            "\nHigh:\t\t" + jtxt['high'] +
            "\nLast Price:\t" + jtxt['last_price'] +
            "\nBid:\t\t" + jtxt['bid'] +
            "\nAsk:\t\t" + jtxt['ask'] +
            "\nVolume:\t\t" + jtxt['volume'] +
            "\nTimestamp:\t" + jtxt['timestamp'] +
            "\n"
            )
        
        lasttime = currenttime
        hr = currenttime.tm_hour

        if (hr > 12):
            ender = "PM"
            hr -= 12
        elif (hr == 12):
            ender = "PM"
        else:
            ender = "AM"

        if (minute < 10):
            print("Last Update: " + str(hr) + ":0" + str(lasttime.tm_min) + " " + ender)
        else:
            print("Last Update: " + str(hr) + ":" + str(lasttime.tm_min) + " " + ender)
print ("Done")