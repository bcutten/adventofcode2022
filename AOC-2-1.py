#B Cutten
#Dec 2, 2022
#adventofcode.com Day 2- Rock Paper Scissors

#caculate how much we scored this round
def calc_score(opp, me):
    score = 0
    if me == "X": #rock
        score += 1
        if opp == "A": #rock
            score += 3
        elif opp == "C": #scissors
            score += 6
    elif me == "Y": #paper
        score += 2
        if opp == "A": #rock
            score += 6
        elif opp == "B": #paper
            score += 3        
    else: #scissors
        score +=3
        if opp == "B": #paper
            score += 6
        elif opp == "C": #scissors
            score += 3        
    return score

done = False #control the file reading loop

total_score = 0

#open the input file
with open('input2.txt') as f:
    
    #keep going until the file is empty
    while not done:
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #compute score of round
            #get oppononents move
            opp =  line[0]
            #get my move
            my_move = line[2]
            total_score += calc_score(opp, my_move)

print(total_score)