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

#find the common item in all three elves and return its value
def calc_priority(elf1, elf2, elf3):
    #now go through each item the first elf has
    for item in elf1:
        #do the other two have it as well?
        if elf2.find(item) >= 0 and elf3.find(item) >= 0:
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
            line2 = f.readline()
            line3 = f.readline()
            priority_sum += calc_priority(line, line2, line3)

print(priority_sum)