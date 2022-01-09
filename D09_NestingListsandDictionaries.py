'''

Nesting is the idea of putting dictionaries into lists or lists into dictionaries.

simple dictionary.
{
key: value,
key2: value2,
}

dictionary with a nested list.
{
key: [list],
key2: {dictionary},
}



'''

# Simple dictionary
capitals ={
    "France": "Paris",
    "Germany": "Berlin",
}

# nesting a list in a dictionary.
travel_log = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburg", "Stuttgart"],
}

# Nesting a list in a list

fruits_and_Veggies = [
    ["Tomato", "Carrot", "Potato"],
    ["Apple", "Orange", "Grape"],
]

another_list = ["A", "B", ["C", "D"]]

# Nesting a dictionary in a dictionary.
travel_log = {
    "France": {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 12},
    "Germany": {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"]}, "total_visits": 5,
}

print(travel_log)

# nesting a dictionary inside a list.
list_I_made = [
    {"key": [1, 2, 3],
     "key2": {"hello": "abra-ke-dabra", "pumpkin": 42, "pie": "hello"}
    },
    {"key": "brocoli",
     "key2": "fun",
    }]

travel_log = [
    {
     "country": "France",
     "cities_visited": ["Paris", "Lille", "Dijon"],
     "total_visits": 12,
    },
    {
     "country": "Germany",
     "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
     "total_visits": 5,
    },
]

print(travel_log)

print(travel_log[0])
print(travel_log[1])
