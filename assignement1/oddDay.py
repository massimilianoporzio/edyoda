input_string = input('Enter elements of a list separated by space ')
print("\n")
user_list = input_string.split()
odds = 0
evens = 0
for i in range(len(user_list)):
    n = int(user_list[i])
    if n % 2 == 0:
        evens = evens +1
    else:
        odds = odds +1 
print("Number of even numbers: ",evens)
print("Number of odd numbers: ",odds)
