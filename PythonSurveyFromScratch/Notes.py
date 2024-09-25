def checkstatus(listXO,playerwin,XOwin):
    global win, sheet, gone, listx, listo
    #checks if there is a winner
    if 1 in listXO and 2 in listXO and 3 in listXO:
        winspeak(playerwin,XOwin) #vertical
    elif 4 in listXO and 5 in listXO and 6 in listXO:
        winspeak(playerwin,XOwin) #vertical
    elif 7 in listXO and 8 in listXO and 9 in listXO:
        winspeak(playerwin,XOwin) #vertical
    elif 1 in listXO and 4 in listXO and 7 in listXO:
        winspeak(playerwin,XOwin) #horizontal
    elif 2 in listXO and 5 in listXO and 8 in listXO:
        winspeak(playerwin,XOwin) #horizontal
    elif 3 in listXO and 6 in listXO and 9 in listXO:
        winspeak(playerwin,XOwin) #horizontal
    elif 1 in listXO and 5 in listXO and 9 in listXO:
        winspeak(playerwin,XOwin) #diagonal
    elif 3 in listXO and 5 in listXO and 7 in listXO:
        winspeak(playerwin,XOwin) #diagonal
      
    if (len(listx) + len(listo)) == 9: #checks for tie
        print("\nNeither player wins, thats a tie!")
        print("Player 1:",xscore,"\nPlayer 2:",oscore)

        while True:
            keep = input("Continue? (y/n)\n > ")
            if keep == "y":
                win = "h"
                sheet = "|1|2|3|\n|4|5|6|\n|7|8|9|"
                gone = []
                multigame()
            elif keep == "n":
                quit()

def winspeak(player,XOwin): #winner
    global win, sheet, gone, xscore, oscore
    win == XOwin
    print("\n"+player+" wins!\n")

    #increases winner's score
    if player == "Player 1": 
        xscore += 1
    elif player == "Player 2": 
        oscore += 1
    print("Player 1:",xscore,"\nPlayer 2:",oscore)

    while True:
        keep = input("Continue? (y/n)\n > ")
        if keep == "y":
            win = "h"
            sheet = "|1|2|3|\n|4|5|6|\n|7|8|9|"
            gone = []
            multigame()
        elif keep == "n":
            quit()

def play(XO,player,listXO):
    global sheet, listx, listo
    while True:
        num = input(player+" enter an available number where you want to put an "+XO+".\n > ")

        try:
            num = int(num)
        except ValueError:
            print("Not a valid number, try again.")
            continue
        if num < 1 or num > 9:
            print("Number not in correct range, try again.")
            continue
        if num in gone:
            print("Number already used, try again.")
            continue
    
        gone.append(num)
        listXO.append(num)
        sheet = sheet.replace(str(num),XO)
        print(sheet)
        break

def game(): #one game
    global gone, listx, listo, sheet, win, turn, xscore, oscore
    win = "h"
    sheet = "|1|2|3|\n|4|5|6|\n|7|8|9|"
    print(sheet)
    turn = 0
    xscore = 0
    oscore = 0
    gone = []
    listx = []
    listo = []
    while True:
        while win != "Xwin" or win != "Owin": #plays the game and checks for winner
            if turn % 2 == 0:
                play("X","Player 1",listx)
                checkstatus(listx,"Player 1","Xwin")
            elif turn % 2 == 1:
                play("O","Player 2",listo)
                checkstatus(listo,"Player 2","Owin")
            turn += 1

def multigame(): #many games
    while True:
        game()

multigame()