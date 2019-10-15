from tic_tac_menu import menu

#width = 600
#height = 600

X = 'x'
O = 'o'
N = ' '

board = [[N, N, N],
         [N, N, N],
         [N, N, N]]

colors = ['#FF0000', '#14EFF5']
turn = 0
game = False

mymenu = menu()

def setup():
    size(600, 600)
    this.getSurface().setResizable(True)
    mymenu.mainMenu(width, height)
    
def draw():
    global board
    global turn
    global colors
    global game
    global width
    global height
    
    if (game == True):
        # Game area
        background(255)
        display(board, turn, colors)
        
        state = eval(board)
        if (state[0] == False):
            background(255)
            textSize(20)
            fill(colors[1])
            if state[1] == 'X':
                fill(colors[0])
            
            mymenu.winner(state[1])
            
            mymenu.manualMenu(10);
            game = False
        
        board, turn = user_input(board, turn)
    else:
        background(255)
        mymenu.show()
        menuInput = mymenu.input()
        
        if (menuInput == 10):
            board = [[N, N, N],[N, N, N],[N, N, N]]
            mymenu.reset(width, height)
        
        # Start Game
        if (menuInput == 0):
            game = True
        
        # Main menu
        if (menuInput == 1):
            mymenu.mainMenu(width, height)
            
        # Options Menu
        if (menuInput == 2):
            mymenu.options(width, height)
            
        # window X
        if (menuInput == 2.1):
            width -= 10
            this.getSurface().setSize(width, height)
            pass
            
        if (menuInput == 2.2):
            width += 10
            this.getSurface().setSize(width, height)
            pass
        
        # window Y
        if (menuInput == 2.3):
            height -= 10
            this.getSurface().setSize(width, height)
            pass
        
        if (menuInput == 2.4):
            height += 10
            this.getSurface().setSize(width, height)
            pass
    
    
def eval(board):
    running = True
    flag = False
    winner = ''
    
    for i in range(3):
        for j in range(3):
            if (board[i][j] == ' '):
                flag = True
                
    running = flag
    
    if (running == False):
        winner = "No One"
    
    for i in range(3):
        if (board[i][0] == board[i][1] == board[i][2] == 'x' or board[i][0] == board[i][1] == board[i][2] == 'o'):
            running = False
            
            if (board[i][0] == 'x'):
                winner = 'X'
            else:
                winner = 'O'
                
        if (board[0][i] == board[1][i] == board[2][i] == 'x' or board[0][i] == board[1][i] == board[2][i] == 'o'):
            running = False
            
            if (board[0][i] == 'x'):
                winner = 'X'
            else:
                winner = 'O'
                
        if (board[0][0] == board[1][1] == board[2][2] == 'x' or board[0][0] == board[1][1] == board[2][2] == 'o'):
            running = False
            
            if (board[0][0] == 'x'):
                winner = 'X'
            else:
                winner = 'O'
                
        if (board[0][2] == board[1][1] == board[2][0] == 'x' or board[0][2] == board[1][1] == board[2][0] == 'o'):
            running = False
            
            if (board[0][2] == 'x'):
                winner = 'X'
            else:
                winner = 'O'
    
    return [running, winner]
    
def user_input(board, turn):  
    if (mousePressed == True):
        for i in range(3):
            for j in range(3):
                if (mouseX <= (j+1)*width/3 and mouseY <= (i+1)*height/3):
                    if (mouseX >= j*width/3 and mouseY >= i*height/3):
                        if (board[i][j] == N):
                            if (turn%2 == 0):
                                board[i][j] = X
                                turn += 1
                            else:
                                board[i][j] = O
                                turn += 1
    return board, turn
            
        
def display(board, turn, colors):
    textAlign(CENTER)
    
    # Color for that player
    fill(colors[turn%2])
    
    # Draw the board
    rectMode(CORNERS)
    rect((width/3)-2, 0, (width/3)+2, height)
    rect((2*width/3)-2, 0, (2*width/3)+2, height)
    rect(0, (height/3)-2, width, (height/3)+2)
    rect(0, (2*height/3)-2, width, (2*height/3)+2)
    
    # Draw the pieces
    textSize(250*height/480)
    # Down
    for i in range(3):
        # Across 
        for j in range(3):
            if (board[i][j] == 'x'):
                fill(colors[0])
            elif (board[i][j] == 'o'):
                fill(colors[1])
                
            text(board[i][j], (j+1)*width/3 - (width/6), (i+1)*height/3 - 14)
    
