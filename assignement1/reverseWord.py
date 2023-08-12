# Write a Python program that accepts a word from the user and reverse it.
'''
Sample Test Case



Input : Edyoda

output: adoydE
'''
inputWord = input("Please enter your word:")
print("Input: ",inputWord)
inputList = list(inputWord)
inputList.reverse()
print("Output: ", ''.join(inputList))