
a=str(input("Enter the Number To check for palindrome:"))
count=0
flag=0
if(len(a)%2==0):
    while(count<(len(a)/2)):
        if(a[count]!=a[len(a)-count-1]):
            flag=1
            break
        count=count+1
        
else:
    while(count<(len(a)/2)):
        if(a[count]!=a[len(a)-count-1]):
            flag=1
            break
        count=count+1


if(flag==0):
    print("The string is a palindrome")
else:
    print("The string is not a palindrome")
