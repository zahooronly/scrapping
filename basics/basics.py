# python basics for learning web scrapping

import pandas as pd

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
states_population=[
    4903185,
    731545,
    7374662,
    3017826,
    39512223,
    7575597,
    3565287,
    973764,
    21550706,
    10617423,
    1367738,
    6732219,
    12672031,
    6588955,
    2976149,
    9985153,
    4694959,
    6083672,
    6829172,
    1068778,
    6046182,
    6725913,
    19552860,
    12174066,
    5105681,
    6537376,
    13260311,
    10731022,
    2995918,
    10593611,
    2085109,
    2085109,
    13593778,
    
]
# print(states[1])


dict_state={
    "States":states,
    "Population":states_population
}
df_states=pd.DataFrame.from_dict(dict_state)
print(df_states)


# loops

# for state in states:
    # print(state)
    # conditions
    # if state=="Floria":
    #     print(state)
        
# functions
# def state_availability(state):
#     if state in states:
#         print("yes")
#         return True
#     else:
#         print("no")
#         return False
# state_availability("Florida")

# file handling

# first way and old way
# with open("test.txt","w") as file:
#     file.write("Data successfully scraped!")

