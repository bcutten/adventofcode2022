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

#move the head and update the tail position
def move_head(command, head_row, head_col, tail_row, tail_col):
    #split up the command into its two components
    direction = command[0]
    amount = int(command[1])
    for i in range(amount): #perform the operation this many times
        if(direction == "R"):
            head_col = head_col + 1
        elif(direction == "L"):
            head_col = head_col - 1
        elif(direction == "U"):
            head_row = head_row - 1
        else: #down
            head_row = head_row + 1
            
        tail_row, tail_col = update_tail(head_row, head_col, tail_row, tail_col)
        #mark that the tail was here
        grid[tail_row][tail_col] = "#"
    #print_grid(grid)
    
    return head_row, head_col, tail_row, tail_col

#update the tail position based on the head location
def update_tail(head_row, head_col, tail_row, tail_col):
    
    if(abs(head_row - tail_row) <= 1 and tail_col == head_col): #on the same col and 1 or less apart  
        #print("No move, same col", head_row, head_col, tail_row, tail_col)
        return tail_row, tail_col #don't move
    elif(abs(head_col - tail_col) <= 1 and tail_row == head_row): #in the same row and 1 or less apart  
        #print("No Move, same row", head_row, head_col, tail_row, tail_col)
        return tail_row, tail_col #don't move 
    elif(abs(head_col - tail_col) <= 1 and abs(tail_row - head_row) <=1): # 1 or less apart in both row and col
        #print("No Move, diagonally only 1 apart", head_row, head_col, tail_row, tail_col)
        return tail_row, tail_col #don't move         
    else: #tail needs to move
        #are they in the same col?
        if(head_col == tail_col):
            #up or down?
            if(head_row < tail_row): #move up
                tail_row -=1
                #print("Same col, move up", head_row, head_col, tail_row, tail_col)
            else: #move down
                tail_row +=1
                #print("Same col, move down", head_row, head_col, tail_row, tail_col)
        elif(head_row == tail_row): #same row?
            #left or right?
            if(head_col < tail_col): #left
                tail_col -= 1
                #print("Same row, move left", head_row, head_col, tail_row, tail_col)
            else: #right
                tail_col +=1
                #print("Same row, move right", head_row, head_col, tail_row, tail_col)
        else: #one of the four diagonal moves is required
            if(head_row < tail_row and head_col < tail_col): #up and left
                tail_row -= 1
                tail_col -= 1
                #print("Diff row and col, move up/left", head_row, head_col, tail_row, tail_col)
            elif(head_row < tail_row and head_col > tail_col): #up and right
                tail_row -= 1
                tail_col += 1
                #print("Diff row and col, move up/right", head_row, head_col, tail_row, tail_col)
            elif(head_row > tail_row and head_col > tail_col): #down and right
                tail_row += 1
                tail_col += 1
                #print("Diff row and col, move down/right", head_row, head_col, tail_row, tail_col)
            else: #down and left
                #print("Pre move Diff row and col, move down/left", head_row, head_col, tail_row, tail_col)
                tail_row += 1
                tail_col -= 1
                #print("Post move Diff row and col, move down/left", head_row, head_col, tail_row, tail_col)
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
    #assume a 11 x 11 grid is large enough
    grid = make_grid(401)
    #start both ends of the rope in the middle
    head_row = 200
    head_col = 200
    tail_row = head_row
    tail_col = head_col 
    #mark the start position
    grid[head_row][head_col] = "#"
    #print_grid(grid)
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #find the location of the first message
            head_row, head_col, tail_row, tail_col = move_head(line.strip().split(), head_row, head_col, tail_row, tail_col)
            
    print_grid(grid)     
    print(count_visits(grid, 401))
    
