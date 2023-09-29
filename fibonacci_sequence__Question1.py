# Write a Python program to get the Fibonacci series between 0 to 50
max_value = int(input("Enter the maxium value for Fibonacci series:"))
a, b = 0, 1
Fibonacci_series = []
while a <= max_value:
    Fibonacci_series.append(a)
    a, b = b, a + b
print("Fibonacci series between 0 and {} using a while loop:".format(max_value))
print(Fibonacci_series)
     
