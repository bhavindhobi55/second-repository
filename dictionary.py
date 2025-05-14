thisdict = {
    "brand":"Ford",
    "car":"Mustang",
    "model":"1969"
}
print(thisdict)
print(len(thisdict))

#access values
x=thisdict["model"]
print(x)
print(thisdict["model"])
x=thisdict.get("model") #with get method
print(x)

#access key,value,item
x = thisdict.keys()
print(x)
x = thisdict.values()
print(x)
x = thisdict.items()
print(x)

#access key,value,item by loop
for x in thisdict:
   print(thisdict)
for x in thisdict.keys():
    print(x)
for x in thisdict.values():
   print(x)
for x in thisdict:
   print(x)
for x,y in thisdict.items():
   print(x,y)

#adding
x=thisdict.items()
print(x) # before adding
thisdict["color"]="blue"
print(thisdict)    #after adding

#update
print(x)    #before update
thisdict["model"]=2020
print(x)   #after update
thisdict.update({"model":2022})
thisdict.update({"color":"red"})
print(thisdict) 

#copy
mydict=thisdict.copy()
print(mydict)
mydict=dict(thisdict)
print("mydict is coppied",mydict)

#remove
print(thisdict)
thisdict.popitem()
print(thisdict)
thisdict.pop("car")
print(thisdict)

#clear,delete
print(thisdict)
thisdict.clear()
print(thisdict)
del thisdict
print(thisdict)

# --------- NESTED Dictionary---------

company ={
    "brand1" : {
        "name" : "Mustang",
        "year" : 1969
    },
    "brand2" : {
        "name" : "BMW",
        "year" : 2018,
        "xyz" : "abc"
    },
    "brand3" : {
        "name" : "dodge",
        "year" : 1981
    }
}
print(company)  #access all items

print(company["brand1"])    #access nested dictionary

print(company["brand2"]["name"])    #access nested dictionary specific element

#access all items in key:value format
for x,obj in company.items():
    print(x)
    for y in obj:
        print(y+':',obj[y])