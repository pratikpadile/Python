#Program (ForLoopEx1.py)

'''
s1= "Hello world";
for x in s1:
	print(x);
print("End OF THE LOOP");


s1="Hello world";
i=0;
for x in s1:
        print("index",i,"char is",x);
        i=i+1;
print("End Of The Loop");


#with range() funcion
for x in range (10):
        print("sai","/t",x+1);
print("End of the Loop");


for x in range(10):
        print(x+2);
print("end of the Loop");
'''
'''
#Even & Odd Number :
num=int(input("Enter any number : "));
print("Even Number : ");
for x in range (num):
    if(x%2==0 and x!=0):
        print(x);
       
num=int(input("Enter any number : "));
print("Odd Number :");
for x in range(num):
    if(x%2!=0):
        print(x);

        
#Range () with step-value
for x in range (10,20,2):
        print(x);
print("End Of The Loop");

for x in range (10,0,-1):
        print(x);
print("End Of The Loop");


#Sum Of Naturals Numbers
sum=0;
for x in range (5):
    print(sum);
    sum=sum+x+1;
print("sum",sum);
'''
