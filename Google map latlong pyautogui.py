import webbrowser
import pyautogui
import pyperclip

import random
from time import sleep as wait
import csv

pyautogui.FAILSAFE = True

# scripts referenced from:
# https://stackoverflow.com/questions/38574629/webbrowser-not-opening-new-windows
# https://github.com/wmcooper2/google-maps-transit-fares/blob/master/googlemaps.py
# https://www.pythontutorial.net/python-basics/python-write-csv-file/

# ***Use as your own risk! Not sure if google map will block your ip if search too often at a time***

# check your mouse position
# pyautogui.mouseInfo()

# open a chrome window first before running the code

# get geodata from redirected google map url after you performed a search
def geodata(location):
    
        list = []
        list.append(location)
        
        #randomize wait time before each search
        time_delay=random.uniform(0.1,0.5)        
        wait(5 + time_delay)
        
        # perform a search of the location in the list
        webbrowser.open("https://www.google.com/maps/search/"+location)

        # customize to your screen, make sure the arrow lands somewhere on the url
        pyautogui.moveTo(1280, 70) 
        pyautogui.click()
        wait(1)
        pyautogui.click()
        
        # copy the redirected url that contains geodata
        pyautogui.hotkey('ctrl', 'a')
        pyautogui.hotkey('ctrl', 'c')
        text = pyperclip.paste()
        
        x, y = cutstring(text)
        
        list.append(x) 
        list.append(y)
        print(location)
        return list

# cut the redirected url retrived from Google map to get the geodata
def cutstring(text):
    split_text = text.split("/", 7)
    split_text = split_text[6].split(",")
    split_text[0] = split_text[0].lstrip("@")
    x = split_text[0]
    y = split_text[1]
    print(x, y)
    return x, y


header=['location', 'latitude', 'longitude']

# list of locations you want google map to provide geodata for
# make sure they are clear/accurate enough so that the search result is right
locations = [ "hku", "cuhk" , "hkbu" ]

wait(5)

# make an empty file "geodata.csv" first in the same folder
with open('geodata.csv', 'w' ) as f:
    writer = csv.writer(f)
    # write the header
    writer.writerow(header)
    
    for location in locations:
        # write the data
        list = geodata(location)    
        writer.writerow(list)