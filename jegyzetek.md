# Mi a python?

* Python egy sokrétű programnyelv, amit az informatika és a tudomány számos területén használnak
* -Felhasználása:
  \- Asztali applikációk fejlesztése
  \- Webes dolgok fejlesztése - IBM,NASA,Netflix, JP Morgan Chase, Spotify,...
  \- Scriptelésre, kis programok írása
  \- Tudományos célok
  \- Mesterséges intelligencia
* Mik az előnyei?
  * Könnyű a szintaxisa,
  * Egyik legkönnyebb nyelv kezdőként
  * Könnyűség ellenére, rengeteg helyen felhasználható
  * Rövidebb programok (pl.: c, c++-hoz képest)
  * Dinamikus típusosságú
    * Nem kell törődni a változók típusával
* Mik a hátrányai?
  * Relatíve lassú
    * Ezért nem olyan programokat írnak vele, aminek hipergyorsan kell futnia
      \-Szerencsénkre alapvetően tudományos célokra nem kellenek villámgyors dolgok, ha kell is akkor már megírták c++-ban és elég nekünk felhasználni egy python wrapperrel
      \-Dinamikus típusosságú
    * Esetleges hibákat tud létrehozni az, hogy bármilyen változó bármilyen típusú lehet

# Egy rövid történelem

\-Guido van Rossum(Holland)
\-1980-as évek végén született
\-Név eredete: Monthy Python
\- C-ben írta

 ![Guido van ROssum](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/150px-Guido_van_Rossum_OSCON_2006_cropped.png)

Magfilozófiája:
\-A szép jobb, mint a csúnya.
\-Az explicit szebb, mint az implicit.
\-Az egyszerű szebb, mint a bonyolult.
\-A bonyolult jobb, mint a komplikált.
\-Az olvashatóság számít.

# Adattípusok

* Alap adatípusok:

  
  1. integer(int) - egész számok (nincs felső/alsó határa)
  2. float(float) - tizedes számok
  3. string(str) - karakter sorozatot jelölnek, szövegekre használjuk
  4. boolean(bool) - igaz/hamis

 \n 

```python
int: 1, 3, 5, 9, -3, 0
float: 1.0, 0.9, -0.7, 5.6, 8.0
str: "hello", "0.2", '-98', 'True'
bool: True, False
```

* Összetett adatípusok:


1. lista(list,array) - mindenféle elem tárolása megadot sorrendben
2. szótár(dictionary) - két dolgot köt össze **kulcs** - **érték**
3. tuple - hasonló a listához, de ha egyszer létre lett hozva nem lehet változtatni

# Aritmetikai és logikai műveletek

* Aritmetikai műveletek

```python
x = 5
y = 6

d = 12 % 5     # d  2
z = x + y      # z 11
w = x - y      # w -1
q = 5 * 6      # q 30
u = 10 / x     # u 2.0
p = 10 * 2.0   # p 20.0
t = x ** 3     # t 125
c = 28 // y    # c 5
```

* Ugyanazok a logikai műveletek mint matematikában:

```python
and # és
or # vagy
not # nem, negáció
<   # kisebb
<=  # kisebb vagy egyenlő
>   # nagyobb
>=  # nagyobb vagy egyenlő
==  # pontosan egyenlő\ azonos
!=  # nem egyenlő\ nem azonos
```

# Feltételek

* Alap logikai forma (if):

```python
if 4 < 5: # Ha ez igaz lefut
    print("true") # mindig 1 tabbal beljebb vagyunk
```

* Ha nem igaz akkor tovább megy
* Else - ha nem fut le az if, akkor ez fut le

```python
number = int(input("Please type a number: "))
if number < 5:
    print("the number is less than 5")
else:
    print("the number is NOT less than 5")
```

* Több feltétel **elif** - else if

```python
number = int(input("Please type a number: "))

if number < 5:
    print("the number is less than 5")
elif number < 10:
    print("the number is greater than or 5 and less than 10")
elif number < 15:
    print("the number is greater than or 10 and less than 15")
else:
    print("the number is NOT less than 15")


if number == 10:
    print("The number is 10")
elif number == 15:
    print("The number is 15")

# Notice it is not necessary to include an else
```


