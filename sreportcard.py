#write a program to print student report card using {} operator and format()

sname=("Pratik Reddy");
srollno=11
eng=66
math=60
com=70
hin=77
phy=52
tmark=eng+math+com+hin+phy

print();
print("--------Report Card--------");
print();
print("Student Name = {}".format(sname),end="   |   ");
print("Student Roll Number = {}".format(srollno));
print("\nSubject Name    Marks");
print("\nEnglish \t{}".format(eng));
print("Hindi   \t{}".format(hin));
print("Mathematics   \t{}".format(math));
print("Computer   \t{}".format(com));
print("Physics   \t{}".format(phy));
print("Total Marks   \t{}".format(tmark));
print("Average Marks \t{}".format(tmark/5));