from collections import deque

d = deque()

# Append 
d.append("monday")
print ("Append ",d)
# Append to the right
d.append("tuesday")
print ("Append to the right",d)
d.append("wedneday")
print ("Append to the right",d)


# Append to the left
d.appendleft("sunday")
print ("Append to the left",d)

# pop to the left
d.popleft()
print("popleft",d)

# pop to the right
d.pop()
print("popright",d)

#reverse deque
d.reverse()
print ("reverse",d)

#deque clear
d.clear()
print ("clear",d)

