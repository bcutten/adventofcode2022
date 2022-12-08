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


#finds the highest scenic score in the forest
def find_high_score(forest):
    high = -1
    size = len(forest)
    #print_forest(forest)
    #check each tree in the forest, except the ones on the outside 
    for row in range(1, size - 1):
        for col in range(1, size - 1):
            left_score = 1
            right_score = 1
            down_score = 1
            up_score = 1
            #check trees to the right
            i = 1
            while(i + col < size): #keep going until we reach the edge
                
                if(forest[row][col] > forest[row][col + i]): #can we see over this tree?
    
                    right_score += 1 #add to score
                    i += 1 #check next tree
                    if(i + col == size): #don't count the final tree in the row though
                        right_score-=1
                else: #can't see over this tree
                    i = size #stop looking
            #print(row, col, right_score)    
            #check trees to the left
            i = 1
            while(col - i > -1): #keep going until we reach the left edge
                
                if(forest[row][col] > forest[row][col - i]): #can we see over this tree?
    
                    left_score += 1 #add to score
                    i += 1 #check next tree
                    if(col - i == -1): #don't count the final tree in the row though
                        left_score-=1
                else: #can't see over this tree
                    i = size #stop looking
                          
            #check trees below
            i = 1
            while(i + row < size): #keep going until we reach the edge
                
                if(forest[row][col] > forest[row + i][col]): #can we see over this tree?
    
                    down_score += 1 #add to score
                    i += 1 #check next tree
                    if(i + row == size): #don't count the final tree in the column though
                        down_score-=1
                else: #can't see over this tree
                    i = size #stop looking  
            #print(row, col, down_score) 
            #check trees above
            i = 1
            while(row - i > -1): #keep going until we reach the left edge
                
                if(forest[row][col] > forest[row - i][col]): #can we see over this tree?
    
                    up_score += 1 #add to score
                    i += 1 #check next tree
                    if(row - i == -1): #don't count the final tree in the column though
                        up_score-=1
                else: #can't see over this tree
                    i = size #stop looking           
            #calculate total scenic score
            score = left_score * right_score * up_score * down_score
            #is this this a new high score?
            if score > high:
                high = score
                #print(row, col, left_score, right_score, up_score, down_score)
      
     
        
    return high

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
    print(find_high_score(forest))
    
