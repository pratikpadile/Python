#Program (NumberSwapping1.py)

a=int(input("Enter A Number : "));
b=int(input("Enter B Number : "));
print("\nValue of A Is {} \nValue of B Is {} ".format(a,b));
temp_num=a;
a=b;
b=temp_num;
print("\n*** After Swapping ***")
print("\nValue of A Is {} \nValue of B Is {} ".format(a,b));
