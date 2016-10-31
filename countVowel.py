# Paste your code into this box 

s = 'azcbobobegghakl'
string = input("Enter the string:")
count=0
for char in string:
    if char =='a' or char=='e' or char=='i' or char=='o' or char=='u':
        count+=1
if count==0:
    print("No vowels in the string "+string)
else:
    print("The number of vowels in the string " + "\'"+string+"\'" + " is " + str(count))