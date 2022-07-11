print("Inheritance")
class father:
    x=10
    def __int__(self):
        pass
    def land(self):
        return 10000

class mother:
    y=100
    def __int__(self):
        pass
    def cash(self):
        return 5000

# single inheritance
print("single inheritance")
class son(father):
    def __init__(self):
        self.a = self.x
    def fun1(self):
        return 10+self.land()

objson = son()
print(objson.a)
print(objson.fun1())

# multiple inheritance
print("multiple inheritance")
class sec_son(father,mother):
    def __init__(self):
        self.z=self.x+self.y
    def fun1(self):
        return self.land()+self.cash()+self.z

obj_sec_con=sec_son()
print(obj_sec_con.fun1())
print('x',obj_sec_con.x)
print('y',obj_sec_con.y)
print('z',obj_sec_con.z)

# multilevel inheritance
print("multilevel inheritance")
class gfather:
    def __init__(self):
        self.b=10
    def land(self):
        return 100

class father2(gfather):
    def __init__(self):
        super().__init__()
        self.c=5
    def cash(self):
        return 5000

class son3(father2):
    def __init__(self):
        super().__init__()
        self.y=3
    def func1(self):
        #return self.land()+self.cash()
        return self.b+self.c

obj_son3=son3()
print(obj_son3.y)
print(obj_son3.land())
print(obj_son3.cash())
print(obj_son3.func1())

print("Hierarchical")
class gmother:
    def __init__(self):
        self.x=10
        self.y=20
    def cash(self):
        return 200

class gson(gmother):
    def __init__(self):
        super().__init__()
        self.p=self.x
    def fun1(self):
        return self.cash()

class gdaughter(gmother):
    def __init__(self):
        super().__init__()
        self.p=self.y
    def fun1(self):
        return self.cash()

obj_gson=gson()
print(obj_gson.p)
print(obj_gson.cash())
print(obj_gson.fun1())

obj_daug=gdaughter()
print(obj_daug.p)
print(obj_daug.cash())
print(obj_daug.fun1())

print('Inheritance end')

print('*** Abstraction ***')
from abc import ABC,abstractmethod
class base_remote(ABC):
    def power(self):
        pass
    @abstractmethod
    def volume(self,a):
        pass
    def channel(self,x):
        pass

class tv_remote(base_remote):
    def volume(self,a):
        return a+5
    def channel(self,x):
        return x+1

#rm_obj=base_remote()
rem_obj=tv_remote()
print(rem_obj.volume(5))
print(rem_obj.channel(6))

print('*** Encapsulation ***')
class Bank:
    __locker=10000
    _manager='manger'
    reception='chair'
    def staff(self,x):
        self.x=self.__locker-x
        return self.x

objcust=Bank()
print(objcust.reception)
print(objcust._manager)
#print(objcust.__locker) # can't access the private member/attribute outside of the class
print(objcust.staff(1000))

class bstaff(Bank):
    def staff(self):
        return self._manager

print(bstaff().staff())

print('parameterized constructor')
class cls_c:
    def __init__(self,xx):
        print('init',self)
        self.x=xx
    def fun1(self,a,b):
        print(self)
        return a+b+self.x

clsobj=cls_c(10)
print(clsobj.fun1(5,7))

print('static method')
class cls_d:
    #xx=10
    def __init__(self):
        self.x=100
    @staticmethod
    def fun1(qname):
        if qname == 'grocery':
            return 1
            #return 1+cls_d.xx
        elif qname == 'stationary':
            return 2
        else:
            return 3

print(cls_d.fun1('grocery'))
obj_clsd=cls_d()
print(obj_clsd.fun1('medical'))
#print(obj_clsd.fun1('grocery'))

print('class method')

class cls_f:
    x=100
    def __init__(self):
        print('int',self)
        self.xx=2
    @classmethod
    def fun1(cls,qname):
        print(cls)
        if qname == 'grocery':
            return cls.x+1
        elif qname == 'stationary':
            return 2+cls().xx
        else:
            return 3

print('calling through direct class')
print(cls_f.fun1('grocery'))
print(cls_f.fun1('stationary'))
print(cls_f.fun1('medical'))

print('calling through object')
obj_clsf=cls_f()
print(obj_clsf.fun1('grocery'))
print(obj_clsf.fun1('stationary'))
print(obj_clsf.fun1('medical'))

print('overloading using multiple dispatch')
from multipledispatch import dispatch
@dispatch(int)
def oload(x):
    return x
@dispatch(int,int)
def oload(x,y):
    return x+y
@dispatch(str,str)
def oload(x,y):
    return x+' '+y

print(oload(3))
print(oload(3,5))
print(oload('hi','hello'))