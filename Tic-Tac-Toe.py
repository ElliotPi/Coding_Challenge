# Elliot Pi

from random import randint

# Defining functions for the gameplay

# This shows the current status of the grid
def showCurrentGame():
    print(*lGame[0:3], sep = ' ')
    print(*lGame[3:6], sep = ' ')
    print(*lGame[6:9], sep = ' ')

# This prompts the player to place a mark 
def playGame_Player():
    bSquare_P = True
    while bSquare_P is True :   # The while loop makes sure that the player input is valid (advoiding overwritting marked positions)
        iSquare_P = int(input("Which square would you like to place your 'X'?(i.e. 0-8) "))
        if iSquare_P in dSquareNumbers :
            lGame[iSquare_P] = "X"
            dSquareNumbers.pop(iSquare_P) 
            bSquare_P = False
        elif iSquare_P < 0 or iSquare_P > 8 :
            print("Please enter valid number to place the mark in the grid(i.e. 0-8).") 
        else:
            print("The square is already occupied by the oppenent. Pick one that is not.")
    showCurrentGame()

# This makes the computer to place a mark 
def playGame_Computer():
    print("\nIt's now the computer's turn.")
    bSquare_C = True
    while bSquare_C is True : # Same logic as the player function
        iSquare_C = randint(0,8) # The computer just randomly choose the position to mark from the remaining spots
        if iSquare_C in dSquareNumbers :
            lGame[iSquare_C] = "O"
            dSquareNumbers.pop(iSquare_C)
            bSquare_C = False     
    showCurrentGame()

# This checks whether one of the eight possible wining row occurs
def winCheck():
    sResult = "No one wins. It's a tie."
    
    # First type of wining situation (Cross)
    lWining_P = ["X","X","X"]
    lWining_C = ["O","O","O"]
    if lGame[0:3] == lWining_P :
        sResult = "You won!"
    elif lGame[0:3] == lWining_C :
        sResult = "Computer won!"
    elif lGame[3:6] == lWining_P :
        sResult = "You won!"
    elif lGame[3:6] == lWining_C :
        sResult = "Computer won!"
    elif lGame[6:9] == lWining_P:
        sResult = "You won!"
    elif lGame[6:9] == lWining_C :
        sResult = "Computer won!"
    
    # Second type of wining situation (Up/Down)
    elif lGame[0] == lGame[3] == lGame[6] == "X":
        sResult = "You won!"
    elif lGame[0] == lGame[3] == lGame[6] == "O":
        sResult = "Computer won!"
    elif lGame[1] == lGame[4] == lGame[7] == "X":
        sResult = "You won!"
    elif lGame[1] == lGame[4] == lGame[7] == "O":
        sResult = "Computer won!"
    elif lGame[2] == lGame[5] == lGame[8] == "X":
        sResult = "You won!"
    elif lGame[2] == lGame[5] == lGame[8] == "O":
        sResult = "Computer won!"
    
    # Third type of wining situation (Diagoanlly)
    elif lGame[0] == lGame[4] == lGame[8] == "X":
        sResult = "You won!"
    elif lGame[0] == lGame[4] == lGame[8] == "O":
        sResult = "Computer won!"
    elif lGame[2] == lGame[4] == lGame[6] == "X":
        sResult = "You won!"
    elif lGame[2] == lGame[4] == lGame[6] == "O":
        sResult = "Computer won!"

    return sResult

# The main program 
def main():
    bContinue = True
    while bContinue == True : 
        # A dictionary of available squares 
        global dSquareNumbers
        dSquareNumbers = {0:0, 1:1, 2:2, 3:3, 4:4, 5:5, 6:6, 7:7, 8:8}
        
        # Setting up the grid of the game 
        global lGame
        lGame = []
        for i in range(0, 9):
            lGame.append("_")

        # A example list for the player to understand the structure
        lDemo = [0,1,2,3,4,5,6,7,8]
        print("\nThis is the number order for each square in the grid:")
        print(*lDemo[0:3], sep = ' ')
        print(*lDemo[3:6], sep = ' ')
        print(*lDemo[6:9], sep = ' ')

        # Ask the player if he/she wanna go first
        sAnswer = input("Wanna go first? (Y/N) ").upper()
        if (sAnswer == "Y") : # The situation that the player starts first
            sPlayer = input("You will be 'X' in the game. Please press 'X' ").upper()
            while sPlayer != "X" :
                sPlayer = input("You must use 'X' in the game. Please press 'X' to move on. ").upper() #Making sure the player is using X
            for turn in range(1,6) : 
                if turn < 3 : # The first 4 marks won't result a winner (2 by the player, 2 by the computer)
                    playGame_Player()
                    playGame_Computer()
                elif 3 <= turn < 5 : # Starting from the 5th mark, a winner might appear. Therefore wincheck each time after someone place a mark
                    playGame_Player()
                    if winCheck() ==  ("You won!") :
                        break
                    playGame_Computer()
                    if winCheck() ==  ("Computer won!") :
                        break
                elif turn == 5 : # The last mark will be placed by the starter
                    playGame_Player()

        elif (sAnswer == "N") : # The situation that the computer starts first. All the logic the same as above, but the order is in reverse.
            sPlayer = input("You will be 'X' in the game. Please press 'X' ").upper()
            while sPlayer != "X" :
                sPlayer = input("You must use 'X' in the game. Please press 'X' to move on. ").upper()
            for turn in range(1,6) :
                if turn < 3 :
                    playGame_Computer()
                    playGame_Player()
                elif 3 <= turn < 5 :
                    playGame_Computer()
                    if winCheck() ==  ("Computer won!") :
                        break
                    playGame_Player()
                    if winCheck() ==  ("You won!") :
                        break
                elif turn == 5 :
                    playGame_Computer()
        print(winCheck()) # This is checking whether a winner is resulted from the last (i.e. 9th) mark and display the final result (someone won or a tie)
        
        sRepeat = ''
        while sRepeat != ("Y" or "N") :
            sRepeat = input("Do you want to play again? (Y/N) ").upper() # Ask the user to play again or not
            if sRepeat == "Y" : # Yes? Then start over.
                main()
            elif sRepeat == "N" : # No? Thank the player and close the program
                print("Thank you for your participation. We'd love to see you soon!")
                bContinue = False
                break
            else: # Requires valid answer
                print("Please enter a valid answer, i.e. Y/N.")
                
# The program beings here       
main()
