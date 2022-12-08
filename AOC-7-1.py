#B Cutten
#Dec 7, 2022
#adventofcode.com Day 7 - No Space Left On Device


#use a dictionary to store the file structure
root = {"parent":{}, #the directory above this one
        "name": "root", #the name of the directory
        "children":[], #a list of children directories
        "data":[]} #the files stored in this directory
current_node = root

#figure out what the current command is
def parse_command(line):
    
    global current_node #get access to the global varible (not good?)
    
    #turn the line into a list of items
    line = line.split()
    #first check if it's a command to change directory
    if(line[0] == "$" and line[1] == "cd"):
        
        #which directory to change to?
        if(line[2] == "/"):
            current_node = root
        elif(line[2] == ".." and current_node["name"] != "root"):
            #change to parent directory
            current_node = current_node["parent"]
        else: #change to a child of this directory
            
            #loop through all children directories
            for child in current_node["children"]:
                #did we find the matching name?
                if child["name"] == line[2]:
                    #change to that directory
                    current_node = child                             
    elif(line[0] == "$" and line[1] == "ls"):
        #do nothing?
        a = 1 
    elif(line[0] == "dir"):
        #creata a child and add to this directory
        child = {"parent": current_node,
                 "name": line[1], 
                 "children": [],
                 "data": []}
        current_node["children"].append(child)
    else: #the line must be a file, add to the data list of this directory
        current_node["data"].append(line)

#build a string out of the file system recursively
#useful for debugging
#formatting isn't the best
def print_files(directory):
    msg = ("Name: " + directory["name"] + "\n")
    msg += "\t"
    #add all the data
    for data in directory["data"]:
        msg += str(data) + "\n\t"
    #add the names of the sub directories
    msg += "Children: "
    for child in directory["children"]:
        msg += child["name"] + "\t"
    #now add the full printout of each sub directory
    msg+="\n"
    for child in directory["children"]:
        msg += print_files(child) + "\n"
        
    return msg

#counter for all of the directories with sizes of at most 100000
total_size = 0  
#find the sum of the current directory
def find_sum(directory):
    size = 0
    #start by adding all of the data it contains
    for data in directory["data"]:
        size += int(data[0])
    #now add all of the data it's children contain
    for child in directory["children"]:
        size += find_sum(child)
    #check if this meets the critera to be added to the total
    if size <= 100000:
        global total_size #bad? not sure how else to do this
        total_size += size
    return size
    


done = False #control the file reading loop

#open the input file
with open('input7.txt') as f:
    
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #find the location of the first marker
            parse_command(line)
    #print(print_files(root))
    #now the entire file structure is built, we can find the the sum of the total sizes of those directories with size at most 100000
    print(find_sum(root))
    print(total_size)