from collections import deque

varibale = deque(['Zero','One','Two'])
#pop
print(varibale.pop())       #Two
print(varibale)             #deque(['Zero', 'One'])

varibale.append('three')
print(varibale)             #deque(['Zero', 'One', 'three'])

varibale.appendleft('four')
print(varibale)             #deque(['four', 'Zero', 'One', 'three'])




