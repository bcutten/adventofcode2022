#B Cutten
#Dec 9, 2022
#adventofcode.com Day 9 - Rope Bridge

#displays a list of list of Strings as a grid, useful for debugging
def print_grid(grid):
    msg = ""
    for line in grid:
        for item in line:
            msg += str(item) + " "
        msg += "\n"
    print(msg)    

#start with an empty grid
def make_grid(size):
    grid = []
    for i in range(size):
        line = []
        for j in range(size):
            #each item in the grid is a dot
            line.append(".")
        grid.append(line)
    return grid

#move the head and update the rest of the rope accordingly
def move_head(command, rope_row, rope_col):
    #split up the command into its two components
    direction = command[0]
    amount = int(command[1])
    for i in range(amount): #perform the operation this many times
        if(direction == "R"):
            rope_col[0] = rope_col[0] + 1
        elif(direction == "L"):
            rope_col[0] = rope_col[0] - 1
        elif(direction == "U"):
            rope_row[0] = rope_row[0]- 1
        else: #down
            rope_row[0] = rope_row[0] + 1
        #update each of the other knots on the rope, one by one
        for i in range(1,10):
            rope_row[i], rope_col[i] = update_tail(rope_row[i-1], rope_col[i-1], rope_row[i], rope_col[i])
        #mark that the tail was here
        grid[rope_row[9]][rope_col[9]] = "#"
    return rope_row, rope_col

#update the tail position based on the head location
def update_tail(head_row, head_col, tail_row, tail_col):
    if(abs(head_row - tail_row) <= 1 and tail_col == head_col): #on the same col and 1 or less apart  
        return tail_row, tail_col #don't move
    elif(abs(head_col - tail_col) <= 1 and tail_row == head_row): #in the same row and 1 or less apart  
        return tail_row, tail_col #don't move 
    elif(abs(head_col - tail_col) <= 1 and abs(tail_row - head_row) <=1): # 1 or less apart in both row and col
        return tail_row, tail_col #don't move         
    else: #tail needs to move
        #are they in the same col?
        if(head_col == tail_col):
            #up or down?
            if(head_row < tail_row): #move up
                tail_row -=1
            else: #move down
                tail_row +=1
        elif(head_row == tail_row): #same row?
            #left or right?
            if(head_col < tail_col): #left
                tail_col -= 1
            else: #right
                tail_col +=1
        else: #one of the four diagonal moves is required
            if(head_row < tail_row and head_col < tail_col): #up and left
                tail_row -= 1
                tail_col -= 1
            elif(head_row < tail_row and head_col > tail_col): #up and right
                tail_row -= 1
                tail_col += 1
            elif(head_row > tail_row and head_col > tail_col): #down and right
                tail_row += 1
                tail_col += 1
            else: #down and left
                tail_row += 1
                tail_col -= 1
        return tail_row, tail_col 

#count how many number signs are in the grid
def count_visits(grid, size):
    count = 0
    for i in range(size):
        for j in range(size):
            if(grid[i][j] == "#"):
                count +=1
    return count     

done = False #control the file reading loop

#open the input file
with open('input9.txt') as f:
    #assume a 401 x 401 grid is large enough, discovered by trial and error
    grid = make_grid(401)
    #start all parts of the rope in the middle
    rope_row = []
    rope_col = []
    for i in range(10):
        rope_row.append(200)
        rope_col.append(200)
    #mark the start position
    grid[rope_row[9]][rope_col[9]] = "#"
    #print_grid(grid)
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #find the location of the first message
            rope_row, rope_col = move_head(line.strip().split(), rope_row, rope_col)
            
    print_grid(grid) #just for fun     
    print(count_visits(grid, 401)) 
    
