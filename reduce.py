
from functools import reduce

list_object = [1,7,4,6,13,16,19]
#suntax is redeuce(lamda x,y : return value , object)
print(reduce(lambda x , y: x + y ,list_object))


#combination of filter and Map
print(list(map(lambda x : x* x ,list(filter(lambda x:x %2==0,list_object)))))

print(sum(map(lambda x : x* x ,list(filter(lambda x:x %2==0,list_object)))))


months = [('December',31), ('January',2),('July',26)]


#total sum of months
print(list(map(lambda x :x [1], months)))
print(sum(map(lambda x :x [1], months)))
#month with least number of days
print(min(map(lambda x :x [1], months)))

#reduce takes 2 parameters
# in the codition perform operation with 2 values and based on the results return values
print(reduce(lambda x ,y : x if x[1] < y[1] else y, months))   #('January', 2)
print(reduce(lambda x ,y : x if x[1] < y[1] else y, months)[0])     #January








