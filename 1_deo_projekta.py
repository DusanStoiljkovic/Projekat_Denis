def gensachovnica(n):
    rad = n
    stlpec = n
    
    hracia_sachovnica = []          # tu som sa rozhodol ze budem robyt cez 2D listu 
    for i in range(stlpec):
        stlpec = []
        for i in range(rad):
            stlpec.insert(i," ")
        hracia_sachovnica.append(stlpec)

    prazdne_miesto = round((n-3)/2)
    x = prazdne_miesto

    stred_hracia_sachovnica = int(n/2)

    for i in range(len(hracia_sachovnica)):
        hracia_sachovnica[x][i-x] = "*"
        hracia_sachovnica[x+2][i] = "*"
        hracia_sachovnica[i][x] = "*"
        hracia_sachovnica[i][x+2] = '*'

    for i in range(len(hracia_sachovnica)):
        hracia_sachovnica[x+1][i] = "D"
        hracia_sachovnica[i][x+1] = "D"
        
    hracia_sachovnica[0][x+1] = "*"
    hracia_sachovnica[n-1][x+1] = "*"
    hracia_sachovnica[x+1][n-1] = "*"
    hracia_sachovnica[x+1][0] = "*"
    hracia_sachovnica[stred_hracia_sachovnica][stred_hracia_sachovnica] = "X"
    
    return hracia_sachovnica

# Vykresluje sachovnicu
def vykresli_sachovnica(doska):
    for i in doska:
        print(" ".join(i))
    print()

# Preveruje vstup od pouzivatela
def prever_n():    
    while True:
        try:
            n = int(input("Zadajte nepárne číslo väčšie ako 5:\n" ))
            if n <= 5 or n%2 != 1:
                if n%2 != 1:
                    if n < 5:
                        print(n,"- je párne číslo a menšie ako 5." + " Skúste znovu.")
                        print("-"*30,"\n")
                    else:
                        print(n,"- je párne číslo." + " Skúste znovu.")
                        print("-"*30,"\n")
                else:
                    print(n,"zadajte väčšie číslo. Skúste znovu.\n")
                    print("-"*30,"\n")

                continue

        except ValueError:
            print("Zdajte číslo. Nie \"reťazec\".")
            print("-"*30,"\n")

            continue

        return n

# Cast ktora dokopy vstetky doteraz definovane funkcie
def main():
    hodnota_n = prever_n()
    doska = gensachovnica(hodnota_n)
    vykresli_sachovnica(doska)
    main()                      # tu som dal aby sa opakovalo ked vykresli sachovnicu

# Tu program zacina pracovat
print("Projek Človeče nehnevaj sa pozostava z troch časti.\nPrvá časť je generovanie šachovnice.\nDruhá časť je simulovanie hry s jednym hráčom.\nTretia časť je simulovanie ako by hra mohla v skutočnosti prebiehať.\n")
main()
