'''Create 2 variables with x as 100 & y as 10 respectively and find the Multiplication and division of both and store in some val as z and z1'''
x=5
print(x)
print(type(x))
y:int='hello'
y='hi'

'''Create a as 2000 and find the division of a by y (created in step 1) and reassign a with the divided result (200)'''
x=100
y=20
z=x*y
z1=x/y

z,z1 = x*y, x/y
print(z)
print(z1)

a=2000
print(a)
a=a/y
print(a)

'''Prove Python is Dynamically Typed Language: Create x:int=100, then assign the x to y, but the datatype of y has to be of type string. (think about using some function like str()). Print the type of y and x'''
x:int=100
y="hi"
y=x # check
print (type(y))
y=str(x)

print (type(x))
print (type(y))

'''Prove Python has dynamic inference feature'''
x=3
print (type(x))
x="hello"
print (type(x))
x=100.5
print (type(x))

'''Prove Python is Strongly Typed Language'''
x=2
y="how are you?"
#print(x+y)
print(str(x)+' '+y)

x=2
y=10.45
print(x+y)

'''Create variables a,b,c,d assigned with 10,20,30,40 respectively'''
a,b,c,d=10,20,30,40
print(a,b,c,d)

'''Prove Python variables are case sensitive'''
xyz=2
XYZ=3
xYz=4
xyZ='abc'
print(xyz)
print(xyZ)

#2c=5
_2c=4
#-s=5
print(_2c)

'''Show some examples of when do we use single, double and triple (single/double) quotes'''
sq='python is "dynnamically typed" langauage'
dq="python is 'dynnamically typed' langauage"
tq='''python is
'high level' and "interepreted" 	
langauage'''
print(sq)
print(dq)
print(tq)

'''Show an examples to use arithmetic, comparison, relational and logical operators.'''
s=10
s+=1
t=20
print('addition of s and t: ',s+t)

if s > y:
 print ('s is greater')
elif y > s:
 print ('y is greater')
elif s==y:
 print ('s equals y')
else:
 print('some error in input value')


x=1
if x:
 print('true')
else:
 print('false')

y='True' #true
if y:
 print('true')
else:
 print('false')

print('*** conditional exercise ***')
'''Write a program to find the greatest of 3 numbers'''
def greatest(a,b,c):
 if a==b==c:
  print('all the numbers are equal')
 elif (a>b and a>c):
  print('a is bigger')
 elif (b>a and b>c):
  print('b is bigger')
 elif (c>a and c>b):
  print('c is bigger')
 elif(a==b and a>c):
  print('a and b are equal and bigger than c')
 elif(a==c and a>b):
  print('a and c are equal and bigger than b')
 elif(b==c and b>a):
  print('b and c are equal and bigger than a')

greatest(5,2,4)


'''Write a single program to find the given number is even or whether it is negative and print the output as (the given number is even but not negative or the given number is not even but negative or the given number is neither negative nor even) '''
#x=input('enter input number: ')
x=2
x=int(x)

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

'''Write a nested if then else to print the course fees - check if student choosing bigdata, then fees is 25000, if student choosing spark then fees is 15000, if the student choosing datascience then check if machinelearning then 25000 or if deep learning then 45000 otherwise if both then 25000+25000.'''

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

'''Check whether the given string is palindrome or not (try to use some function like reverse). For eg: x="madam" and y="madam", if x matches with y then print as "palindrome" else "not a  palindrome".'''
#x=input('enter string to find whether it is palindrom or not\n') #"madam"
x='madam'
x.strip()
y=''
l=len(x)-1
while(l>=0):
 y+=x[l]
 l-=1

if x==y:
 print('given string is palindrome')
else:
 print('given string is not palindrome')


'''Check whether the x=100 is an integer or string. (try to use some functions like str or upper function etc to execute this use case) or use isinstanceof(variablename,datatype) function.'''
x = 'hi'
print(type(x))

if isinstance(x, int):
 print('integer')
elif isinstance(x, str):
 print('string')

############# General handson ref ########

var1=" Years"
var2=" Inceptez "
totalsal,empid=10000+2000, 10

print('Total sal is '+str(totalsal)+' for the emp id '+str(empid))
print('Total sal is',totalsal,'for the emp id',empid)
print(f'Total sal is {totalsal} for the emp id {empid}')
print('Total sal is {0} for the emp id {1}'.format(totalsal,empid))

str1='Test'
print(str1[0])
str1='ATEST'
print(str1)
for i in str1:
    print(i)
str1='10'
print(str1.upper())

lst2 = ['a','e','x','o','u']
x=lst2.remove('x')
print(x)
print(lst2)
lst2.insert(2,'i')
print(lst2)
lst2.append('e')
print(lst2)
x=lst2.pop()
print(x)
print(lst2)


lst2[2]='I'
print(lst2)
lst2.reverse()
print(lst2)
lst2.clear()
print(lst2)
lst2=lst2.__add__(['a']) # only list can be added
print(lst2)

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
lst = [5,4,2,3,1,5,3]
print(lst)
print("slicing a list")
print(lst[1:3])
print("Append lists")
lst=lst.__add__(weekdays)
'''for i in lst:
    print(i+10)'''

print(lst.count(3))
print(len(lst))
print(lst)

tup=("hi","inceptez","pvt ltd")
print(tup)
print(tup[1])
tuplst=list(tup)
print(tuplst)
tuplst.insert(2,'technologies')
tup=tuple(tuplst)
print(tup)

for i in tup:
    print(i)

if 'inceptez' in tup:
    print('inceptez is available in tuple')

lst=[1,3,4,5,2,6,3,4,2]
#lst=[1000,3000,4000,5000,2000,6000,3000,4000,2000]
s=set(lst)
print(s)
print(s.__len__())
s.remove(4)
s.discard(7)
print(s)
print(s.intersection({1,2}))

my_dict = {'first_name': 'inceptez', 'last_name': 'tech','age': 6}
print(my_dict)
print(my_dict.keys())
print(my_dict.values())
x=my_dict.__delitem__('last_name')
print(x)
print(my_dict)
my_dict['last_name']='technologies'
print(my_dict)
x=my_dict.pop('age')
print(x)
print(my_dict)
#print(my_dict['city'])
print(my_dict.get('city'))

for k,v in my_dict.items():
    print(k,v)

for i in my_dict.keys():
    print(i,my_dict[i])

complextup=[(1,
            "Madison's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Madison"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"Elisa"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}]),
            (2,
            "Irfan's Family",
            [{"gender":"male","Relation":"self","personalinfo":{"title":"Ms","name":"Irfan"}},
             {"gender":"female","Relation":"spouse","personalinfo":{"title":"Mrs","name":"abc"}},
             {"gender":"female","Relation":"daughter","personalinfo":{"title":"Miss","name":"Hanna","hobby":"book reading"}},
             {"gender":"male","Relation":"son","personalinfo":{"title":"Master","name":"Dave","schooling":True}}])
            ]
for i in complextup:
    if i[0] == 2:
        name=i[2][0]['personalinfo']['name']
        for j in i[2]:
            if j['Relation'] == 'son' and j['personalinfo']['schooling']:
                print(name, j['Relation'], 'has school')
            if j['personalinfo'].get('hobby'):
                print(name,j['Relation'],'has hobby of',j['personalinfo']['hobby'])

print(complextup[1][2][2].get('personalinfo'))
print(complextup[1][2][2]['personalinfo'].get('hobby'))

print(complextup[1][2][2].keys())
print(complextup[1][2][2].values())

x=100
try:
    y="hello"
    #z=str(x)+y
    z=x+y
    print(z)
except Exception as msg:
    print("inside exception block",msg)
except TypeError as msg:
    print("inside type error exception block",msg)
else:
    print("inside else block")
finally:
    print("inside finally block")

try:
    lst=[1,2,3]
    print(lst[2])
finally:
    print("finally block")
#else:
#    print("inside else")

def func():
    print('func')
    x=2
    y=5
    print('multiplication of x and y',x*y)
func()


def func2(x,y):
    print('func2')
    print('x=',x,'y=',y)
    print('multiplication of x and y', x * y)

func2(5,3)
func2(y=5,x=3)

def func3(*args):
    print('func3')
    print(args)
    print(type(args))
    print('multiplication of 1st two args', args[0] * args[1])

func3(4,5,[1,2,3])
func3(4,[5,2],[1,2,3])
#func3(4,{5,2},[1,2,3])
#func3(4,{'id':1},[1,2,3])

def func4(**args):
    print('func4')
    print(args)
    print(type(args))
    print('multiplication of args with key x and y', args['x'] * args['y'])

func4(x=4,y=5,z=6)
func4(x=4,y=[5],z=6)

print("*** lambda examples ***")
xyz=lambda x:x+10
print(xyz(5))

lst=[4,5,6]
xy=list(map(lambda x:x+3,lst)) # logic applied values
print(xy)
xy_m=list(map(lambda x:x>3,lst)) # logic applied boolean
print(xy_m)
xyz_f=list(filter(lambda x:x+4,lst)) # logic eligible values
print(xyz_f)
xy_f=list(filter(lambda x:x>4,lst)) # condition eligible values
print(xy_f)

def f1(a):
    b=a+2
    def f2(b):
        return b*a
    return f2

print(f1(5))
f=f1(3)
print(f(4))

lst=[range(2,12)]
print(lst)