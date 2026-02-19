numbers=[10,20,30,40,50,60,70,80,90,100]
even=[]
odd=[]
for i in range(0,len(numbers),2):
    print(numbers[i],end=" ")
print()
for i in range(1,len(numbers),2):
      print(numbers[i],end=" ")

l=len(numbers)
for i in range(l):
   if numbers[i]==70:
        print("Found at: ",i)
      break
else:
      print("not found")
flag=False
n=[]
k=int(input())
for i in range(len(numbers)):
   if numbers[i]==k:
        flag=True
        ans=i
        n.append(i)
if flag==True:
    print("Found at:",ans)
else:
    print("not found")
print(n)
