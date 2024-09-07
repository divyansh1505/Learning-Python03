d = {}  #i just initialised a dictionary 

for i in range(4):
    name = input("Enter your name : ")
    lang = input("Your favourite programming language : ")
    d.update({name : lang})

print(d)

# The identifier in Dictionary is the key, so key cannot be the same but value
# cannot be, so if by using this update a function i enter a key again, it will 
# get updated to the value i have put on it the 2nd time 