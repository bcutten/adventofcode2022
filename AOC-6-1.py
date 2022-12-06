#B Cutten
#Dec 6, 2022
#adventofcode.com Day 6 - Tuning Trouble

#identify the first position where the four most recently received characters were all different
def find_marker(line):
    
    #go through all the characters
    for i in range(len(line) - 4):        
        #check if this and the next three characters are all different
        if (line[i] != line[i + 1] and line[i] != line[i + 2] and line[i] != line[i + 3]) and (line[i + 1]  != line [i + 2] and line[i + 1]  != line [i + 3]) and (line[i + 2]  != line [i + 3]):
            return i + 4 #the current position plus the next 4 
            
    #hopefully we won't ever return a 0 since there should be at least one marker
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
        else: #find the location of the first marker
            print(find_marker(line))

