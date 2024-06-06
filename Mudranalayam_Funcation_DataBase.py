

from A2 import *

def Creation_Of_New_Database(Database, Database_serial_Code):

    loaded_database_json = Database

#    loaded_database_json


def Database_Next_Serial_Code_Generator():
    print(len(loaded_data_base["mudranalayam"]))

def Serial_Code_Generator_Main(input_value : int):
    if type(input_value)==int:
        return Serial_Code_Generator(input_value)
    else: print(f"Invaild Input, {datetime.datetime.now()}")

def Serial_Code_Generator(input_value : int):
    #A=0 , Z=25
    divid_value = [0, 25, 625, 15625, 390625, 9765625]
    a = [25**i>=input_value and input_value>=25**(i-1) for i in range(5)].index(True)
    list = [0,0,0,0,0]
    for i in range(a):
            if i!=a-1:
                value = input_value // 25**(a-(1+i))
                remaining_value = input_value % (25**(a-(i+1)))
                list[a-i-1] = value
                input_value = remaining_value
            else:
                list[a-i-1]=input_value


    Total_value=0
    for i in range(len(list)):
        load=list[i]*(25**i)
        load= load + Total_value
        Total_value =load

    SerialCodefinal = [str(chr(65 + list[0])) +
                       str(chr(65 + list[1])) +
                       str(chr(65 + list[2])) +
                       str(chr(65 + list[3])) +
                       str(chr(65 + list[4]))]
    return SerialCodefinal[0]

if __name__=="__main__":
    pass





