'''Create an input based List'''

def makeList(x):
    #get input based on how many times you want the for loop to run
    numberOfTimes = int(input('How many items are there? '))
    print('Enter your value: ')
    
    #run i x number of times. x = the variable numberOfTimes
    for i in range(numberOfTimes):
        userInput = input()
        #add the input to the desired list x
        x.append(userInput)

#empty list to be used as storage        
list1 = []

#call the function 
makeList(list1)

#print the created list
print(list1)

