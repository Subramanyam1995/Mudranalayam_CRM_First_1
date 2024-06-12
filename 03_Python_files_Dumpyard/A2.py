import json
import pprint
from Mudranalayam_Funcation_DataBase import Creation_Of_New_Database
import datetime
with open("Data_Base.json","r") as database_1:
    loaded_data_base = json.load(database_1)

loaded_data_base["mudranalayam"]["AAAAA"]["Name"] = [["Dileep",9902136721]]

update_name = ["Sudeep", 1231231234]

#pprint.pprint(a["mudranalayam"]["AAAAA"],indent=4)

loaded_data_base["mudranalayam"]["AAAAA"]["Name"].insert(0,update_name)

#pprint.pprint(a["mudranalayam"]["AAAAA"],indent=4)

loaded_data_base["mudranalayam"]["AAAAD"]={  }

#pprint.pprint(a["mudranalayam"],indent=1)

#print(len(loaded_data_base["mudranalayam"]["AAAAA"]))

"""with open("Data_Base.json","w") as database_1:
        json.dump(a, database_1,indent=4)
        """
