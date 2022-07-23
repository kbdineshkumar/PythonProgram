# 48. Create another module inside the same package and create an object namely objmask to instantiate the class mask
# and objendecode to instantiate the class endecode
# 49. Create a list with 3 names like [“arun”,”ram kumar”,”yoga murthy”], loop the elements using map function and apply hashMask for all 3 elements and print the masked values.
# 50.  Loop the list created in the above step and apply the revEncode function for all the 3 elements and print of the encoded values.
# 51. Create a decode function inside endecodeclass as revDecode and write a logic to decode the encoded string we got in step 50.

from oops import mask,endecode

objmask=mask()
lst=["arun","ram kumar","yoga murthy"]
lst_res=list(map(objmask.hashMask,lst))
print(lst_res)

objendecode=endecode()
enc_res=list(map(objendecode.revEncode,lst))
print(enc_res)

dec_res=list(map(objendecode.revDecode,enc_res))
print(dec_res)