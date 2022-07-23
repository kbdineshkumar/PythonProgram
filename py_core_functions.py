import string

#use case 12 using function
def pos_neg_odd_even(x):
    if x>=0:
        if x%2 == 0:
            print('given number is even and non negative')
        else:
            print('given number is neither negative nor even')
    else:
        if x%2 == 0:
            print('given number is even but negative')
        else:
            print('given number is not even but negative')

x=2
a=int(x)
pos_neg_odd_even(a)
pos_neg_odd_even(x=-4)

# Write a nested if then else to print the course fees - check if student choosing bigdata, then fees is 25000,
# if student choosing spark then fees is 15000, if the student choosing datascience then check
# if machinelearning then 25000 or if deep learning then 45000 otherwise if both then 25000+25000.
def coursefee(course, subcourse):
 if course == 'bigdata':
  print('cousre fees is'+' '+str(25000))
 elif course == 'spark':
  print('cousre fees is'+' '+str(15000))
 elif course == 'datascience':
  if subcourse == 'machinelearning':
   print('cousre fees is'+' '+str(25000))
  elif subcourse == 'deep learing':
   print('cousre fees is'+' '+str(45000))
  else:
   print('course fees is'+' '+str(25000+25000))

coursefee('bigdata','')
coursefee('spark','')
coursefee('datascience','machinelearning')
coursefee('datascience','deep learing')
coursefee('datascience','')

# 14. Check whether the given string is palindrome or not (try to use some function like reverse).
# For eg: x="madam" and y="madam", if x matches with y then print as "palindrome" else "not a  palindrome".
def check_palindrome(x):
    y=''
    l=len(x)-1
    while(l>=0):
        y+=x[l]
        l-=1

    if x==y:
        print('given string is palindrome')
    else:
        print('given string is not palindrome')

x='madam'
x.strip()
check_palindrome(x)

# Check whether the x=100 is an integer or string. (try to use some functions like str or upper function etc to execute this use case) or
# use isinstanceof(variablename,datatype) function.'''

def type_check(x):
    if isinstance(x, int):
        print('integer')
    elif isinstance(x, str):
        print('string')
    elif isinstance(x, type(x)):
        print('neither int nor str')

x = 10.5
print(type(x))
type_check(x)

# 26. Write a program using for loop to print even numbers and odd numbers in the below range of data (generate using range function) [5,6,7,8,9,10,11,12,13,14,15,
# 16,17,18,19,20] output should be with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.

def odd_even(lst):
    even=[]
    odd=[]
    for i in lst:
        if i%2 == 0:
            even.append(i)
        else:
            odd.append(i)
    return (odd,even)

lst=list(range(5,21))
print(lst)
(odd, even) = odd_even(lst)
print('even no. are:',even)
print('odd no. are:',odd)

# 27. Write a while loop to loop from 0 till 21 with the increment of 3, the result should be exactly 3,6,9,12,15,18 and store this result in a list
def inc_by_val(x):
    i=0+x
    res=[]
    while(i<21):
       res.append(i)
       i+=3
    return res

res=inc_by_val(3)
print('results: ',res)

# 28. Write a for or while loop to print the cube of 4, result should be 4*4*4=64 (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)

def find_cube(x):
    i=1
    cube=1
    while(i<=3):
        cube=cube*x
        print(x)
        i+=1
    return cube

x=4
ret=find_cube(x)
print('cube results: ',ret)

# 29. Create a list as sal_lst=[10000,20000,30000,10000,15000], loop through the list and add 1000 bonus to the salary and store in another list sal_bonus_lst=[11000,21000,31000,11000,16000]
# then store the bonus applied salary in another list where sal>11000

def bonus_calc(sal_lst):
    sal_bonus_lst=[]
    sal_bonus_lst1=[]
    for i in sal_lst:
        x=i+1000
        sal_bonus_lst.append(x)
        if x>11000:
            sal_bonus_lst1.append(x)
    return (sal_bonus_lst, sal_bonus_lst1)

sal_lst=[10000,20000,30000,10000,15000]
print('salary list: ',sal_lst)
(sal_bonus_lst, sal_bonus_lst1) = bonus_calc(sal_lst)
print('bonus applied sal: ',sal_bonus_lst)
print('bonus applied sal with > 11000: ',sal_bonus_lst1)

# 30. Write a do while loop to print “Inceptez technologies” n number of times as per the input you get from the user.
# Minimum it has to be printed at least one time regardless of the user input.
def print_cmp_name(x):
    i=0
    while True:
        print("Inceptez technologies")
        if(i == x):
            break
        i+=1

#x=int(input('enter the no: '))
x=1
print_cmp_name(x)

# 31. lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number, calculate the min value and the max value of all the elements in the lst1.

def list_manipulate(lst1):
    t=0
    comb=[]
    for i in lst1:
        for j in i:
            t+=j
            comb.append(j)
    return(t,comb)

lst1=[[10,20],[30,40,50],[60,70,80]]
(t,comb) = list_manipulate(lst1)
print('total sum of all number:', t)
comb.sort()
print('min value',comb[0])
print('max value',comb[-1])

# 32. Create a looping construct to create 3 tables upto 10 values. Output should be like this…
def table(x):
    for i in list(range(1,11)):
        print(i,'x',x,'=',i*x)

x=3
table(x)

# 35. Write a function to create a calculator that accepts 3 arguments with the datatype of first 2 as int and 3rd one is str, based on the 3rd argument value passed as add/sub/div/mul perform either addition or subraction or multiplication or division respectively of argument 1 and 2 then return the result to the calling environment. Create a default argument function to handle “if the 3rd argument is not passed then default it to add”.
# 36. Convert the above calculator function to return complex type as tuple by calculating addition, subtraction, multiplication and division in one shot and return result with multiple types for eg. calc(10,3,all) should return (13,7,30,.33)
def calc(x,y,operation='add'):
    if operation == 'add' or operation == '':
        return x+y
    if operation == 'sub':
        return x-y
    if operation == 'mul':
        return x*y
    if operation == 'div':
        return x/y
    if operation == 'all':
        return (x+y,x-y,x*y,x/y)

ab=calc(5,3,'add')
print(ab)

ab=calc(5,3,'sub')
print(ab)

ab=calc(5,3,'mul')
print(ab)

ab=calc(5,3,'div')
print(ab)

ab=calc(5,3)
print(ab)

ab=calc(5,3,operation='mul')
print(ab)

ab=calc(operation='div',y=5,x=3)
print(ab)

ab=calc(5,3,'all')
print(ab)

# 37. Create a method to accept a string like “inceptez technologies” and return the following values in
# multiple result types (capitalize, upper case, length of the string, number of words, ends with “s” or not, replace ‘e’ with ‘a’)
# for eg. the result should be like this.. (Inceptez Technologies, INCEPTEZ TECHNOLOGIES, 21, 2, True,incaptaz tachnologias)
def str_manipulate(st):
    if (isinstance(st, str)):
        return (st.title(),st.upper(),st.__len__(),len(st.split()),st.endswith('s'),st.replace('e','a'))
    else:
        print("The given input is not a string. please give the input as string")

x=str_manipulate(st='inceptez technologies')
print(x)

st1='hello how are you'
print(st1.title())

# 41. Apply exception handler code in the above usecase number 35 to achieve the followings
# a.  If the calculator function is called with either the first or second argument as non integer values then raise Exception and call the calculator function
# with the type casted value
# for eg. calc("10",20, "add") in the except block of the exception handler we have to call the same function as calc(int("10"),20, "add") and
# return the result to the calling environment.
def calc(x,y,operation='add'):
    try:
        if operation == 'add' or operation == '':
            return x+y
        if operation == 'sub':
            return x-y
        if operation == 'mul':
            return x*y
        if operation == 'div':
            return x/y
        if operation == 'all':
            return (x+y,x-y,x*y,x/y)
    except Exception as msg:
        print('error in input',msg)
        return calc(int(x),int(y),str(operation))
    finally:
        print('end of the function')

ab=calc(5,3,'add')
print(ab)

ab=calc("5",3,'sub')
print(ab)

ab=calc(5,'3','mul')
print(ab)

ab=calc('5','3','div')
print(ab)

ab=calc(5,3)
print(ab)

ab=calc(5,3,operation='mul')
print(ab)

ab=calc(operation='div',y=5,x='3')
print(ab)

ab=calc(5,3,'all')
print(ab)

# 38. Create a regular function called promo that accepts 3 arguments where arg1 is amount, arg2 is the offer_percent and arg3 is the offer_cap_limit.
# Calculate if amount*offer_percent < offer_cap_limit then return amount-(amount*offer_percent) else return the amount-offer_cap_limit

# a. Create the function with the above logic and call with all 3 params passed for eg: promo(1000,.10,200)
def promo(amt, off_per, off_cap_lmt):
    off_amt=amt*off_per
    if off_amt < off_cap_lmt:
        return amt-off_amt
    else:
        return amt-off_cap_lmt

val=promo(1000,.10,200)
#val=promo(300,.50,100)
print(val)

# b. Create the function with the above logic (with default parameter) and call with first 2 params passed for eg: promo(1000,.10)
def promo(amt, off_per, off_cap_lmt=200):
    off_amt=amt*off_per
    if off_amt < off_cap_lmt:
        return amt-off_amt
    else:
        return amt-off_cap_lmt

val=promo(1000,.10)
#val=promo(300,.50)
print(val)

# c. Create the function with the above logic (with arbitrary arguments) and call with all 3 params passed for eg: promo(1000,.10,200)
def promo(*args):
    (amt,off_per,off_cap_lmt)=(args[0],args[1],args[2])
    off_amt=amt*off_per
    if off_amt < off_cap_lmt:
        return amt-off_amt
    else:
        return amt-off_cap_lmt

val=promo(1000,.10,200)
#val=promo(300,.50,100)
print(val)

# d. Create the function with the above logic (with keyword arbitrary arguments) and call with all 3 params passed for eg: promo(offer_percent=.10,offer_cap_limit=200,amount=1000)
def promo(**args):
    (amt,off_per,off_cap_lmt)=(args['amount'],args['offer_percent'],args['offer_cap_limit'])
    off_amt=amt*off_per
    if off_amt < off_cap_lmt:
        return amt-off_amt
    else:
        return amt-off_cap_lmt

val=promo(offer_percent=.10,offer_cap_limit=200,amount=1000)
#val=promo(offer_percent=.50,amount=300,offer_cap_limit=100)
print(val)

# 39. Create a lambda function with the logic of lam=amount-(amount*offer_percent) and create a regular function with the above same logic with 4 arguments
# to Calculate if amount*offer_percent < offer_cap_limit then return lam(amount,offer_percent) else return the amount-offer_cap_limit.
# Eg. Call this function like promo(1000,.10,200,lam) to ensure this is a higher order function
def promo(amt, off_per, off_cap_lmt,lam):
    off_amt=amt*off_per
    if off_amt < off_cap_lmt:
        #return amt-off_amt
        return lam(amt,off_per)
    else:
        return amt-off_cap_lmt

lam=lambda amt,off_per:amt-(amt*off_per)
val=promo(1000,.10,200,lam)
#val=promo(300,.50,100,lam)
print(val)

# 40. Create a lambda function as like the regular function created in step 38.
# a. Create the function with the above logic and call with all 3 params passed for eg: promo(1000,.10,200)
print("method 1")
promo=lambda amt, off_per, off_cap_lmt:amt-(amt*off_per) if (amt*off_per<off_cap_lmt) else amt-off_cap_lmt
val=promo(1000,.10,200)
#val=promo(300,.50)
print(val)

print("method 2")
promo=lambda amt, off_per, off_cap_lmt:(lambda: amt-off_cap_lmt, lambda: amt-(amt*off_per))[amt*off_per<off_cap_lmt]()
val=promo(1000,.10,200)
#val=promo(300,.50,100)
print(val)

# b. Create the function with the above logic (with default parameter) and call with first 2 params passed for eg: promo(1000,.10)
promo=lambda amt, off_per, off_cap_lmt=50:amt-(amt*off_per) if (amt*off_per<off_cap_lmt) else amt-off_cap_lmt
val=promo(1000,.10)
#val=promo(300,.50)
print(val)

# c. Create the function with the above logic (with arbitrary arguments) and call with all 3 params passed for eg: promo(1000,.10,200)
promo=lambda *args:args[0]-(args[0]*args[1]) if (args[0]*args[1]<args[2]) else args[0]-args[2]
val=promo(1000,.10,200)
#val=promo(300,.50)
print(val)

# d. Create the function with the above logic (with keyword arbitrary arguments) and call with all 3 params passed for eg: promo(offer_percent=.10,offer_cap_limit=200,amount=1000)
promo=lambda **args:args['amount']-(args['amount']*args['offer_percent']) if (args['amount']*args['offer_percent']<args['offer_cap_limit']) else args['amount']-args['offer_cap_limit']
val=promo(offer_percent=.10,offer_cap_limit=200,amount=1000)
#val=promo(offer_percent=.50,amount=300,offer_cap_limit=100)
print(val)


# 42. Write an exception handler code to raise exception if the 2nd argument passed is a negative value in the function created in step 38
# a. Create the function with the above logic and call with all 3 params passed for eg: promo(1000,.10,200)
def promo(amt, off_per, off_cap_lmt):
    try:
        if off_per < 0:
            raise Exception
        else:
            off_amt=amt*off_per
            if off_amt < off_cap_lmt:
                return amt-off_amt
            else:
                return amt-off_cap_lmt
    except Exception as msg:
        print("offer percent shouldn't be in negative", msg)
        return 0

val=promo(1000,-.10,200)
#val=promo(300,.50,100)
print(val)