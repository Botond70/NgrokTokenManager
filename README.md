# NgrokTokenManager
Egy nem feltétlen hasznos ngrok authentication token manager
használat előtt, legalább két tokent bele kell rakni a tokenek.bac text fileba



syntax: python ngrokmanager.py (lbi(n|d)) [int for n|d]

l - load, betölti a tokenek.txt fileban lévő tokeneket, ha üres, akkor létrehozza, és feltölti a backupból

b - betölti a tokenek.bac fileban lévő tokeneket, HA NINCS LEGALÁBB 2 TOKEN BENNE NEM MŰKÖDIK!!!

i - lefuttatja az ngrok config add-authtoken {token} parancsot az os-el, akkor működik, ha az ngrok.exe3 parancsfile-al egy mappában van a program!

n [int] - új tokenre lép át, az int-el megadható hányszor lépjen, default = 0

d [int] - droppolja a jelenlegi tokent a listából, és nem menti el a tokenek.txt-be

az utóbbi két paraméter nem kompatibilis egymással
