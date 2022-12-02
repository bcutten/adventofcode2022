#B Cutten
#Dec 2, 2022
#adventofcode.com Day 2- Rock Paper Scissors



#caculate how much we scored this round
#X = lose = 0 
#Y = draw = 3 
#Z = win = 6

#Rock = 1
#Paper = 2
#Sciccors = 3
def calc_score(opp, result):
    score = 0
    if opp == "A": #rock
        if result == "X":#lose
            score += 0 + 3
        elif result == "Y": #draw
            score += 3 + 1
        else: #win
            score += 6 + 2
    elif opp == "B": #paper
        if result == "X":#lose
            score += 0 + 1
        elif result == "Y": #draw
            score += 3 + 2
        else: #win
            score += 6 + 3              
    else: #C = scissors
        if result == "X":#lose
            score += 0 + 2
        elif result == "Y": #draw
            score += 3 + 3
        else: #win
            score += 6 + 1               
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
            #get the desired result
            result = line[2]
            total_score += calc_score(opp, result)

print(total_score)