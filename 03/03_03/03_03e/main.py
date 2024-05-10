# mutating a dictionary 

user_preferences = {
    "language": "English",
    "font_size": "14px",
    "timezone": "GMT",
    "currency": "USD",
    "enable_location": False,
    "volume_level": 80,
    "date_format": "MM/DD/YYYY"
}

# lets change the language from english to spanish 
user_preferences["language"] = "Spanish"

#change the volume to 50, NOTEE: we are overriding here and can no longer access previous data
user_preferences["volume_level"] = 50

# add an item to the dictionary 
user_preferences["highlight_color"] = "pink"

# delete an item from the dictionary 
del user_preferences["currency"]            # the way it guessed currency for me really just lets me know codespaces is listining lol 

# use the pop function to retrieve an item when you delete it
# i think if i remember pop pops to the front? but a quick google search has me uncertain. something to ponder lol 
removed_item = user_preferences.pop("date_format", "N/A")   # NA prevents a key error from occuring


print(user_preferences)
