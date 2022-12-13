stanje = 0
transakcije = []

while True:
    print("1. Polog Novaca")
    print("2. Isplata Novaca")
    print("3. Stanje Racuna")
    print("4. Promet po racunu")
    print("5. Izlaz")
    izbor = int(input("Upisite sto zelite raditi: "))
    if izbor == 1:
        kolicina = float(input("Unesite koliko novaca zelite poloziti: "))
        stanje += kolicina
        transakcije.append(("polog", kolicina))
        print("Polog uspjesan! Trenutno stanje je", stanje)
    elif izbor == 2:
        kolicina = float(input("Unesite koliko zelite novaca isplatiti: "))
        if kolicina > stanje:
            print("Nemate dovoljno novaca!")
        else:
            stanje -= kolicina
        transakcije.append(("isplata", kolicina))
        print("Isplata uspjesna! Trenutno stanje: ", stanje)
    elif izbor == 3 :
        print("Stanje racuna iznosi: ", stanje)
    elif izbor == 4:
        for transakcije in transakcije:
            print(transakcije)
    elif izbor == 5:
        print("hvala sto ste koristili nasu banku! Hvala i Dovidjenja!")
        break
    else:
        print("Ta opcija ne postoji, pokusajte ponovo!")
