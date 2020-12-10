import json

def read_static_data():
    with open('StaticData') as json_file:
        return json.load(json_file)

def read_dynamic_data():
    with open('DynamicData') as json_file:
        return json.load(json_file)

def save_dynamic(data):
    with open('DynamicData',"w") as json_file:
        json.dump(data, json_file, indent=4)

static_data = read_static_data()
dynamic_data = read_dynamic_data()
print(dynamic_data)
