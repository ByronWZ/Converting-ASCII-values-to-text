#variable called nums
nums = [112, 105, 99, 111, 67, 84, 70, 123, 103, 48, 48, 100, 95, 107, 49, 116, 116, 121, 33, 95, 110, 49, 99, 51, 95, 107, 49, 116, 116, 121, 33, 95, 55, 99, 48, 56, 50, 49, 102, 53, 125, 10]
#Variable called flag
flag = ""
#for loop created to get a string representing of a character which points to a Unicode code integer with the chr() function
for number in nums:
    flag += chr(number)
print(flag)
