# Key: State
# Value: Capital
# i think this kinda reminds me of a structure tbh
# i guess this is abstract

states_to_capitals = {
  "Texas" : "Austin",
  "New York" : "Albany",
  "Colorado" : "Denver"
}

print(states_to_capitals["Colorado"])

for key in states_to_capitals.keys():
  print(key)

# now lets print out the key and its value 
for key, value in states_to_capitals.items():
  print(key + " | " + value)
