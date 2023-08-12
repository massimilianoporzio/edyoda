# Write a Python program to get the Fibonacci series between 0 to 50
# Every next number is found by adding up the two numbers before it.

# Expected Output : 1 1 2 3 5 8 13 21 34

fibonacciSeries=[]

fibonacci = 0
n = 0
while fibonacci < 50:
    if n <2:
        fibonacciSeries.append(n)
        fibonacci = fibonacciSeries[len(fibonacciSeries)-1]
        n = n + 1
        continue
    fibonacci = fibonacciSeries[len(fibonacciSeries)-1] +fibonacciSeries[len(fibonacciSeries)-2]
    if fibonacci < 50:
        fibonacciSeries.append(fibonacci)  
        n = n + 1
output = [x for x in fibonacciSeries if x>0]
[print(i, end=' ') for i in output]