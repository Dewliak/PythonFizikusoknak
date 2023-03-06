# Mi a python?
- Python egy sokrétű programnyelv, amit az informatika és a tudomány számos területén használnak
	-Felhasználása:
		- Asztali applikációk fejlesztése
		- Webes dolgok fejlesztése - IBM,NASA,Netflix, JP Morgan Chase, Spotify,...
		- Scriptelésre, kis programok írása
		- Tudományos célok
		- Mesterséges intelligencia

- Mik az előnyei?
	- Könnyű a szintaxisa,
	- Egyik legkönnyebb nyelv kezdőként
	- Könnyűség ellenére, rengeteg helyen felhasználható
	- Rövidebb programok (pl.: c, c++-hoz képest)
	- Dinamikus típusosságú
		- Nem kell törődni a változók típusával

- Mik a hátrányai?
	- Relatíve lassú
		- Ezért nem olyan programokat írnak vele, aminek hipergyorsan kell futnia
			-Szerencsénkre alapvetően tudományos célokra nem kellenek villámgyors dolgok, ha kell is akkor már megírták c++-ban és elég nekünk felhasználni egy python wrapperrel
	-Dinamikus típusosságú
		- Esetleges hibákat tud létrehozni az, hogy bármilyen változó bármilyen típusú lehet

#Egy rövid történelem
	-Guido van Rossum(Holland)
	-1980-as évek végén született
	-Név eredete: Monthy Python 
	- C-ben írta

	![Guido van ROssum](https://upload.wikimedia.org/wikipedia/commons/thumb/9/94/Guido_van_Rossum_OSCON_2006_cropped.png/150px-Guido_van_Rossum_OSCON_2006_cropped.png)
	

	Magfilozófiája:
		-A szép jobb, mint a csúnya.
		-Az explicit szebb, mint az implicit.
		-Az egyszerű szebb, mint a bonyolult.
		-A bonyolult jobb, mint a komplikált.
		-Az olvashatóság számít.

# Adattípusok
	- Alap adatípusok:
		1. integer(int) - egész számok (nincs felső/alsó határa)
		2. float(float) - tizedes számok 
		3. string(str) - karakter sorozatot jelölnek, szövegekre használjuk
		4. boolean(bool) - igaz/hamis

	```
		int: 1, 3, 5, 9, -3, 0
		float: 1.0, 0.9, -0.7, 5.6, 8.0
		str: "hello", "0.2", '-98', 'True'
		bool: True, False
	```
