import json

data = {"name": "John", "age": 30, "city": "New York"}

json_data = json.dumps(data)
print(json_data)
json_data = '{"name": "John", "age": 30, "city": "New York"}'
data = json.loads(json_data)
print(data)


data = {"name": "John", "age": 30, "city": "New York"}

with open("data.json", "w") as file:
    json.dump(data, file)


with open("data.json", "r") as file:
    data = json.load(file)

print(data)  # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
