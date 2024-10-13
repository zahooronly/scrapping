# python basics for learning web scrapping

states=[
    "Alabama",
    "Alaska",
    "Arizona",
    "Arkansas",
    "California",
    "Colorado",
    "Connecticut",
    "Delaware",
    "Florida",
    "Georgia",
    "Hawaii",
    "Idaho",
    "Illinois",
    "Indiana",
    "Iowa",
    "Kansas",
    "Kentucky",
    "Louisiana",
    "Maine",
    "Maryland",
    "Massachusetts",
    "Michigan",
    "Minnesota",
    "Mississippi",
    "Missouri",
    "Montana",
    "Nebraska",
    "Nevada",
    "New Hampshire",
    "New Jersey",
    "New Mexico",
    "New York",
    "North Carolina",
]

# print(states[1])

# loops

for state in states:
    # print(state)
    # conditions
    if state=="Floria":
        print(state)
        
# functions
def state_availability(state):
    if state in states:
        print("yes")
        return True
    else:
        print("no")
        return False
# state_availability("Florida")
