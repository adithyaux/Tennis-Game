scores={}
points={0:0,1:15,2:30,3:40,4:"40+1",5:"40+1+1"}
setWinner=[]
setScore={"set1":[],"set2":[],"set3":[]}
gameWinner=[]

#Function to find the winner of the match.
def calculate_matchwinner(player1,player2):

    if setWinner.count(player1) > setWinner.count(player2):
        return player1
    elif setWinner.count(player1) < setWinner.count(player2):
        return player2

#Function to find the winner of a single set.
def calculate_set_winner(player1,player2):

    if gameWinner.count(player1) >= 6 and (gameWinner.count(player1)-gameWinner.count(player2))  >= 2:
        return player1
    elif gameWinner.count(player2) >= 6 and (gameWinner.count(player2)-gameWinner.count(player1))  >= 2:
        return player2
    else:
        return ""

#Function to find the winner of each game in the set.
def calculate_game_winner(player1,player2):
    print(scores[player1],scores[player2])
    if scores[player1] == 4 and scores[player2] == 4:
       scores[player1]=3
       scores[player2]=3
    if scores[player1] >=4 and (scores[player1]-scores[player2]) >= 2:
        return player1
    elif scores[player2] >=4 and (scores[player2]-scores[player1]) >= 2:
        return player2
    else:
        return ""
#Obtaining input from user
player1=input("Enter the name of player 1:")
player2=input("Enter the name of player 2:")
message="Who starts the first serve?(1 for {}, 2 for {})".format(player1,player2)
scores[player1]=0
scores[player2]=0

firstServe=input(message)
while True:
 text = input("Waiting for the game to start(Hit Enter)")
 if text == "":
    i=1
    message="Winner of next point(1 for {}, 2 for {})".format(player1,player2)

    while i<4:
      point=input(message)
      try:
        if int(point) == 1:

          score=scores[player1]+1

          scores[player1]=score
        elif int(point) == 2:

          score=scores[player2]+1

          scores[player2]=score

      except ValueError:
           print("Enter 1 or 2 as option")
           continue
      if scores[player1] >= 4 or scores[player2] >= 4:

        winner=calculate_game_winner(player1,player2)
        if winner != "":
          print("Game over")
          print("Current Score")
          print("-------------------------------------------")
          print("Set\t1\t2\t3")
          print("-------------------------------------------")
          player1score=""
          player2score=""
          if i == 2:

                player1score+="%s\t%s"%(player1,setScore["set1"][0])
                player2score+="%s\t%s"%(player2,setScore["set1"][1])
          elif i == 3:

                player1score+="%s\t%s\t%s"%(player1,setScore["set1"][0],setScore["set2"][0])
                player2score+="%s\t%s\t%s"%(player2,setScore["set1"][1],setScore["set2"][0])
          if winner == player1:

            print(player1score+"\t"+str(gameWinner.count(player1)+1))
            print(player2score+"\t"+str(gameWinner.count(player2)))
            gameWinner.append(player1)
          else:
            print(player1score+"\t"+str(gameWinner.count(player1)))
            print(player1score+"\t"+str(gameWinner.count(player2)+1))
            gameWinner.append(player2)
          scores={player1:0,player2:0}
      print("Game Score %s-%s"%(str(points[scores[player1]]),str(points[scores[player2]])))


      if len(gameWinner) >=6:
          swinner=calculate_set_winner(player1,player2)
          if swinner != "":

             setWinner.append(swinner)
             setScore["set"+str(i)]=[gameWinner.count(player1),gameWinner.count(player2)]

             gameWinner=[]
             i+=1
    print("Match over. " + calculate_matchwinner(player1, player2)+" Wins!")
    break
 else:
    print("Press enter to begin the game")