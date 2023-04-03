"""
Egyenletrendszer megoldó program - Gauss és Jordan módszerrel

Lépesek:
    1. adatok beolvasása
    2. gauss háromszög kialakítása
    3. Jordan formára hozás

"""


def GCD(a,b):
    if b == 0:
        return a

    return GCD(b, a % b)

def LCM(a,b):
    return (a*b)/GCD(a,b)

def sor_szorzasa(matrix,index,szorzo):

    """
    sor =  matrix[index]
    for i in range(len(sor)):
        sor[i] = sor[i]*szorzo

    return sor
    """

    return list(map(lambda elem: elem*szorzo, matrix[index]))


def sor_skalar_szorzas(matrix,index,skalar):
    for i in range(len(matrix[index])):
        matrix[index][i] *= skalar

def sor_hozzaadasa(matrix,index,sor):
    for i in range(len(matrix[index])):
        matrix[index][i] += sor[i]

def matrix_kiiratasa(matrix):
    print("matrix: ")

    for line in matrix:
        l = ""
        for elem in line:
            l += str(round(float(elem),2)) + " "
        print(l)




if __name__ == "__main__":
    matrice_size = int(input("Add meg a nagysagat:"))

    matrice = []    

    for i in range(matrice_size):
        line = list(map(int,input().split()))
        matrice.append(line)

    print("ALAP")
    matrix_kiiratasa(matrice)
    
    # haromszog

    for i in range(matrice_size):

        alap_elem = matrice[i][i]

        for j in range(i+1,matrice_size):
            #megkeresi a legkisebb kozos tobbszorost
            LKO = LCM(alap_elem,matrice[j][i])

            szorzott_sor = sor_szorzasa(matrice,i,-(LKO/alap_elem))
            print(szorzott_sor)
            sor_skalar_szorzas(matrice,j,LKO/matrice[j][i])        
            sor_hozzaadasa(matrice,j,szorzott_sor)
            matrix_kiiratasa(matrice)  

    #jordan

    for i in range(matrice_size-1,-1,-1):

        # 1-esre hozas
        sor_skalar_szorzas(matrice,i,1/matrice[i][i])
        matrix_kiiratasa(matrice)
        
        for j in range(i):
            matrice[j][matrice_size] -= matrice[j][i]*(matrice[i][matrice_size])
            matrice[j][i] = 0
        
        matrix_kiiratasa(matrice)
        

"""
test:
3
3 2 -4 3
2 3 3 15
5 -3 1 14

"""
