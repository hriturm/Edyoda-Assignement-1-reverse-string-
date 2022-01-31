str1 = input("Please enter your Value to get a mirror Dimension: ")

str2 = ''

for i in str1:
    str2 = i + str2
    
print("Original = ", str1)
print("After = ", str2)