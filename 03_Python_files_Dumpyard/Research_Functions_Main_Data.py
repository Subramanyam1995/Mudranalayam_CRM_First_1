def AAAAA_ZZZZZ(value: int):
    #A=0 , Z=25
    input_value = 151
    divid_value = [0, 25, 625, 15625, 390625, 9765625]
    a = [25**i>=input_value and input_value>=25**(i-1) for i in range(5)].index(True)
    print("a",a)
    list = [0,0,0,0,0]
    for i in range(a):
            if i!=a-1:
                value = input_value // 25**(a-(1+i))
                print(f"value: {value}, input_value: {input_value}, a: {a}")
                remaining_value = input_value % (25**(a-(i+1)))
                print(f"remaining_value: {remaining_value}, input_value: {input_value}, a: {a}")
                list[a-i-1] = value
                input_value = remaining_value

            else:
                list[a-i-1]=input_value
                print("exist")
    olddata=0
    for i in range(len(list)):
        load=list[i]*(25**i)
        load= load + olddata
        olddata =load
    print(olddata)
