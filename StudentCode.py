#Luke has made a change
#Code for Student

#Prompt for student number
prompt = "Enter student number: " #prompt user
stuNum = input(prompt) #store student number
randNum = stuNum[5:9] #take last 4 digits of number and use for randomising

#Basic Randomiser (add all digits divide by amount of numbers)
for a in randNum:
    print(int(a))
    