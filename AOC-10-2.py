#B Cutten
#Dec 9, 2022
#adventofcode.com Day 10 - Cathode Ray Tube

#parse the operation and figure out what to do with it
def process_operation(command, x, cycle_num, output):
    if command == "noop": #don't change x, increment cycles
        cycle_num +=1
        #update the screen
        output = update_screen(x, cycle_num, output)        
    else: #it's an add command
        val = int(command.split()[1]) #get the amount to add to x
        #run two cycles, the order is important here
        cycle_num += 1 #start a cycle
        #update the screen
        output = update_screen(x, cycle_num, output)
        cycle_num += 1 #start a cycle
        #update the screen
        output = update_screen(x, cycle_num, output)
        x += val #update X (the sprite position)      
    return x, cycle_num, output

#update the screen based on the position being drawn and the sprite position
def update_screen(x, cycle_num, output):
    #each new line means we need to add another 40 pixels to X since it's only the position on the row
    offset = output.count("\n")
    offset = offset * 40
    x += offset
    #cycle 1 gets drawn at position 0, and cycle 40 gets drawn at position 39 in each row
    cycle_num -= 1
    
    #check which character should be drawn
    #the sprite is 3 pixels wide, centered at X
    if(abs(x - cycle_num) <= 1): #is the current position within 1 either way of the middle of the sprite?
        output += "#"
    else: #not drawing where the sprite currently is
        output += "."
    
    if((cycle_num + 1) % 40 == 0): #have we processed 40 cycles? here we add one back to counteract subtracting one above
        #add a new line to the ouput
        output += "\n"
    
    return output


done = False #control the file reading loop

#open the input file
with open('input10.txt') as f:
    x = 1 #register starts with a 1
    cycle_num = 0
    output = ""
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #process the instruction
            x, cycle_num, output = process_operation(line.strip(), x, cycle_num,  output)
    
    print(output)
    
    
