import json
with open("userdata.json",'r') as file:
    data = json.load(file)
user = data['user']
print(user['name'])
for role in user['roles']:
    print(role)

user['location']['city'] = "Dallas"
with open("userdata_edited.json",'w') as file:
    json.dump(data, file, indent = 4)
