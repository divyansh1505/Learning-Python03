s = {1, 5, 6}

e = set() #dont use s = {} as it will create an empty dictionary 

s.add(4)
print(s)

s1 = {3,4,7,9,12,45,67,89}
s2 = {3,65,78,89,43,55}

print(s1.intersection(s2))    #these two will give same results 
print(s1 & s2)

print(s1.union(s2))  #similarly, these two will give the same results 
print(s1 | s2) 

print(s1 - s2)  #this works in REPL too 