'''
This program grabs data from bitfinex's ticker, displays the data, and refreshes every minute.
Written by Ian Schwartz
'''
import os
import sys
import json
import time
import requests

'''
NOTE: As is, this program uses the public API. For actual trading, it would
need to use the Authenticated API, which is beyond the scope of this program.
'''

url = "https://api.bitfinex.com/v2/ticker/tBTCUSD/"

response = requests.request("GET", url) #Get the data
txt = response.text #We're only interested in the text area of the response (returns as string type)
jtxt = json.loads(txt) #convert into an array of strings

'''
jtxt now looks like:
[47527, 9.49607463, 47528, 16.426778170000002, -661, -0.0137, 47528, 10274.45975602, 48583, 45851.95356552]

According to the documentation, it goes:
BID, BID_SIZE, ASK, ASK_SIZE, DAILY_CHANGE, DAILY_CHANGE_RELATIVE, LAST_PRICE, VOLUME, HIGH, LOW
'''

BID = jtxt[0]
BID_SIZE = jtxt[1]
ASK = jtxt[2]
ASK_SIZE = jtxt[3]
DAILY_CHANGE = jtxt[4]
DAILY_CHANGE_RELATIVE = jtxt[5]
LAST_PRICE = jtxt[6]
VOLUME = jtxt[7]
HIGH = jtxt[8]
LOW = jtxt[9]

#Print the initial data to console
print("Current Data of BTC to USD\n" +
    "\nBid:\t\t\t" + str(BID) + 
    "\nBid Size:\t\t" + str(BID_SIZE) +
    "\nAsk:\t\t\t" + str(ASK) +
    "\nAsk Size:\t\t" + str(ASK_SIZE) +
    "\nDaily Change:\t\t" + str(DAILY_CHANGE) + 
    "\nDaily Change Relative:\t" + str(DAILY_CHANGE_RELATIVE) + 
    "\nLast Price:\t\t" + str(LAST_PRICE) +
    "\nVolume:\t\t\t" + str(VOLUME) + 
    "\nHigh:\t\t\t" + str(HIGH) + 
    "\nLow:\t\t\t" + str(LOW) + 
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
        
        BID = jtxt[0]
        BID_SIZE = jtxt[1]
        ASK = jtxt[2]
        ASK_SIZE = jtxt[3]
        DAILY_CHANGE = jtxt[4]
        DAILY_CHANGE_RELATIVE = jtxt[5]
        LAST_PRICE = jtxt[6]
        VOLUME = jtxt[7]
        HIGH = jtxt[8]
        LOW = jtxt[9]

        #Print the initial data to console
        print("Current Data of BTC to USD\n" +
            "\nBid:\t\t\t" + str(BID) + 
            "\nBid Size:\t\t" + str(BID_SIZE) +
            "\nAsk:\t\t\t" + str(ASK) +
            "\nAsk Size:\t\t" + str(ASK_SIZE) +
            "\nDaily Change:\t\t" + str(DAILY_CHANGE) + 
            "\nDaily Change Relative:\t" + str(DAILY_CHANGE_RELATIVE) + 
            "\nLast Price:\t\t" + str(LAST_PRICE) +
            "\nVolume:\t\t\t" + str(VOLUME) + 
            "\nHigh:\t\t\t" + str(HIGH) + 
            "\nLow:\t\t\t" + str(LOW) + 
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
