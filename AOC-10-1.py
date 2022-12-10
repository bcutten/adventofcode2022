#B Cutten
#Dec 9, 2022
#adventofcode.com Day 10 - Cathode Ray Tube


#parse the operation and figure out what to do with it
def process_operation(command, x, cycle_num, signal_strength):
    if command == "noop": #don't change x, increment cycles
        cycle_num +=1
        #calc signal strength
        signal_strength = calc_signal_strength(x, cycle_num, signal_strength)        
    else: #it's an add command
        val = int(command.split()[1]) #get the amount to add to x
        #run two cycles, the order is important here
        cycle_num += 1 #start a cycle
        #update the signal strength
        signal_strength = calc_signal_strength(x, cycle_num, signal_strength)
        cycle_num += 1 #start a cycle
        #update the signal strength
        signal_strength = calc_signal_strength(x, cycle_num, signal_strength)
        x += val #update X      
    return x, cycle_num, signal_strength

#calculate and updated signal strength value
def calc_signal_strength(x, cycle_num, signal_strength):
    #add to signal strength if it's one of the special 6 values
    if((cycle_num + 20) % 40 == 0): #sum the strength at cycle 20, and every 40 after that
        signal_strength += cycle_num * x
        #print("STRENGTH", signal_strength)
    return signal_strength

done = False #control the file reading loop

#open the input file
with open('input10.txt') as f:
    x = 1 #register starts with a 1
    cycle_num = 0
    signal_strength = 0
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #process the instruction
            x, cycle_num, signal_strength = process_operation(line.strip(), x, cycle_num, signal_strength)
    print(signal_strength)    
    
    
