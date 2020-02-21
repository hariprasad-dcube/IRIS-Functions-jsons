
import json

with open('./functions.json') as file:
    data = json.load(file)
print(len(data))
# for i in data:
#     for j in i.keys():
#         print(j,':', i[j],'\n')