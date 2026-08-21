n = int(input("Write a number: "))
sum=0
for i in range(1,n+1,1):
    sum=sum+i
print("The sum is :",sum)
#Revesed a String
string=input("Write a String: ")
string11=("")
for i in string:
    string11=i+string11
print("\n Original Version",string)
print("\n Revesed Version",string11)