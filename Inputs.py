#5 Input problem
#Input function allows user input
# int(input())

#6 turn Q3 into Input

n = int(input("Enter value of n: "))
a, b = 1, 1
for i in range(n-2):
    print(b)
    a, b = a + b, b
print("The nth Fibonacci number is", b)

#n = int(raw_input())
#def printFib(n):
#    answer = [0] * (n+1) #creating a list to hold the answers
#    answer[1] = 1 #initializing the first values
#    for i in range(2, n + 1): answer[i] = answer[i - 1] + answer[i -2] #To get the 2nd number, add the two numbers before it
#    return answer
#print printFib(n)

#def fibonacci(n):
#    if n == 1:
#        return 1
#    elif n == 0:
#        return 0
#    else:
#        return fibonacci(n-1) + fibonacci(n-2)
#number = int(input("Enter an integer: \t"))
#for i in range(number):
#    print(fibonacci(i))

#num = int(input("enter number of digits you want in series: "))
#a, b = 0, 1
#print("\nfibonacci series: ")
#print(a, ",", b, end=", ")
#for i in range(2, num):
#    next = a +

#print('Enter one number: ')
#x = int(input('Enter a integer: '))
#x = input('Enter a integer: ')
#print('Integer is:', x)

#7 turn Q4 into input
n = int(input("Enter the number of sides on the polygon: "))
Sum = (n-2) * 180
#Display output
if Sum < 1:
    print("Error")
else:
    print("The total sum is " + str(Sum) + " degrees.")
