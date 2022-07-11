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

x=int(input('enter the no: '))
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

# 37. Create a method to accept a string like “inceptez technologies” and return the following values in multiple result types (capitalize, upper case, length of the string, number of words, ends with “s” or not, replace ‘e’ with ‘a’) for eg. the result should be like this.. (Inceptez Technologies, INCEPTEZ TECHNOLOGIES, 21, 2, True,incaptaz tachnologias)
def str_manipulate(st):
    if (isinstance(st, str)):
        return (st.title(),st.upper(),st.__len__(),len(st.split()),st.endswith('s'),st.replace('e','a'))
    else:
        print("The given input is not a string. please give the input as string")

x=str_manipulate(st='inceptez technologies')
print(x)

st1='hello how are you'
print(st1.title())


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


print('*** purchase amt exercise ***')
'''
def offer_calc(x):
    off_per=50/100
    #off_max=100
    discounted_price=x()*off_per
    def max_check(off_max=100):
        if discounted_price == '':
            print('no discount will be applied')
            dp_u=x
        elif discounted_price >= off_max:
            dp_u=x-off_max
        elif discounted_price < off_max:
            dp_u=x-discounted_price
        return dp_u
    return max_check

def ip():
    x=int(input('enter the purchase amount: '))
    return x

#x=offer_calc(ip)
#resu=x()
'''
#p=300
def off(pamount,per,mx):
    #per=0.5
    #mx=100
    def disc_cal(x,y):
        dis=x*y
        return dis
    def disc(fn,x,y):
        return fn(x,y)
    dis=disc(disc_cal,per,pamount)
    #print('discounted price:',dis)
    def max_check():
        if dis >= mx:
            print(f'max offer applied is {mx} only')
            n=pamount-mx;
        elif dis < mx:
            print(dis,'offer applied')
            n=pamount-dis
        return n
    return max_check


mx=100
i=int(input('enter the purchase amount: '))
print('By default 50% offer available and max discount price is 100')
m=str(input('do you want modify the discount % and max discount price ? yes or no: '))
if m=='yes' or m=='y':
    dper=int(input('enter the discount %: '))
    dprice= int(input('enter the max discount price: '))
    x=off(i,dper/100,dprice)
    print(x())
elif m=='no' or m=='n':
    x = off(i,per=0.5,mx=100)
    print(x())

'''
def disc_calc(o,m):
    r=o*m
    return r

def disc(fnname,x,y):
    return fnname(x,y)

print(disc(disc_calc,0.5,100))

'''