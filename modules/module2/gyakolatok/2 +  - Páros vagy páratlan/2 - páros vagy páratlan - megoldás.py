# írj programot ami bekér egy számot a felhasználótól
# és megmondja hogy az a szám páros vagy páratlan-e
# megj.: az inputot áttudod alakítani integerré az int()
# -> x = int(input())

x = int(input())

if x % 2 == 0:
    print("Páros")
else:
    print("Páratlan")
    
