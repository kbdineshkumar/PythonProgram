# 26. Write a program using for loop to print even numbers and odd numbers in the below range of data (generate using range function) [5,6,7,8,9,10,11,12,13,14,15,
# 16,17,18,19,20] output should be with even as 6,8,10,12,14,16,18,20 and odd as 5,7,9,11,13,15,17,19.

lst=list(range(5,21))
print(lst)
even=[]
odd=[]
for i in lst:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
print('even no. are:',even)
print('odd no. are:',odd)

# 27. Write a while loop to loop from 0 till 21 with the increment of 3, the result should be exactly 3,6,9,12,15,18 and store this result in a list
lst=list(range(21))
res=[]
print(lst)
for i in lst:
    if i>0 and i%3==0:
        res.append(i)

print('results: ',res)

# 28. Write a for or while loop to print the cube of 4, result should be 4*4*4=64 (initiate some variable outside the loop with 4 and loop through 3 times to achieve the result)
x=4
i=1
cube=1
while(i<=3):
    cube=cube*x
    print(x)
    i+=1
print(cube)

#  Create a list as sal_lst=[10000,20000,30000,10000,15000], loop through the list and add 1000 bonus to the salary and store in another list sal_bonus_lst=[11000,21000,31000,11000,16000]
# then store the bonus applied salary in another list where sal>11000

sal_lst=[10000,20000,30000,10000,15000]
print('salary list: ',sal_lst)
sal_bonus_lst=[]
sal_bonus_lst1=[]
for i in sal_lst:
    x=i+1000
    sal_bonus_lst.append(x)
    if x>11000:
        sal_bonus_lst1.append(x)

print('bonus applied sal: ',sal_bonus_lst)
print('bonus applied sal with > 11000: ',sal_bonus_lst1)

x=int(input('enter the no: '))
i=0
while True:
    print("Inceptez technologies")
    if(i == x):
        break
    i+=1

# lst1=[[10,20],[30,40,50],[60,70,80]], calculate the sum of all number, calculate the min value and the max value of all the elements in the lst1.
lst1=[[10,20],[30,40,50],[60,70,80]]
t=0
comb=[]
for i in lst1:
    for j in i:
        t+=j
        comb.append(j)

print('total sum of all number:', t)
comb.sort()
print('min value',comb[0])
print('max value',comb[-1])

# 32. Create a looping construct to create 3 tables upto 10 values. Output should be like this…
for i in list(range(1,11)):
    print(i,'x 3 =',i*3)