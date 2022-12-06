#B Cutten
#Dec 6, 2022
#adventofcode.com Day 6 - Tuning Trouble

#identify the first position where the fourteen most recently received characters were all different
def find_message(line):
    
    #go through all the characters
    for i in range(len(line) - 14):
        message = ""
        #build a string of the next 14 characters
        for j in range(14):
            message += line[i + j]
        #convert the list of characters into a set, and see if it's length is 14 (meaning all different)
        #check if this and the next three characters are all different
        if (len(set(message)) == 14):
            return i + 14 #the current position plus the next 14
        
    
    #hopefully we won't ever return a 0 since there should be at least one message
    return 0

done = False #control the file reading loop

#open the input file
with open('input6.txt') as f:
    
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #find the location of the first message
            print(find_message(line))

