def do_this_and_print(func,data):
    print(func(data))

#We can dealre a lamaba - represtation as a fucntion similar to java
# syntax lamda value : ( operations with value, or return )
do_this_and_print(lambda value : value * 2 , 123)       #246
#finding cube
do_this_and_print(lambda value : value ** 3 , 2)        #8

do_this_and_print(lambda value : len(value) , "Test")   #4