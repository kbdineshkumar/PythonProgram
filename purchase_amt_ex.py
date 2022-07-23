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