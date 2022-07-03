import string
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