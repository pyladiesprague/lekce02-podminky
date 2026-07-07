# ---------------------------------------------
#  Otočení podmínky: not
# ---------------------------------------------
# Spusť soubor a sleduj, co se vypíše.
#
# not znamená „ne". Otočí hodnotu naruby: z True udělá False
# a naopak. Hodí se, když chceš reagovat na to, že něco NEPLATÍ.


print(not True)     # False
print(not False)    # True


# not před podmínkou ji obrátí:
prsi = False
print(not prsi)    # True – „neprší"


# Typické použití – reagovat na opak:
prihlaseny = False

if not prihlaseny:
    print("Nejprve se přihlas.")


# ---
# Častá chyba: and/or spojují CELÉ podmínky, ne holá čísla.
#
# Chceš zjistit, jestli je některá ze stran a, b záporná. Správně
# musíš napsat porovnání dvakrát – zvlášť pro a a zvlášť pro b:
#
#     if a < 0 or b < 0:        # správně
#
# Když se to pokusíš zkrátit takhle, je to chyba:
#
#     if a or b < 0:           # ŠPATNĚ
#
# Python to čte jako „(a)  nebo  (b < 0)" – u prvního čísla žádné
# porovnání není. Vždycky napiš celé porovnání na OBOU stranách or / and.
