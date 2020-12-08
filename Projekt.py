import random

def gensachovnica(n):  # odlucio sam se da cu ovu tablu uraditi preko 2D liste 
    line = n         # redovi
    column = n      # kolone 

    game_board = []          
    for i in range(column):
        column = []
        for i in range(line):
            column.insert(i," ")
        game_board.append(column)

    empty_place = round((n-3)/2)
    x = empty_place
    center_game_board = int(n/2)

    for i in range(len(game_board)):          # u ovom delu popunjavam tu listu
        game_board[x][i-x] = "*"
        game_board[x+2][i] = "*"
        game_board[i][x] = "*"
        game_board[i][x+2] = '*'

    for i in range(len(game_board)):
        game_board[x+1][i] = "D"
        game_board[i][x+1] = "D"
        
    game_board[0][x+1] = "*"
    game_board[n-1][x+1] = "*"
    game_board[x+1][n-1] = "*"
    game_board[x+1][0] = "*"
    game_board[center_game_board][center_game_board] = "X"

    
    return game_board        # ovde vracam tu tablu vracam 

# tu sam mislio da napravim funkciju koja ce mi generisati brojeve od 1 - 6 (kasnije sam odustao od te ideje)
def generovanie_cisla():
    number = random.randint(1,6)

    return number


# prve kolo 
def prve_kolo(n,area):            
    board = area
    current_position = 0 
    
    empty_place = round((n-3)/2)
    x = empty_place
    
    line = 0
    column = 0
    
    while True:     # toto dava panacika "A" do startnej pozicie ked spadne number6
        number = random.randint(1,6)
        print(number)
        current_position_line = 0
        current_position_column = 0
        
        if number == 6:
            board[0][x+2] = "A"
            current_position_line = 0
            current_position_column = x+2

            draw_board(board)
                    
            return board, current_position_line, current_position_column
            
        else:
            continue
    


# pohyb panacika A
def pohyb_hraca_1(area, n, position_line, position_column):            # tu mi nastaje problem jer neznam da napravim algoritam
    board = area
    players_per_team = round((n-3)/2)
    x = players_per_team
    forward_position_line = position_line
    forward_position_column = position_column
    print("line", forward_position_line,"column",forward_position_column)

    current_position_line = 0
    current_position_column = 0
    
    number = int(input())    # tu si viberam number z kocky
    print("Hodil kocku a dostal: ", number)

    if forward_position_column > n//2:                  ## TOTO DOLE JE PEKLO 
        if forward_position_column == (n//2)+1:
            if number<= players_per_team:
                if forward_position_line == players_per_team:
                    board[players_per_team][forward_position_column+abs(number- players_per_team)] = "A"
                    board[forward_position_line][forward_position_column] = "*"
                    current_position_line = players_per_team
                    current_position_column = forward_position_column+(number- players_per_team)

                    return board, current_position_line, current_position_column

                elif number<= players_per_team:
                    if forward_position_line == players_per_team:
                        board[players_per_team][forward_position_column+(number- players_per_team)] = "A"
                        board[forward_position_line][forward_position_column] = "*"
                        
                    else:
                        current_position_column = forward_position_column+(number- players_per_team)
                        board[forward_position_line+number][forward_position_column] = "A"
                        board[forward_position_line][forward_position_column] = "*"
##                        current_position_line = forward_position_line+cislo
##                        current_position_column = forward_position_column

                    return board, current_position_line, current_position_column                
                elif number> players_per_team:
                    board[players_per_team][forward_position_column+(number- players_per_team)] = "A"
                    board[forward_position_line][forward_position_column] = "*"
                    current_position_line = players_per_team
                    current_position_column = forward_position_column+(number- players_per_team)

                    return board, current_position_line, current_position_column

            elif number> players_per_team:
                    board[players_per_team][forward_position_column+(number- players_per_team)] = "A"
                    board[forward_position_line][forward_position_column] = "*"
                    current_position_line = players_per_team
                    current_position_column = forward_position_column+(number- players_per_team)

                    return board, current_position_line, current_position_column
        
            
##    if cislo+forward_position_line <= players_per_team:
##        board[forward_position_line+cislo][forward_position_column] = "A"
##        board[forward_position_line][forward_position_column] = "*"
##        current_position_line = forward_position_line+cislo
##        aktualna_pozicia_stlpcu = forward_position_column
##
##    elif cislo+forward_position_line >= players_per_team:
##        board[players_per_team][forward_position_line+2+cislo] = "A"
##        board[forward_position_line][forward_position_column] = "*"
##        current_position_line = players_per_team
##        aktualna_pozicia_stlpcu = forward_position_line+2+cislo
        
    
##    return board, current_position_line, aktualna_pozicia_stlpcu

    











# Vykresluje sachovnicu   
def draw_board(board):  # Ova funkcija ispise (nacrta) tu tablu       
    for i in board:
        print(" ".join(i))
    print()

# Preveruje vstup od pouzivatela    
def prever_n():         # Ovde sam odlucio da napisem funkciju koja ce proveriti input od korisnik 
    while True:         # Najbolje  je da kornik unese broj veci od 5 a da je neparan 
        try:            # Ovde sve to proveravam 
            n = int(input("Zadajte neparne cislo vacsie ako 5:\n" ))
            if n <= 5 or n%2 != 1:
                if n%2 != 1:
                    if n < 5:
                        print(n,"- je parne cislo a mensie ako 5." + " Skuste znovu.")
                        print("-"*30,"\n")
                    else:
                        print(n,"- je parne cislo." + " Skuste znovu.")
                        print("-"*30,"\n")
                else:
                    print(n,"zadajte vacsie cislo. Skuste znovu.\n")
                    print("-"*30,"\n")

                continue

        except ValueError:
            print("Zdajte cislo. Nie \"retazec\".")
            print("-"*30,"\n")

            continue

        return n


def main_2(area,n,position_line,position_column):       # Tu se idigrava sve za  2deo projekta (isao sa na ideju da pamti krosle kordinate figure A)
    new_area, new_position_line, new_position_column = pohyb_hraca_1(area,n,position_line, position_column)
    draw_board(new_area)
    board = new_area
    position_line = new_position_line
    position_column = new_position_column
    print("Print z main2 :"+"rad",position_line,"stlpec",position_column)

    main_2(area,n, position_line, position_column)



# Ovde program krece 
n = prever_n()
area = gensachovnica(n)
draw_board(area)
board, position_line, position_column =  prve_kolo(n,area)
main_2(area,n,position_line, position_column)
