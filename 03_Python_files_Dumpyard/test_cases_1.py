import json

"""database  = {}
for i in range(1000):
        database[f"{i}"]={"A1":"aa","B1":"bb"}

with open("test_cases_1.json","w") as data:
        json.dump(database,data, indent=15)
print("Done")"""

"""with open("test_cases_1.json","r") as data:
    database = json.load(data)

aa = list(database.keys())
print(len(aa))"""
set1 = {"apple", "banana", "cherry"}
set2 = {"google", "microsoft", "apple"}

set1.intersection_update(set2)

print(set1)

set1 = {"apple", 1,  "banana", 0, "cherry"}
set2 = {False, "google", 1, "apple", 2, True}

set3 = set1.intersection(set2)

print(set3)