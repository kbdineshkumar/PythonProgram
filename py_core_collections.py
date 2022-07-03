print("*** collection exercise ***")
'''Create a list with a range of 10 values starting from 2 to 11 and prove mutability by updating the 3rd element with 100 and prove resizable properties by adding 100 in the 5th position'''
lst=list(range(2,12))
print(lst)
lst[2]=100
lst.insert(5,100)
print(lst)

'''Create a tuple of 2 fields eg. ("Inceptez","Technologies","Pvt","Ltd"), prove immutability and non resizable nature, access the 2nd and 4th fields and store in another tuple.'''
tup = ("Inceptez","Technologies","Pvt","Ltd")
#tup[2]="tech" # immutable
tup_2 = (tup[1], tup[3])
print(tup_2)
print(type(tup_2))

#tup_1 = tuple(tup[0], tup[2]) # tuple takes at most 1 argument
#print(tup_1)

'''Convert the list of tuples [("Inceptez","Technologies"),("Apple","Incorporation")] to list of dictionary type, using for loop as given below
[{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] , once the list of dictionary is arrived print only "Incorporation" by passing "Apple" as a key using dict["Apple"] and
dict.get("Apple") and try with dict["Apple1"] and dict.get("Apple1") then find the difference between get and using[] notation.'''

lst_tup=[("Inceptez","Technologies"),("Apple","Incorporation")]
lst_dict=[]
for i in lst_tup:
    lst_dict.append({i[0]: i[1]})

print(lst_dict)
print(lst_dict[1]['Apple'])
print(lst_dict[1].get('Apple'))

#print(lst_dict[1]['Apple1']) # key error
print(lst_dict[1].get('Apple1')) # None

# Create a list of tuple as given below and delete all duplicate tuples of the list
# lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]

lst=[("Inceptez","Technologies"),("Apple","Incorporation"),("Inceptez","Technologies"),("Inceptez","Technologies")]
lst_dedup=list(set(lst))
print(lst_dedup)

# Append ("Intel","Corp") in the above de duplicated list
lst_dedup.append(("Intel","Corp"))
print(lst_dedup)

# Convert the lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}] to lst1=["Inceptez","Apple"] ,
# think about using for loop, list() function, keys function and list append functions to achieve this.

lst1=[]
lst_dict= [{"Inceptez":"Technologies"},{"Apple":"Incorporation"}]
for i in lst_dict:
    lst1.append(list(i.keys())[0])

print(lst1)

# Create a list of values lst=[10,20,40,30,20], find the first, last values of the list, sort the list in ascending order, sort in descending order,
# print the minumum and maximum values of the descending sorted list, find the sum of all elements in the list, remove the number 30 and 20 from the list.

lst=[10,20,40,30,20]
print('first element: ',lst[0]) # first element
print(lst[len(lst)-1]) # last element
print('last element: ', lst[-1]) # last element

lst.sort()
print('ascending order: ',lst)

lst.sort(reverse=True)
print('descending order: ',lst)

print('min value: ',lst[-1])
print('max value: ',lst[0])

x=0
for i in lst:
    x+=i

print('sum of all the element: ', x)

lst.remove(30)
print('removing 30:',lst)
lst.remove(20)
print('removing 20:', lst)

# Do the above same (step 25) operation in the tuple of elements tup=(10,20,40,30,20)
print('*** tuple ***')
tup=(10,20,40,30,20)

print('first element: ',tup[0]) # first element
print(tup[len(tup)-1]) # last element
print('last element: ', tup[-1]) # last element

lst_tup=list(tup)
#print(lst_tup)

lst_tup.sort()
print('ascending order: ',tuple(lst_tup))

lst_tup.sort(reverse=True)
print('descending order: ',tuple(lst_tup))

print('min value: ',lst_tup[-1])
print('max value: ',lst_tup[0])

lst_tup.remove(30)
print('removing 30:',tuple(lst_tup))
lst_tup.remove(20)
print('removing 20:', tuple(lst_tup))

# Convert the string to list from str1="Inceptez Technologies Pvt Ltd" to lst_str1=['Inceptez', 'Technologies', 'Pvt', 'Ltd']

str1="Inceptez Technologies Pvt Ltd"
#lst_str1=str1.split(' ')
lst_str1=list(str1.split(' '))
print(lst_str1)

# With the below given data in the format of list(list(elements))
# emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]

emplstlst= [["1", ("Arun","Kumar"), "10000"],["2", ("Bala","Mohan"), "12000"]]

#Convert the first element of the above list into tuple
#("1", ("Arun","Kumar"), "10000")

emp_1_tup=tuple(emplstlst[0])
print(emp_1_tup)

# Print the second element's second element and reverse the first and last name as given below
# ("Mohan","Bala")

emp_2=list(emplstlst[1][1])
emp_2.sort(reverse=True)
print(tuple(emp_2))

#  Convert the emplstlst into tuples(tuples)
emplst=[]
for i in emplstlst:
    emplst.append(tuple(i))

emplstlst=tuple(emplst)
print(emplstlst)

# Add all salary of the above list
sal=0
for i in emplstlst:
    sal+=int(i[2])

print('total salary: ',sal)