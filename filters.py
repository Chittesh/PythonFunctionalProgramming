list_object = [1,7,4,6,13,16,19]
# Filter only even numbers
list_evenObject = list(filter ( lambda i : i % 2 == 0, list_object))
print(list_evenObject)
print(list(filter ( lambda i : i % 2 == 1, list_object)))

list_object = ["Apple","Ant","Bat"]
#filter out word containg at at the end
print(list(filter ( lambda i : i.endswith('at'), list_object)))      #['Bat']
print(list(filter ( lambda i : len(i) == 3, list_object)))          #['Ant', 'Bat']