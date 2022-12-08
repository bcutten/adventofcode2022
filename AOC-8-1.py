#B Cutten
#Dec 8, 2022
#adventofcode.com Day 8 - Treetop Tree House


#takes a line of String numbers and turns it into a list of number
def make_int_list(line):
    int_list = [] 
    #go through each number in the line, turn into an int, and add to new list
    for number in line:
        int_list.append(int(number))
    return int_list

#displays a list of list of ints as a grid, useful for debugging
def print_forest(forest):
    msg = ""
    for trees in forest:
        for tree in trees:
            msg += str(tree) + "\t"
        msg += "\n"
    print(msg)    
    
done = False #control the file reading loop


#checks to see which trees are visible from the outside of the forest
def count_visible(forest):
    count = 0
    size = len(forest)
    #make a parallel grid to track whether each tree has already been counted
    #need this since we're checking from all side
    counted = []
    for i in range(size):
        row = []
        for j in range(size):
            row.append(False)
        counted.append(row)
       
    #check each row left to right
    for row in range(size):
        tallest = -1 #track the tallest tree so far in the row
        for col in range(size):
            if(forest[row][col] > tallest): #this tree can be seen
                tallest = forest[row][col] #save the new tallest
                if(not counted[row][col]): #only count if we haven't done so already
                    count +=1
                    counted[row][col] = True #remember that we already counted this one
      
    
    #check each row right to left
    for row in range(size):
        tallest = -1 #track the tallest tree so far in the row
        for col in range(size - 1, -1, -1):
            if(forest[row][col] > tallest): #this tree can be seen
                tallest = forest[row][col] #save the new tallest
                if(not counted[row][col]): #only count if we haven't done so already
                    count +=1
                    counted[row][col] = True #remember that we already counted this one  
    
    
    #check each col top to bottow
    for col in range(size):
        tallest = -1 #track the tallest tree so far in the column
        for row in range(size):
            if(forest[row][col] > tallest): #this tree can be seen
                tallest = forest[row][col] #save the new tallest
                if(not counted[row][col]): #only count if we haven't done so already
                    count +=1
                    counted[row][col] = True #remember that we already counted this one
                    
    #check each col bottom to top
    for col in range(size):
        tallest = -1 #track the tallest tree so far in the column
        for row in range(size - 1, -1, -1):
            if(forest[row][col] > tallest): #this tree can be seen
                tallest = forest[row][col] #save the new tallest
                if(not counted[row][col]): #only count if we haven't done so already
                    count +=1
                    counted[row][col] = True #remember that we already counted this one  
        
    return count

#open the input file
with open('input8.txt') as f:
    forest = []
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #find the location of the first message
            forest.append(make_int_list(line.strip()))

    #forest has been grown, print to make sure it worked
    #print_forest(forest)
    #now find the number of visible trees in the forest
    print(count_visible(forest))
    
