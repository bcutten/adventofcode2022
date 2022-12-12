#B Cutten
#Dec 12, 2022
#adventofcode.com Day 12 - Hill Climbing Algorithm

from collections import deque as queue

#displays a list of list of  as a grid, useful for debugging
def print_grid(height_map):
    msg = ""
    for line in height_map:
        for item in line:
            msg += str(item) + "\t"
        msg += "\n"
    print(msg)    
    
#convert a letter into it's numerical value
def get_value(letter):
    if letter == "E": #this is the target
        letter = "z" #it has elevation z
    asci = ord(letter)
    if asci >= 97: #lowercase
        return asci - 96 #a = 1
    else: #uppercase
        return asci - 38 #A = 27

#find the row and col of the S in the map
def find_start(height_map):
    for row in range(len(height_map)):
        for col in range(len(height_map[row])):
            if(height_map[row][col] == "S"):
                return row, col
    return -1, -1 #shouldn't get here                

#needs to be a BFS, help from https://www.geeksforgeeks.org/breadth-first-traversal-bfs-on-a-2d-array/
#also need to track the number of steps it takes to get to each place
def find_path_bfs(height_map, visited, start_row, start_col, distances):
    q = queue()
    #add the starting location to the q
    q.append((start_row, start_col))
    #remember that we've been here
    visited[start_row][start_col] = True
    #we start here so the distance is zero
    distances[start_row][start_col] = 0
    #now process all of the locations in the q
    while(len(q) > 0):
        #get the next location to check
        cell = q.popleft()
        row = cell[0]
        col = cell[1]
        #is this the place we're looking for?
        if(height_map[row][col] == "E"):
            return distances[row][col]
        else: #keep looking in the four other directions, if we can
            #check which directions are possible
            #for each one make sure we don't go out of bounds
            #also make sure we haven't already been here
            #finally make sure that the height isn't too much to climb
            current_height = get_value(height_map[row][col])
            #left?
            if((col - 1 >= 0) and (not visited[row][col -1]) and (get_value(height_map[row][col - 1]) <= current_height + 1)):
                #add this location to the list to check
                q.append((row, col - 1))
                #mark that it has been checked
                visited[row][col - 1] = True
                #update the number of steps it takes to get to that location
                distances[row][col - 1] = distances[row][col] + 1
            #right?
            if((col + 1 < len(height_map[row])) and (not visited[row][col  + 1]) and (get_value(height_map[row][col + 1]) <= current_height + 1)):
                #add this location to the list to check
                q.append((row, col + 1))
                #mark that it has been checked
                visited[row][col + 1] = True
                #update the number of steps it takes to get to that location
                distances[row][col + 1] = distances[row][col] + 1                
            #up?
            if((row - 1 >= 0) and (not visited[row - 1][col]) and (get_value(height_map[row - 1][col]) <= current_height + 1)):
                #add this location to the list to check
                q.append((row - 1, col))
                #mark that it has been checked
                visited[row - 1][col] = True   
                #update the number of steps it takes to get to that location
                distances[row - 1][col] = distances[row][col] + 1                
            #down?
            if((row + 1 < len(height_map)) and (not visited[row + 1][col]) and (get_value(height_map[row + 1][col]) <= current_height + 1)):
                #add this location to the list to check
                q.append((row + 1, col))
                #mark that it has been checked
                visited[row + 1][col] = True
                #update the number of steps it takes to get to that location
                distances[row + 1][col] = distances[row][col] + 1                
            
    return -1 #shouldn't get here

 #attempt at a recursive BFS without googling
 #this might have worked if I had included a distance count for each location
def find_path(height_map, visited, row, col, steps):
    #have we already been here?
    if(visited[row][col] == True):
        #stop searching this way
        return steps, visited
    #first mark that we're here
    visited[row][col] = True
    #are we at the end?
    if(height_map[row][col] == "E"):
        return steps, visited
    
    #check which directions are possible
    current_height = get_value(height_map[row][col])
    #left?
    if((col - 1 >= 0) and (not visited[row][col -1]) and (get_value(height_map[row][col - 1]) <= current_height + 1)):
        steps, visited = find_path(height_map, visited, row, col - 1, steps + 1)
       
    #right?
    if((col + 1 < len(height_map[row])) and (not visited[row][col  + 1]) and (get_value(height_map[row][col + 1]) <= current_height + 1)):
        steps, visited = find_path(height_map, visited, row, col + 1, steps + 1)    
    #up?
    if((row - 1 >= 0) and (not visited[row - 1][col]) and (get_value(height_map[row - 1][col]) <= current_height + 1)):
        steps, visited = find_path(height_map, visited, row - 1, col, steps + 1)    
    #down?
    if((row + 1 < len(height_map)) and (not visited[row + 1][col]) and (get_value(height_map[row + 1][col]) <= current_height + 1)):
        steps, visited = find_path(height_map, visited, row + 1, col, steps + 1)     
    
    return steps, visited

done = False #control the file reading loop
#open the input file
with open('input12.txt') as f:
    height_map = []
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #load the map from the file
            height_map.append((line.strip()))

    #first load the map
    print_grid(height_map)
    #find the starting point
    start_row, start_col = find_start(height_map)
    #make a parallel grid to track whether each location has already been visited
    visited = []
    for i in range(len(height_map)):
        row = []
        for j in range(len(height_map[i])):
            row.append(False)
        visited.append(row)
    #make another parallel grid to track whether distances to each location
    distances = []
    for i in range(len(height_map)):
        row = []
        for j in range(len(height_map[i])):
            row.append(0)
        distances.append(row)    
    #find the shortest path to the End
    steps = find_path_bfs(height_map, visited, start_row, start_col, distances)
    
    print_grid(visited)
    print_grid(distances)
    print(steps) 
