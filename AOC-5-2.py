#B Cutten
#Dec 5, 2022
#adventofcode.com Day 5 - Supply Stacks

done = False #control the file reading loop

#hardcoding the starting stacks
stack1 = ["S", "L", "W"]
stack2 = ["J", "T", "N", "Q"]
stack3 = ["S", "C", "H", "F", "J"]
stack4 = ["T", "R", "M", "W", "N", "G", "B"]
stack5 = ["T", "R", "L", "S", "D", "H", "Q", "B"]
stack6 = ["M", "J", "B", "V", "F", "H", "R", "L"]
stack7 = ["D", "W", "R", "N", "J", "M"]
stack8 = ["B", "Z", "T", "F", "H", "N", "D", "J"]
stack9 = ["H", "L", "Q", "N", "B", "F", "T"]

#put all stacks in a list so they are easier to deal with
#add an empty list at the stack so the numbers and the indexes line up
stacks = [[""],stack1, stack2, stack3, stack4, stack5, stack6, stack7, stack8, stack9]

#open the input file
with open('input5.txt') as f:
    
    #keep going until the file is empty
    while not done:
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #do this move on the appropriate stack
            #convert the string into a list
            line = line.split()
            #move 5 from 4 to 5
            #get the number from the list
            amount = int(line[1])
            from_stack = stacks[int(line[3])]
            to_stack = stacks[int(line[5])]
            
            #now move the requested number of boxes
            temp_list = [] #this will store the boxes being moved
            #take off this many boxes, storing in a new list            
            for i in range(amount):
                #grab the item from the end of the other stack and put it at the front of this list (keeping original order)
                temp_list = [from_stack.pop()] + temp_list
            #add the new list to the end of the old
            to_stack.extend(temp_list)
                
#now print the last item in each stack (i.e. the one on the top)
output = ""
for stack in stacks:
    output += stack[-1] #-1 is the last item in the list
print(output)