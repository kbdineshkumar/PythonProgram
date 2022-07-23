# 45. Create 2 classes, one class called mask and one more class called endecode
# 46. Inside the class mask create a private value as addhash=100 and a method hashMask(str) should return the hash of str+addhash value.
# For eg. If I pass hashMask("abc"+str(100)) it should return
# 6867843172862474341
# 47. Inside the class endecode create a private value as prefixstr=”aix” and a method revEncode(str) ={return the prefixstr+reverse of str value}
# 51. Create a decode function inside endecodeclass as revDecode and write a logic to decode the encoded string we got in step 50.

class mask:
    __addhash=100
    def __init__(self):
        pass
    def hashMask(self,st):
        return hash(st+str(self.__addhash))

class endecode:
    __prefixstr="aix"
    def __init__(self):
        pass
    def revEncode(self,st):
        return self.__prefixstr+("".join(reversed(st)))
    def revDecode(self,st):
        (pre,revst)=(st[0:3],st[3:])
        try:
            if pre==self.__prefixstr:
                return ("".join(reversed(revst)))
            else:
                raise Exception
        except Exception as msg:
            print("unable to decode as encoded string is incorrect")
