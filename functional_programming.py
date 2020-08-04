def muliply_by_2(data):
    return data * 2;

print(muliply_by_2(3))

# we are making one paramameter as a function
def do_this_and_print(func,data):
    # desihned to call the function
    print(func(data))

#passing first functions as a parameter
do_this_and_print(muliply_by_2 , 4)

