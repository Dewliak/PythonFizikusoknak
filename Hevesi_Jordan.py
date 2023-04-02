"""
GAUSS - JORDAN módszer egyenletrendszerek megoldásához
"""

# neccesary functions
def oszt(sor,oszto,matrice):
    """ sor-adik sor osztasa egy adott szammal(oszto) """
    
    for k in range(len(matrice)+1):
        matrice[sor][k] = matrice[sor][k]/oszto


def csere(x,y,matrice):
    """ x-edik és az y-adik sor cseréje """
    temp = matrice[x]
    matrice[x] = matrice[y]
    matrice[y] = temp


def keres(sor,oszlop,matrice):
    """ Keres egy olyans sort, ahol az adott oszlopban nem 0 van és kicseréli azokat"""
    index = -1

    for k in range(sor+1,len(matrice)):
        if matrice[k][oszlop] != 0:
            index = k
            break

    if index == -1:
        print("Nincs megoldas")
    else:
        csere(sor,index,matrice)


def osszead(x,y,seged,matrice):
    """ az x-dik sor segedszeresenek hozzaadasa az y/ik sorhoz"""
    for k in range(len(matrice)+1):
        matrice[y][k] -= matrice[x][k]*seged



def gyokok(matrice):
    """ A megfelelőre alakra hozott mátrixból a gyökök meghatározása"""
    n = len(matrice)
    for i in range(n,-1,-1):
        for j in range(i+1,n):
            matrice[i][n] = matrice[i][n] - matrice[i][j]*matrice[j][n]


# utility
def printmegoldasok(matrice):
    for i in range(len(matrice)):
        print(i+1,". gyök = ", round(matrice[i][len(matrice)],2))


def print_matrice(matrice):
    for i in matrice:
        print(list(map(lambda x: round(x,2), i)))

# main programes
def gauss(matrice):
    """ Gauss módszer """
    for i in range(len(matrice)):
        if matrice[i][i] == 0:
            keres(i,i,matrice)
        
        oszt(i,matrice[i][i],matrice)
        
        for j in range(i+1,len(matrice)):
            #print(i,"sor hozzadasa", j,".sorhoz, ennyivel szorozva: ",matrice[j][i]/matrice[i][i])
            osszead(i,j,matrice[j][i]/matrice[i][i],matrice)

    gyokok(matrice)


def jordan(matrice):
    """ Jordan módszer """ 
    for i in range(len(matrice)):
        if matrice[i][i] == 0:
            keres(i,i,matrice)
        
        oszt(i,matrice[i][i],matrice)
        
        for j in range(0,len(matrice)):
            #print(i,"sor hozzadasa", j,".sorhoz, ennyivel szorozva: ",matrice[j][i]/matrice[i][i])
            if i != j:
                osszead(i,j,matrice[j][i]/matrice[i][i],matrice)

    print_matrice(matrice)
    gyokok(matrice)


if __name__ == "__main__":
    matrice = [[2,4,0,7],[3,6,-1,8],[1,5,1,1]]
    print_matrice(matrice)
    jordan(matrice)
    printmegoldasok(matrice)
