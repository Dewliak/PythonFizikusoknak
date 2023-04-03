# Listák

* probléma: hogy tároljak nagyobb mennyiségű adatot? Az összes telefonszámot, összes könyvcímet?
* egy egyszerű változóban csak 1 dolog fér el
* megoldás: adatstruktúrák - több egymással összefüggő adatot tároljunk
* egyike a **lista**

## Mire képes egy lista?

* egy listában képesek vagyunk tárolni adatokat, tudva a sorrendjüket, nem kell hogy azonos típsú legyen. FONTOS : tudjuk őket folyamatosan változtatni.

```python
myList = ["tim", 43, 7.0, True]
fruits = ["apple", "pear", "orange"]
numbers = [1, 4, 6, 77, -8]
```

#### elemekhez való hozzáféres - indexelés

* az elemekhez \[\] - el férünk hozzá, beleírjuk az elem indexét, ami a helye 0-tól számolva. pl.: a myList-ben a 7.0 2-es indexű tehát ` myList[2] = 7.0`

#### adatok hozzáadása és törlése

* Ezek a metódusok mindig a lista után ponttal vannak hozzáírva


1. append - `list.append(elem)` - a lista végére teszi az elemet
2. insert - `list.insert(index,elem)` - az adott index elé teszi az elemet
3. \[\]  - `list[index] = elem` - a lista index - 1 ik elemét átírja az elemre

```python
fruits = ["apple", "pear", "orange"]

fruits[1] = "banana"

print(fruits)  # prints ["apple", "banana", "orange"]

fruits = ["apple", "pear", "orange"]

fruits.append("banana")

print(fruits)  # prints ["apple", "pear", "orange", "banana"]

fruits.insert(0,"mango")

print(fruits)  # prints ["mango","apple", "pear", "orange", "banana"]
```


4. remove(elem) - kitörli az adott elemet a listából
5. pop(index) - kitörli az adott indexű elemet


