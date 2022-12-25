'''Create an input based List'''

#initialize an empty list which we will use as storage
emptyList = []

#get input based on how many times you want the for loop to run
numberOfTimes = int(input('How many times would you like me to run? '))

#for loop to run i x times, x being the variable numberOfTimes
print('Enter your value: ')
for i in range(numberOfTimes):
    userInput = input()
    #append the input from userInput to emptyList
    emptyList.append(userInput)

print('List: ',emptyList)

