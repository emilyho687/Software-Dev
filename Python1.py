print('hello') #1

# Python program to print list
# using for loop
#a = [1, 2, 3, 4, 5]
# printing the list using loop
#for x in range(len(a)):
#    print (a[x])
list(range(21)) #2
for x in range(21):
    print (x, end=' ')

#3 fibonacci sequence
a, b = 0, 1
while b < 400:
    print(b)
    a, b = b, a + b

#4 polygon
# Program: Sum of interior angles calculator
n = 6
sum = (n-2)*180
print(sum)
