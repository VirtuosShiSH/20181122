import win32clipboard
import webbrowser
import requests
import time

# set clipboard data
#win32clipboard.OpenClipboard()
#win32clipboard.EmptyClipboard()
#win32clipboard.SetClipboardText('testing 123')
#win32clipboard.CloseClipboard()

# get clipboard data
win32clipboard.OpenClipboard()
data = win32clipboard.GetClipboardData()
win32clipboard.CloseClipboard()
list = data.split()
#print(data)
#print(list)
link = ""
for item in list:
    link = "https://jira.krafton.com/browse/"+item
    print(link)
    time.sleep(0.5)
    webbrowser.open_new_tab(link)