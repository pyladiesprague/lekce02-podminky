# ---------------------------------------------
#  Řešení – podmínky (if / elif / else)
# ---------------------------------------------


# 1) Máš proměnnou vek. Vypiš "Jsi plnoletá.", když je vek 18 a víc,
#    jinak vypiš "Ještě ne.".
vek = 16
if vek >= 18:
    print("Jsi plnoletá.")
else:
    print("Ještě ne.")


# 2) Vrať se ke studentce se třemi známkami. Spočítej průměr a vypiš
#    "Máš vyznamenání!", když je průměr menší nebo rovný 2,
#    jinak vypiš "Bez vyznamenání.".
znamka1 = 1
znamka2 = 3
znamka3 = 2
prumer = (znamka1 + znamka2 + znamka3) / 3
if prumer <= 2:
    print("Máš vyznamenání!")
else:
    print("Bez vyznamenání.")


# 3) Zeptej se uživatele na číslo. Vypiš "Velké číslo!", když je větší
#    než 100, jinak "Malé číslo.".
cislo = int(input("Zadej číslo: "))
if cislo > 100:
    print("Velké číslo!")
else:
    print("Malé číslo.")


# 4) Máš proměnnou znamka (číslo 1 až 5). Pomocí if/elif/else vypiš
#    slovní hodnocení: 1 → "výborně", 2 → "chvalitebně", 3 → "dobře",
#    a cokoli dalšího → "je co zlepšovat".
znamka = 3
if znamka == 1:
    print("výborně")
elif znamka == 2:
    print("chvalitebně")
elif znamka == 3:
    print("dobře")
else:
    print("je co zlepšovat")


# 5) Zeptej se uživatele na teplotu. Vypiš:
#    pod 0 → "Mrzne.", pod 15 → "Chladno.", pod 25 → "Příjemně.",
#    jinak → "Horko.".
teplota = float(input("Jaká je teplota? "))
if teplota < 0:
    print("Mrzne.")
elif teplota < 15:
    print("Chladno.")
elif teplota < 25:
    print("Příjemně.")
else:
    print("Horko.")


# 6) Vnořená podmínka s otázkami na uživatele.
#    Zeptej se: "Prší? (ano/ne)" a ulož odpověď do proměnné prsi.
#    Když prší, zeptej se ještě "Máš deštník? (ano/ne)" a ulož do mam_destnik.
#      - když má deštník, vypiš "Beru deštník, nezmoknu."
#      - když nemá, vypiš "Zmoknu."
#    Když neprší, vypiš "Sluníčko, jde se ven!".
prsi = input("Prší? (ano/ne) ")
if prsi == "ano":
    mam_destnik = input("Máš deštník? (ano/ne) ")
    if mam_destnik == "ano":
        print("Beru deštník, nezmoknu.")
    else:
        print("Zmoknu.")
else:
    print("Sluníčko, jde se ven!")
