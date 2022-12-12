#B Cutten
#Dec 11, 2022
#adventofcode.com Day 11 - Monkey in the Middle

#define a monkey
class Monkey:
  #this makes a new monkey and stores the attributes
  def __init__(self, number, items, modifier, sign, divisor, throw_1, throw_2, num_inspected):
    self.number = number
    self.items = items
    self.modifier = modifier
    self.sign = sign
    self.divisor = divisor
    self.throw_1 = throw_1
    self.throw_2 = throw_2
    self.num_inspected = num_inspected
  
  #when a monkey inspects an item
  def inspect(self, item_num):
    self.num_inspected += 1
    #some monkeys will add to worry, some will multiply
    if(self.sign == "+"):
      self.items[item_num] = int(self.items[item_num]) + int(self.modifier)
    else:
      if(self.modifier == "old"):
        self.items[item_num] = int(self.items[item_num]) * int(self.items[item_num])
      else:
        self.items[item_num] = int(self.items[item_num]) * int(self.modifier)
  
  #check where this monkey throws the item next
  def throw(self, item_num):
    if(int(self.items[item_num]) % int(self.divisor) == 0):
      return self.throw_1
    else:
      return self.throw_2
   
  #make the monkey into a String for printing  
  def __str__(self):
    return "Monkey #" + str(self.number) + "\n" + "Items: " + str(self.items) + "\nOperation: " + self.sign + " " + str(self.modifier) + "\n" + "True to monkey " + str(self.throw_1) + " false to monkey " + str(self.throw_2) + "\nInspected " + str(self.num_inspected)
  

done = False #control the file reading loop

#open the input file
with open('input11.txt') as f:
    monkeys = [] #keep all of the monkeys in a list
    
    #keep going until the file is empty
    while not done: #the loop will only run once this time
        #read one line
        line = f.readline()
        #are we at the end of the file?
        if not line:
            done = True        
        else: #create a Monkey object
            #first line is the monkey number
            line = line.split()
            number = int(line[1][0])
            #second line is the list of items
            line_2 = f.readline().split()
            line_2.remove("Starting")
            line_2.remove("items:")
            #add each number to the a new list 
            items = []
            for item in line_2:
                #all of the items are 2 digit number, but some in this list may have a comma at the end
                if len(item) == 2:
                    items.append(int(item))
                else: #there's a comma so just grab the first two characters
                    items.append(int(item[0:2]))
            #third line is the operation
            line_3 = f.readline().split()
            sign = line_3[4]
            modifier = line_3[5]
            #fourth line is divisor
            line_4 = f.readline().split()
            divisor = line_4[3]
            #fifth line is the true test
            line_5 = f.readline().split()
            throw_1 = int(line_5[5])
            #sixth line is the falst test
            line_6 = f.readline().split()
            throw_2 = int(line_6[5])    
            #seventh line is blank
            f.readline()
            m = Monkey(number, items, modifier, sign, divisor, throw_1, throw_2, 0)
            #print(m)
            monkeys.append(m)
    for r in range(20):
      #the monkeys now take turns inspecting and throwing items
      for m in monkeys:
          #the monkey inspects one of its items at a time
          for i in range(len(m.items)):
              m.inspect(i)
              #print(m.items[i])
              #relief that the item wasn't damaged divides worry by 3
              m.items[i] = int(m.items[i]) // 3 #integer division
              recipient = m.throw(i) #check which monkey to throw the item to
              #add the item to the other monkeys item list
              monkeys[recipient].items.append(m.items[i])
          #a monkey throws all of it's items each round, so remove them all
          m.items = []
            
    
    #now find two most active monkeys
    #assume the first one is the most active
    high_1 = monkeys[0]
    high_2 = monkeys[0]
    #check the rest
    for i in range(1,len(monkeys)):
      #is this a new high?
      if(monkeys[i].num_inspected > high_1.num_inspected):
        #move the old high down
        high_2 = high_1
        #save the new high
        high_1 = monkeys[i]
      elif(monkeys[i].num_inspected > high_2.num_inspected): #a new second place?
        high_2 = monkeys[i]
    #now print the product of the inspections
    print(high_2.num_inspected * high_1.num_inspected)
    
    
