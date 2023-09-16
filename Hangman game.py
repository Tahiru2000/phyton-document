#def hangman():
    #word= "DOG"
    #wrong_guesses=0
    #stages= ["","______","|  |","| 0","| /|\ ","| / \\", "|" ]
    #score_board= ['__']* len(word)
    #win=False
    #print('Welcome to Hangman')
    #while wrong_guesses < len(stages) - 1 :
        #print('\n')
        #guess= input("Guess letter:")
        #if guess in word:
            #score_board[word.index(guess)]=guess
        #else:
            #wrong_guesses += 1
        #print((' '.join(score_board)))
        #print('  \n'.join(stages[0: wrong_guesses + 1]))
        #if '__' not in score_board:
            #print('You win! The word was:')
            #win=True
            #break
    #if not win:
        #print(' \n' .join(stages[0: wrong_guesses]))
        #print('You lose!')
#hangman()


#def add  (x  ,  y):
   # """Returns x +y.
   # :param  x:  int first integer to be add.
    #:param   y:  int second integer to be add.
    #Return:  int  sum of  x and y.
    #"""
    #return 
#x +y

#mylist=["mango","apple","pear"]
#mylist.append("orange")
#print(mylist)

#mylist.pop(0)
#print(mylist)

#namelist=["tahiru","shaibu","gaff"]
#namelist[2]="kadiri" 
#print(namelist)
#print(len(namelist))
#namelist[0:3]
#print(namelist)

#my_tuple=("egg","yam","rice")
#"yam"  in my_tuple
#print(my_tuple)

#my_dict={"mango": "blue","banan":"red","orange":"white"}
#print(my_dict)
#my_dict.pop ("mango")
#print(my_dict)
#yearstarted="1989"
#creator="Guidvan"
#country="The Nethadland"
#my_string="pyton was created in {} by {} in  {}.". format(yearstarted,creator,country)

#print(my_string)
#firstname="Tahiru"
#lastname="Shaibu"
#my_string="my name is {} {}.".format(lastname,firstname)
#print(my_string)
#the_dog=["the",  "catch",  "the", "robbert"]
#one_string= "".join(the_dog)
#print(one_string)

#my_string="the cat jump over the dag."
#my_string=    my_string.replace("cat","lion")
#print(my_string)
 
#questions=["what is your name?"'\n' ,"what is your favorite food?"'\n' ,"which country are you from"'\n' ,"what is your question"]
#n = 0
#while True:
    #print( "Type q to quit")
    #answer= input(questions[n])
    #if answer == "q":
        #break
    #n+=1
    #if n>2:
        #n=0
#print(questions)
        
#def player():
    
    #process=0
    #score=["\___/","| |","/\/", "| 0","|"]
    #award="bell"
    #score_board=["___"] * len (award)
    #win= False
    #print("welcome to penalty")
    #while process< len (score)- 1:
        
        #print('\n')
        #start= input("throw the first the die."'\n')
        #if start in award:
            
            #score_board[award.index(start)] = start
        #else:
            #process+=1
            #print((''.join(score_board)))
            #print('\n'. join(score[0: process+1]))
        #if "___" not in score_board:
            #print("you win the game")
            #print('  '.join(score_board))
            #win= True
            #break  
        #if not win:
                
            #print('\n' .join(score[0 : process]))
            #print('you fail')
#player()

me=print("answer some quetions b4 u enjoy")
questions=["what is ur name \n","Are u part of UG48 group "'\n',"Do you take part in the presentation "'\n',"what is the part that u perform "'\n',
"did u pass" '\n', "fail no enjoyment"]
n=0
while True:
    print("Type q to quit")
    answer= input(questions[n])
    if answer =="q":
       break
    n+=1
    if n>4:    
        n=0
print(questions)
    

            
    
     
    