#B Cutten
#Dec 3, 2022
#adventofcode.com Day 3- Rucksacks


#convert an item (letter) into it's numerical value
def priority_value(letter):
    asci = ord(letter)
    if asci >= 97: #lowercase
        return asci - 96 #a = 1
    else: #uppercase
        return asci - 38 #A = 27

#determine the priority value of this rucksack
def calc_priority(line):
    #first split the rucksack into two compartments
    halfway = int(len(line) / 2)
    comp_0 = line[0:halfway]
    comp_1 = line[halfway:]
    #now go through each item in the first compartment
    for item in comp_0:
        #is it in the second compartment?
        if comp_1.find(item) >= 0:
           #this is the shared item, so find the priority value
            val = priority_value(item)
            #print(val) debug
            return val
    
    #hopefully we won't ever return a 0 since there should be at least one shared item
    return 0

done = False #control the file reading loop

priority_sum = 0

#open the input file
with open('input3.txt') as f:
    
    #keep going until the file is empty
    while not done:
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #compute priority value of this rucksack
            priority_sum += calc_priority(line)

print(priority_sum)