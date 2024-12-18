#Write a program to create a set.
set = {1,2,3,"sai",True,11,1,2,3,1,4,5}
print(type(set))
print(set)
#Write a python program to iterate over sets.
set = {1,2,3,"ram",True,11,1,2}
if "vamsi" in set:
    print("ram is present in the set")
else:
    print("ram is not present in the set")
 #Write a Python program to add member to a set.
set = {1,2,3,"sai",True,11,1,2}
set.add(4)
print(set)
#Write a Python program to remove a member from a set.
set = {1,2,3,"sai",True,11,1,2}
set.remove(1)
print(set)
#Write a Python program to remove item from a given set.
set = {1,2,3,"ram",True,11,1,2}
set.remove(2)
print(set)
set.discard("ram")
print(set)
#Write a python program to create a intersection of set ?
set_1 = {"sun","mon","tue","wed","thur"}
set_2 = {"tue","wed","sat","holiday"}
print(set_1.intersection(set_2))
print(type(set_1))
print(type(set_2))
#Write a python program to createa unionof set ?'
set_1 = {"sun","mon","tue","wed","thur"}
set_2 = {"tue","wed","sat","holiday"}
print(set_1.union(set_2))
 #Write a python program to create set differance ?
set_1 = {1,2,3,4,5,6}
set_2 = {10,11,1,2,3,4,5,6}
print(set_1.difference(set_2))
 #Write a Python program to remove items 10, 20, 30 from the following set at once.?
set = {1,2,3,4,5,6,7,8,9,"vvv",10,20,30}
set.discard(10)
set.discard(20)
set.discard(30)
print(set)
#Check if two sets have any elements in common. If yes, display the common elements?
set_1 = {1,2,3,4,5,6}
set_2 = {10,11,1,2,3,4,5,6}
print(set_1.intersection(set_2))
#Write a python program to  add a key to a dictionary ?
dict = {
    "date":17,
    "time":4
 
}
dict['day'] = "tuesday"
print(dict)
#Write a python program to check weather the given value is present in the dictionary or not ?
dict = {
    "name":"sairam",
    "age": 24,
    "city":"Rjy"
}
if "name" in dict:
    print("yes")
    if "age" in dict:
        print("yes")
         
#Write a python program to merge two python dictionaries ?
dict_1 = {
    "name":"sai",
    "company":"skywaves"
 }
dict_2 = {
    "Uan created": "NO",
 
    "mail id": "sai@gmail.com"
 
}
dict_3 = dict_1 | (dict_2)
print(dict_3)