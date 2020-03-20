#!/usr/bin/python
# -*- coding: UTF-8 -*-
import win32clipboard
import webbrowser
import requests
import time
import re

#win32clipboard.EmptyClipboard()
#win32clipboard.SetClipboardText('testing 123')
#win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()

#print(data)

link = ""

dataTEMP = """https://jira.krafton.com/browse/PUBG-34203     
 https://jira.krafton.com/browse/PUBG-31938     
 https://jira.krafton.com/browse/PUBG-31940     
PUBG-31908     
 https://jira.krafton.com/browse/PUBG-30937       
 PUBG-31896  PUBG-434   
 https://jira.krafton.com/browse/PUBG-31897"""

p = re.compile('(?!\/)PUBG-\d+')
matchIssueIdOnly = p.findall(data)

for item in matchIssueIdOnly:
    link = "https://jira.krafton.com/browse/"+item
    print(link)
    time.sleep(0.5)
    webbrowser.open_new_tab(link)