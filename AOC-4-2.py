#B Cutten
#Dec 4, 2022
#adventofcode.com Day 4- Camp Cleanup

#check if any part of the pairs overlap
#return 1 if they do, 0 if they don't
def check_overlap(pairs):
    #first split the pairs into pair 1 and pair 2
    #using strip here to get rid of any newline characters
    pairs = pairs.strip().split(",")
    #each pair is a list with a start and an end value
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    #check if the first pair does not overlap with the second
    #first the case where the pair 1 is smaller
    if int(pair1[1]) < int(pair2[0]):
        return 0
    elif int(pair2[1]) < int(pair1[0]): #next the case where pair 2 is smaller
        return 0
    else: #one part must overlap
        return 1

done = False #control the file reading loop

overlapping_pairs = 0

#open the input file
with open('input4.txt') as f:
    
    #keep going until the file is empty
    while not done:
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #check if the line contains an overlapping pair
            overlapping_pairs += check_overlap(line)

print(overlapping_pairs)