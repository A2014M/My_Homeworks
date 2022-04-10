import json

data = '''[
    {
    "name" : "Nastya",
    "surname": "Mankoovskaya",
    "age": "35",
    "position": "junior"
    },
    {
    "name" : "Nastya",
    "surname": "Mankoovskaya",
    "age": "35",
    "position": "junior"
    }
]
'''
print(data)
print(type(data))
new_data = json.loads(data)
print(new_data)
print(type(new_data))