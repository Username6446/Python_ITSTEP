import random

def out(field):
    for i in range(3):
        for j in range(3):  
            if j<2:
                print(field[i][j], end=" || ")
            else:
                print(field[i][j], end="")
        if i < 2:
            print()
            print("=== === ===")
    print("\n")

def check(field,i):
    i-=1
    if i<=8 and i>=0:
        if field[i//3][i%3] == " ":
            return False
    
    return True

def win(flag, player):
    symbol = "X" if player == "player1" else "O" 
    for i in range(3):
        if flag[i][0]==symbol and flag[i][1]==symbol and flag[i][2]==symbol:
            return True
        elif flag[0][i]==symbol and flag[1][i]==symbol and flag[2][i]==symbol:
            return True
    if (flag[0][0]==symbol and flag[1][1]==symbol and flag[2][2]==symbol) or (flag[0][2]==symbol and flag[1][1]==symbol and flag[2][0]==symbol):
            return True
    return False

def insert(field, ind, player):
    ind=ind-1
    if player == "player":
        field[ind//3][ind%3] = "X"
    if player == "bot":
        field[ind//3][ind%3] = "O"

def win_lose(field, ch): 
    ret = 0
    if field[0][0]==ch and field[0][2]==ch and not check(field,2):
        ret = 2
    elif field[1][0]==ch and field[1][2]==ch and not check(field,5):
        ret = 5
    elif field[2][0]==ch and field[2][2]==ch and not check(field,8):
        ret = 8
    elif field[0][0]==ch and field[2][0]==ch and not check(field,4):
        ret = 4
    elif field[0][1]==ch and field[2][1]==ch and not check(field,5):
        ret = 5
    elif field[0][2]==ch and field[2][2]==ch and not check(field,6):
        ret = 6
    elif field[0][2]==ch and field[2][0]==ch and not check(field,5):
        ret = 5
    elif field[0][0]==ch and field[0][1]==ch and not check(field,3):
        ret = 3
    elif field[0][1]==ch and field[0][2]==ch and not check(field,1):
        ret = 1
    elif field[1][0]==ch and field[1][1]==ch and not check(field,6):
        ret = 6
    elif field[1][1]==ch and field[1][2]==ch and not check(field,4):
        ret = 4
    elif field[2][0]==ch and field[2][1]==ch and not check(field,9):
        ret = 9
    elif field[2][1]==ch and field[2][2]==ch and not check(field,7):
        ret = 7
    elif field[0][0]==ch and field[1][0]==ch and not check(field,7):
        ret = 7
    elif field[0][1]==ch and field[1][1]==ch and not check(field,8):
        ret = 8
    elif field[0][2]==ch and field[1][2]==ch and not check(field,9):
        ret = 9
    elif field[1][0]==ch and field[2][0]==ch and not check(field,1):
        ret = 1
    elif field[1][1]==ch and field[2][1]==ch and not check(field,2):
        ret = 2
    elif field[1][2]==ch and field[2][2]==ch and not check(field,3):
        ret = 3
    elif field[0][0]==ch and field[1][1]==ch and not check(field,9):
        ret = 9
    elif field[0][2]==ch and field[1][1]==ch and not check(field,7):
        ret = 7
    elif field[2][0]==ch and field[1][1]==ch and not check(field,3):
        ret = 3
    elif field[2][2]==ch and field[1][1]==ch and not check(field,1):
        ret = 1
    else:
        ret = 0
    return ret

def lvl2_ckeck(field):
    return win_lose(field, "X") if win_lose(field, "X") else  random.randint(1,9)

def lvl3_check(field):
    return win_lose(field, "O") if win_lose(field, "O") else win_lose(field, "X")
    # if lvl3_win(field):
    #     return lvl3_win(field)
    # elif lvl2(field):
    #     return lvl3_win(field)
    # else:
    #     return random.randint(1,9)

def lvl3(field, count):
    ret = 0
    if count==1:
        if field[1][1]=="X":
            ret = random.choice([1, 3, 7, 9])
        else:
            ret = 5
    elif count==3:
        if field[1][1]=="X":
            if field[2][0]=="X":
                ret = 1
            else:
                ret = win_lose(field, "X") if win_lose(field, "X") else random.randint(1,9)
        elif field[0][0]=="X" or field[0][2]=="X" or field[2][0]=="X" or field[2][2]=="X":
            if field[0][0]=="X" and not win_lose(field, "X") and not check(field, 9):
                ret = 9
            elif field[0][2]=="X" and not win_lose(field, "X") and not check(field, 7):
                ret = 7
            elif field[2][0]=="X" and not win_lose(field, "X") and not check(field, 3):
                ret = 3
            elif field[2][2]=="X" and not win_lose(field, "X") and not check(field, 1):
                ret = 1
            else:
                ret = win_lose(field, "X") if win_lose(field, "X") else random.randint(1,4)*2
        elif field[0][1]=="X" or field[1][0]=="X" or field[1][2]=="X" or field[2][1]=="X":
            if field[0][1]=="X" and not win_lose(field, "X"):
                if field[2][0]=="X":
                    ret = 3
                elif field[2][2]=="X":
                    ret = 1
                elif field[2][1]=="X":
                    ret = 1
                elif field[1][0]=="X":
                    ret = 1
                elif field[1][2]=="X":
                    ret = 3
            elif field[1][0]=="X" and not win_lose(field, "X"):
                if field[0][2]=="X":
                    ret = 7
                elif field[2][2]=="X":
                    ret = 1
                elif field[1][2]=="X":
                    ret = 1
                elif field[0][1]=="X":
                    ret = 1
                elif field[2][1]=="X":
                    ret = 7
            elif field[1][2]=="X" and not win_lose(field, "X"):
                if field[0][0]=="X":
                    ret = 9
                elif field[2][0]=="X":
                    ret = 3
                elif field[1][0]=="X":
                    ret = 1
                elif field[0][1]=="X":
                    ret = 3
                elif field[2][1]=="X":
                    ret = 9
            elif field[2][1]=="X" and not win_lose(field, "X"):
                if field[0][0]=="X":
                    ret = 9
                elif field[0][2]=="X":
                    ret = 7
                elif field[0][1]=="X":
                    ret = 1
                elif field[1][0]=="X":
                    ret = 7
                elif field[1][2]=="X":
                    ret = 9
    else:
        ret = win_lose(field, "X") if win_lose(field, "X") else random.randint(1,9)
    return ret

def botgame():
    end = True
    while end:
        field = [[" " for i in range(3)] for j in range(3)]
        help = [[0 for i in range(3)] for j in range(3)]
        while True:
            level = int(input("Enter level of bot (1-3) :: "))
            if 1 <= level <= 3:
                break
            print("Invalid input! Please enter a number (1-3).")
        k=1
        for i in range(3):
            for j in range(3):
                help[i][j] = k 
                k+=1
        count = 0
        while True:
            out(help)
            player = 0
            while True:
                player = int(input("Enter number of field (1-9) :: "))
                if not check(field, player):
                    break
            count += 1
            insert(field, player, "player")
            if(win(field, "player1")):
                out(field)
                print("Player win")
                break
            elif(win(field, "player2")):
                out(field)
                print("Bot win")
                break
            elif count==9:
                out(field)
                print("Draw")
                break
            bot = 0
            while True:
                if level==1:
                    bot = random.randint(1,9)
                elif level==2:
                    bot = lvl2_ckeck(field) 
                elif level==3:
                    bot = lvl3(field, count) 
                if not check(field, bot):
                    break
            insert(field, bot, "bot")
            count += 1
            out(field)
            if(win(field, "player1")):
                print("Player win")
                break
            elif(win(field, "player2")):
                print("Bot win")
                break

        end = int(input("Enter 1 - continue, 0 - end :: "))

def dualgame():
    field = [[" " for i in range(3)] for j in range(3)]
    help = [[0 for i in range(3)] for j in range(3)]
    k=1
    for i in range(3):
        for j in range(3):
            help[i][j] = k 
            k+=1
    count = 0
    while True:
        out(help)
        player1 = 0
        flag = True
        while flag:
            player1 = int(input("Player1 enter number of field (1-9) :: "))
            flag = check(field, player1)
        count += 1
        insert(field, player1, "player")
        out(field)
        out(help)
        if(win(field, "player1")):
            print("Player1 win")
            break
        elif(win(field, "player2")):
            print("Player2 win")
            break
        elif(count==9):
            out(field)
            print("Draw")
            break
        player2 = 0
        flag = True
        while flag:
            player2 = int(input("Player2 enter number of field (1-9) :: "))
            flag = check(field, player2)
        count += 1
        insert(field, player2, "bot")
        out(field)

        if(win(field, "player1")):
            print("Player1 win")
            break
        elif(win(field, "player2")):
            print("Player2 win")
            break

botgame()  