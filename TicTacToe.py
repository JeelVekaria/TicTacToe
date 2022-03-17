import pygame
pygame.init()

winner = False
width = 600
height = 700
window = pygame.display.set_mode((width,height))
wallpaper = pygame.image.load('assets/TicTacToeWallpaper.png')
circle = pygame.image.load('assets/TTTCircle.png')
notCircle = pygame.image.load('assets/TTTX.png')
teal = (0,100,100)
window.fill(teal)
window.blit(wallpaper,(0,100))

redWin = pygame.image.load('assets/redWin.png')
blueWin = pygame.image.load('assets/blueWin.png')

circ=True

#Board Coordinates

board = [   [0,0,0],
            [0,0,0],
            [0,0,0]     ]
boardCoord = [ 
    [(0,100),(200,100),(400,100)],
    [(0,300),(200,300),(400,300)],
    [(0,500),(200,500),(400,500)],

]

pygame.display.set_caption("TicTacToe")

#Circle's 1
#X's 2
# def setCircle(posX, posY):
#     board[posX][posY] == 1
# def setX(posX, posY):
#     board[posX][posY] == 2
def setMarker(x,y,z):

    if z==True:
        return 1
    else:
        return 2

def switch(x):
    if x==True:
        return False
    return True
def redWins():
    window.blit(redWin,(0,0))
    global winner
    winner = True
def blueWins():
    window.blit(blueWin,(0,0))
    global winner
    winner = True

def checkWinner(board):
    for i in range(3):
        #Checks all rows
        if board[i][0]==1 and board[i][1]==1 and board[i][2]==1:
            redWins()
            break
        if board[i][0]==2 and board[i][1]==2 and board[i][2]==2:
            blueWins()
            break
        #Checks all columns
        if board[0][i]==1 and board[1][i]==1 and board[2][i]==1:
            redWins()
            break
        if board[0][i]==2 and board[1][i]==2 and board[2][i]==2:
            blueWins()
            break
        # Checks all diagonal (top left to bottom right)
        if board[0][0]==1 and board[1][1]==1 and board[2][2]==1:
            redWins()
            break
        if board[0][0]==2 and board[1][1]==2 and board[2][2]==2:
            blueWins()
            break
        # Checks all diagonal (bottom left to top right)
        if board[0][2]==1 and board[1][1]==1 and board[2][0]==1:
            redWins()
            break
        if board[0][2]==2 and board[1][1]==2 and board[2][0]==2:
            blueWins()
            break
def updateBoard():
    for i in range(3):
        for k in range(3):
            if board[i][k] == 1:
                window.blit(circle, boardCoord[i][k])
            if board[i][k] == 2:
                window.blit(notCircle, boardCoord[i][k])
while True:
    for event in pygame.event.get():
        #Exit Game
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        posx, posy = pygame.mouse.get_pos()
        # print((posx,posy))
        keys = pygame.key.get_pressed()

        #Checks for one click
        if event.type == pygame.MOUSEBUTTONDOWN and winner==False:
            
            if posx>0 and posx<200 and posy>100 and posy<300 and board[0][0]==0:
                board[0][0] = setMarker(0,0,circ)
                circ = switch(circ)

            if posx>200 and posx<400 and posy>100 and posy<300 and board[0][1]==0:
                board[0][1] = setMarker(0,1,circ)
                circ = switch(circ)

            if posx>400 and posx<600 and posy>100 and posy<300 and board[0][2]==0:
                board[0][2] = setMarker(0,2,circ)
                circ = switch(circ)

            if posx>0 and posx<200 and posy>300 and posy<500 and board[1][0]==0:
                board[1][0] = setMarker(1,0,circ)
                circ = switch(circ)

            if posx>200 and posx<400 and posy>300 and posy<500 and board[1][1]==0:
                board[1][1] = setMarker(1,1,circ)
                circ = switch(circ)

            if posx>400 and posx<600 and posy>300 and posy<500 and board[1][2]==0:
                board[1][2] = setMarker(1,2,circ)
                circ = switch(circ)

            if posx>0 and posx<200 and posy>500 and posy<700 and board[2][0]==0:
                board[2][0] = setMarker(2,0,circ)
                circ = switch(circ)

            if posx>200 and posx<400 and posy>500 and posy<700 and board[2][1]==0:
                board[2][1] = setMarker(2,1,circ)
                circ = switch(circ)

            if posx>400 and posx<600 and posy>500 and posy<700 and board[2][2]==0:
                board[2][2] = setMarker(2,2,circ)
                circ = switch(circ)
        checkWinner(board)
        updateBoard()
        pygame.display.update()