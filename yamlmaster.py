import yaml
with open('userdata.yaml','r') as file:
  data = yaml.safe_load(file)
user = data['user1']
for role in user['roles']:
    print(role)
user['location']['city']= "Dallas"
with open('userdata_edited.yaml','w') as file:
    yaml.dump(data, file, default_flow_style = False)
print(data)
print(type(data))
