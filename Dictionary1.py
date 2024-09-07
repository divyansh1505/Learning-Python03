a =  {
    "Key" : "Value",
    "name" : "Divyansh",
    "age" : 18,
    "nationality" : "Indian",
    "Height" : "Tall",
    "SkinType" : "Handsome", 
}

print(a["name"])
print(a["age"])

print(a.items())   #print all key-value pair 
print(a.keys())    #print all the keys 
a.update({"Aura" : "Infinite"})   #it added another key-value pair 
print(a.items())
type(a)