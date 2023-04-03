# Ciklusok

for i in range(x):

* a ciklus ismétlődés. Egy ciklus addig ismétlődik, míg egy adott feltéltel nem teljesül
* két fő fajtája van
  1, *for* loop - akkor használjuk általában, ha tudjuk hányszor akarunk valamit megismételni. Általában számhoz van kötve.
  2, *while* loop - leggyakrabban akkor használjuk, mikor nem tudjuk pontosan hányszor akarunk valamit megismételni. Általában logikai feltételhez van kötve.

## For ciklus

* szintaxisa:

```python
 for valtozo in range(x):
   #csinálj valamit
```

vagy

```python
 for valtozo in iterable:
   #csinálj valamit
```

* a *valtozo* bármi lehet, lényegében egy új változót hozunk létre, ezért nem ajánlatos már meglévőt használni

  #### range funkció
  * azt teszi lehetővé, hogy elszámoljunk egy adott számig for loop segítségével.
  * Két formája van:
    * Rövid forma: `range(x)`
      * Elszámol 0-tól x-ig (de azt nem beszámítva) 1-esével növekedve
      * pl. range(10) = 0,1,2,3,4,5,6,7,8,9
    * Hosszú forma: `range(start,end,step)`
      * start-tól end-ig(azt megint csak nem beszámítva) step intervallumokkal
      * pl.: range(3,11,2) = 3,5,7,9
* példa a for loopra:

```python
for x in range(4):
    # 0-tól kezdünk egészen 4-ig
    print(x) # kiírjuk az x-et

# A kimenet
0
1
2
3
# Figyeld meg hogy a 4-et már nem írjuk ki.


for i in range(0,6,2):
    # 0-tól 6-ig megyünk 2-esével
    print(i)

# A kimenet
0
2
4
```

## while ciklus

* addig ismétlődik, amíg a feltétel nem teljesül
* szintaxis:

  ```python
  while feltetel:
    #csinal valamit
  ```
  * a felététel lehet bármi pl.:  True(ekkor mindig igaz), a == 2,...

## break

* megesik, hogy valamilyen ok miatt hamarabb kiakarunk lépni a ciklusból, erre a **break** szócskát használjuk

```python
  i = 3
  while i < 20:
    if i % 2 == 0: # paros
      break

    i += 1
```


