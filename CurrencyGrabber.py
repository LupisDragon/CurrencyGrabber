'''
This program grabs data from bitfinex's ticker, displays the data, and refreshes every minute.
Written by Ian Schwartz
Modified to grab price candles by E. A.   3/12/21
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
candlewidth=["1m","5m","15m","30m","1h","3h","4h","6h","12h"]

for k in candlewidth: #goes through each value in the list 'candlewidth' and assigns it to k
    url = "https://api.bitfinex.com/v2/candles/trade:"
    url += k
    url += ":tBTCUSD/hist"
    #url = "https://api.bitfinex.com/v2/candles/trade:1m:tBTCUSD/hist"
    #url = "https://api.bitfinex.com/v2/ticker/tBTCUSD/"

    response = requests.request("GET", url) #Get the data
    txt = response.text #We're only interested in the text area of the response (returns as string type)
    jtxt = json.loads(txt) #convert into an array of strings
    
    '''
    jtxt now looks like:

    [1615561200000,56226,56477,56552,56052,128.22140116],
    [1615557600000,55733,56226,56243.85613651,55430,308.3953228],
    [1615554000000,56435,55734,56436,55183,1491.00838938],
    [1615550400000,56521,56435,56869,56248.82739558,183.76572076],
    [1615546800000,56769.4646076,56507.96157496,57094,56413,313.76806297],
    [1615543200000,56540,56770,56927,55860,802.222184],
    etc

    I assume that means time, open, close,high, low, volume
    '''

    #Print data to file
    filename="xxx"+k+".txt"
    try:
        my_data_file = open(filename, 'a')
    #    findlastentre = my_data_file.read()   
    
    #do something with this later to know when to append the update
        startpoint = 117  #later on we will figure out the starpoint
    except IOError:
        my_data_file = open(filename, 'w')
        startpoint = 0
  
 
    '''
    Ian's Notes: this next sextion uses a "start point" and "end point" for the file (I'm guessing so it can overwrite the file later on?
    Honestly, I don't understand the logic of it, but I'm including it in here because I fixed the file output that E.A. wrote.
    '''
    #Print to file - oldest 1st    (eventually we will have it only print new data but reading last time stamp & only printing after)
    for i in range(startpoint,120):
    # don't really need these anymore but here they are for referance:
    #    TIME = jtxt[119-i][0]
    #    OPEN = jtxt[119-i][1]
    #    CLOSE = jtxt[119-i][2]
    #    HIGH = jtxt[119-i][3]
    #    LOW = jtxt[119-i][4]
    #    VOLUME = jtxt[119-i][5]
       my_data_file.write( "\n"+str(jtxt[119-i][0]) 
              +"\t"+str(jtxt[119-i][1])
              +"\t"+str(jtxt[119-i][3])
              +"\t"+str(jtxt[119-i][4])
              +"\t"+str(jtxt[119-i][2])
              +"\t"+str(jtxt[119-i][5])
        )

    my_data_file.close()
    
#END OF PROGRAM
