user_preferences = {
    "timezone": "GMT",
    "language": "English",
    "notifications": None,
    "currency": "USD",
    "theme": None
}

# clean our data 
def update_preferences(user_pref):
    updated_preferences = {}
    for key, value in user_pref.items():        #iterate through to find keys w no values
        if value is not None:
            updated_preferences[key] = value

    return updated_preferences

# do it using comprehension 
def updatee_preferences(user_pref):
    return {key: value for key, value in user_pref.items() if value is not None}


print(update_preferences(user_preferences))
print(updatee_preferences(user_preferences))

