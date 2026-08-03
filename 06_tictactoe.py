import os

def display(board):
    os.system("cls")
    print("This is Tic Tac Toe")
    for i in range(9):
        if i%3 == 0:
            print('\n','-'*17) 
        print(f" | {board[i]} |",end='')
    print('\n','-'*17,'\n')
    print("Choice: index(1-9)")


board = [' ',' ',' ',' ',' ',' ',' ',' ',' ']
display(board)
n=0

while n != 9:
    if n%2 == 0:
        try:
            x = int(input("X's turn: ")) - 1
            if x not in range(9):
                print("Enter number between 1 and 9")
                continue
            if board[x] == ' ':
                board[x] = 'X'
                n+=1
            else:
                print("Cell already occupied")
        except (ValueError,IndexError):
            print("enter valid index..")
            continue
        display(board)
    else:
        try:
            o = int(input("O's turn: ")) - 1
            if x not in range(9):
                print("Enter number between 1 and 9")
                continue
            if board[o] == ' ':
                board[o] = 'O'
                n+=1
            else:
                print("Cell already occupied")
        except (ValueError,IndexError):
            print("enter valid index..")
            continue
        display(board)
    
    for i in range(0,7,3):
        if(board[i] == board[i+1] == board[i+2] != ' '):
            print(f"{board[i]} wins the Match...\nCongratulations {board[i]}")
            n=9
            break
    for i in range(3):
        if(board[i] == board[i+3] == board[i+6] != ' '):
            print(f"{board[i]} wins the Match...\nCongratulations {board[i]}")
            n=9
            break
    if (board[0] == board[4] == board[8] != ' '):
        print(f"{board[0]} wins the Match...\nCongratulations {board[0]}")
        n=9
        break
    elif (board[2] == board[4] == board[6] != ' '):
        print(f"{board[2]} wins the Match...\nCongratulations {board[2]}")
        n=9
        break
else:
    print("Draw...\nNo one won :(")
