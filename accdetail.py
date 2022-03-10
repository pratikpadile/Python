#write a program to print customer account details in a bank using {} operator and format()

custaccnum=848381
custname=("Pratik Reddy");
balance=100000
intrest= 5

print("\n-------------Customer Details-----------");
print("\nCustomer Account Number = {}".format(custaccnum),end=' \t');
print("Customer Account Name = {}".format(custname));

print("Bank Balance = {}".format(balance));

tint=(balance/100)*(intrest)

print("Intrest      = {}".format(tint));
print("\n\t\t\tTotal Balance ${}".format(balance+tint));