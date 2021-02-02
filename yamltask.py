import yaml

dict_file = [{'apples':8}, {'mangoes':10},{'bananas':20}]
with open(r'C:\Users\edwiwils\Desktop\hello-world\fruits.yaml', 'w') as file:
    doc = yaml.dump(dict_file, file)
