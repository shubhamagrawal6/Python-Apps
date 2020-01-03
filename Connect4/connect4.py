#Learning python via projects
#Connect 4 game using pygame


import numpy as np
import pygame
import sys
import os


pygame.init()
blue = (0,0,255)
black = (0,0,0)
red = (255,0,0)
yellow = (255,255,0)
sqsize = 100
radius = sqsize//2 - 5
myfont = pygame.font.SysFont("helvetica", 75)
play = True
turn1 = True


#Game ke functions
def drawboard(board):
    for c in range(columns):
        for r in range(rows):
            pygame.draw.rect(win, blue, (c*sqsize, (r+1)*sqsize, sqsize, sqsize))
            if board[r][c] == 0:
                pygame.draw.circle(win, black, (c*sqsize + sqsize//2, (r+1)*sqsize + sqsize//2), radius)
            elif board[r][c] == 1:
                pygame.draw.circle(win, red, (c*sqsize + sqsize//2, (r+1)*sqsize + sqsize//2), radius)
            else:
                pygame.draw.circle(win, yellow, (c*sqsize + sqsize//2, (r+1)*sqsize + sqsize//2), radius)
    
    pygame.display.update()

def droppiece(board, col, piece):
    for r in range(rows):
        if board[rows - r - 1][col] == 0:
            board[rows - r - 1][col] = piece
            os.system("aplay /home/shubham/Desktop/Pythongames/Connect4/dropsound.wav&")
            drawboard(board)
            break
            
def winning(board, piece):
    #Check horizontal win
	for c in range(columns-3):
		for r in range(rows):
			if board[r][c] == piece and board[r][c+1] == piece and board[r][c+2] == piece and board[r][c+3] == piece:
				return True

	#Check vertical win
	for c in range(columns):
		for r in range(rows-3):
			if board[r][c] == piece and board[r+1][c] == piece and board[r+2][c] == piece and board[r+3][c] == piece:
				return True

	#Check positive diagonal win
	for c in range(columns-3):
		for r in range(rows-3):
			if board[r][c] == piece and board[r+1][c+1] == piece and board[r+2][c+2] == piece and board[r+3][c+3] == piece:
				return True

	#Check negative diagonal win
	for c in range(columns-3):
		for r in range(3, rows):
			if board[r][c] == piece and board[r-1][c+1] == piece and board[r-2][c+2] == piece and board[r-3][c+3] == piece:
				return True


rows = 6
columns = 7
board = np.zeros((rows, columns)) #Creates 2-D array of all elements zero
size = (columns*sqsize, (rows+1)*sqsize) #Tuple for size
win = pygame.display.set_mode(size) #Creates window for game
pygame.display.set_caption("Connect4 by @shubhamagrawal6")


#Main Game loop
while play:

    drawboard(board)

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()
        
        if event.type == pygame.MOUSEMOTION:
            pygame.draw.rect(win, black, (0,0, columns*sqsize, sqsize))
            posx = event.pos[0] #pos[0] gives the X-coordinate
            if turn1:
                pygame.draw.circle(win, red, (posx, sqsize//2), radius)
            else:
                pygame.draw.circle(win, yellow, (posx, sqsize//2), radius)
            pygame.display.update()


        if event.type == pygame.MOUSEBUTTONDOWN:
            pygame.draw.rect(win, black, (0,0, columns*sqsize, sqsize))
            posx = event.pos[0] #pos[0] gives the X-coordinate
            col = posx//sqsize

            #Player 1 
            if turn1:
                if board[0][col] == 0:
                    droppiece(board, col, 1)
                    turn1 = not turn1
                    if winning(board, 1):
                        label = myfont.render("Player 1 wins!!", 1, red)
                        win.blit(label, (40,10))
                        play = False

            #Player 2
            else:
                if board[0][col] == 0:
                    droppiece(board, col, 2)
                    turn1 = not turn1
                    if winning(board, 2):
                        label = myfont.render("Player 2 wins!!", 1, yellow)
                        win.blit(label, (40,10))
                        play = False
        
    if not play:
        pygame.display.update()
        pygame.time.wait(3000)
                
                    
            
            
            
            
            
            
