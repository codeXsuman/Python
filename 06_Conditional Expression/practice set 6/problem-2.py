# 2.Write a program to find out whether a student has passed or failed if it requires a total of 40% and at least 33% in each subject to pass. Assume 3 subjects and take marks as an input from the user.

sub1 = int(input("Enter marks of subject 1:"))
sub2 = int(input("Enter marks of subject 2:"))
sub3 = int(input("Enter marks of subject 3:"))

if (sub1<0 or sub1>100 or sub2<0 or sub2>100 or sub3<0 or sub3>100):
    print("Invalid input, marks should be between 0 to 100")

elif (sub1<33 or sub2<33 or sub3<33):
    print("you have failed.")

elif ((sub1+sub2+sub3)/3 <40):
    print("you have failed.")

else:
    print("you have passed.")