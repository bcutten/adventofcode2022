#B Cutten
#Dec 1, 2022
#adventofcode.com Day 1- Calorie Counting

done = False #control the file reading loop

most_calories =  -1 #track the highest total calories an elf has
elf_calories = 0 #the number of calories the current elf has

#open the input file
with open('input.txt') as f:
    
    #keep going until the file is empty
    while not done:
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True
        elif line == "\n": #a blank line indicates the end of this elf's calorie data
            #did this elf have the most total calories?
            if elf_calories > most_calories:
                #save this total
                most_calories = elf_calories
            elf_calories = 0 #start counting at zero for the next elf
        else: #this line has a calorie value for the curren elf, so add to it's total
            elf_calories += int(line)
print(most_calories)
