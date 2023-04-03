# írj programot ami bekér egy évet a felhasználótól
# és megmondja hogy az adott év szökő év-e
# mikor szökőév egy év? https://www.youtube.com/watch?v=xX96xng7sAE

x = int(input())

if x % 4 == 0:
    if x % 100 == 0:
        if x % 400 == 0:
            print("Szökőév")
        else:
            print("Nem szökőév")
    else:
        print("Szökőév")
else:
    print("Nem szökőév")
    
