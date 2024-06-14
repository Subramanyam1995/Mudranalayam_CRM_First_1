import json

with open("test_cases_1.json","r+") as data:
    database = json.load(data)
print(database)

database1  = {}
for i in range(1000):
        database1[f"{i}"]=database

with open("test_cases_1.json","w") as data:
        json.dump(database1,data, indent=15)