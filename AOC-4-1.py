#B Cutten
#Dec 4, 2022
#adventofcode.com Day 4- Camp Cleanup



#check if the pairs overlap
#return 1 if they do, 0 if they don't
def check_overlap(pairs):
    #first split the pairs into pair 1 and pair 2
    #using strip here to get rid of any newline characters
    pairs = pairs.strip().split(",")
    #each pair is a list with a start and an end value
    pair1 = pairs[0].split("-")
    pair2 = pairs[1].split("-")
    #print(pair1)
    #print(pair2)
    #check if the first pair is contained within the second
    if int(pair1[0]) >= int(pair2[0]) and int(pair1[1]) <= int(pair2[1]):
        #print("pair 1 is in pair 2")
        return 1
    elif int(pair2[0]) >= int(pair1[0]) and int(pair2[1]) <= int(pair1[1]): #or is the second pair contained in the first?
        #print("pair 2 is in pair 1")
        return 1
    else: #neither pair is contained within the other
        return 0

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