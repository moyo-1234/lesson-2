fruits = {
    "apple" : "red",
    "banana" : "Yellow",
    "Cherry" : "Maroon"
    }

#operations of dictionary:
#accessing values
print(fruits["banana"])


#update the value
fruits["banana"] = "green"
print(fruits)



#adding the items
fruits["watermelon"] = "red"
print(fruits)


#remove the items
del fruits["apple"]

print(fruits)

#check membership

if "banana" in fruits:
   print("banana is present")
else:
   print("banana isn't present")



#iterating over the keys
for key in fruits.keys() :
    print(fruits[key])

#iterating over the values
for values in fruits.values():
    print(values)

#getting the length
print(fruits)
print(len(fruits))

