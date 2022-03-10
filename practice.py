#Program ()

n= int(input("Enter a no.:"));
if n%2!=0:
    print("weird");

elif n%2==0 and (n in range(2,6)):
        print("Not weird");
        
elif n%2==0 and (n in range(6,20)):
        print("Not weird");
 
elif n%2==0 and (n>20):
    print("weird");
else:
    print("Not weird");

