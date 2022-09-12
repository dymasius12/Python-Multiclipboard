import sys 
import clipboard
# We are going to save the clipboard in json file
import json

# below print the after the python file name
# print(sys.argv)

#this is a variable where you want to save your data
SAVED_DATA = "clipboard.json"

# Make a file that can create JSON file for us
def save_data(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)

def load_data(filepath):
    #check if the file exist or not
    try:
        with open(filepath, "r") as f:
            data = json.load(f)
            return data
    except:
        return {}

save_data("test.json", {"key": "value"})

if len(sys.argv) == 2:
    command = sys.argv[1]
    
    data = load_data(SAVED_DATA)

    if command == "save":
        key = input("enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVED_DATA,data)
    elif command == "load":
        print("load")
    elif command =="list":
        print("list")
    else:
        print("Unknown command!")

else:
    print("Please type in only 1 command.")

# if we want to copy using the clipboard function
# clipboard.copy("abc")

# This is more on printing the data in the clipboard
# data = clipboard.paste()
# print(data)