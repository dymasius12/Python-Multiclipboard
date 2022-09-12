import sys 
import clipboard
# We are going to save the clipboard in json file
import json

data = clipboard.paste()
print(data)