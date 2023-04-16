# In this section we are going to learn more about the lists
# List basically a data staructure. Datatsructure we are using to organise and retreive data efficiently.
# Lists declare as a set of items inside a square bracket. eg: fruits = ["apple", "avacado"]
# List has order. The order will not change
 
states_in_india = ["Kerala", "Tamil Nadu", "Karnadaka"]

#We can retreive list from by using index. Index starts from 0

print(states_in_india[0])

# We can assign a new value to an index
print(states_in_india[2])
states_in_india[2] = "Goa"
print(states_in_india[2])

#we can add new value to list by append

states_in_india.append("Delhi")

print(states_in_india)

states_in_india.extend(["Karanadaka", "Andra Pradesh"])

print(states_in_india)

 