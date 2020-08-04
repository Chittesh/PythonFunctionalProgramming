list_object = ["Apple","Ant","Bat"]

#To get a list with upper case
print(list(map(lambda x : x.upper(), list_object)))     #['APPLE', 'ANT', 'BAT']
print(set(map(lambda x : x.upper(), list_object)))      #{'ANT', 'BAT', 'APPLE'}