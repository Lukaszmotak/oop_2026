# Klasa = szablon, przepis
class Czlowiek:
    #Istota
    # atrybuty klasy
    # (Cechy wspolne kazdego czlowieka)
    gatunek = "Homo Sapiens"
    def __init__(self, imie, plec):
        #Konstruktor
        #Akt istnienia
        print(f"Niech powstanie Czlowiek o imieniu {imie}")
        self.imie = imie
        # adam.imie = "Adam"
        # ewa.imie = "Ewa"


    #Metoda
    #Moznosc (mozliwosc)
    def przedstaw_sie(self):
        print(f"Dzien dobry, mam na imie {self.imie} i jestem" , end="")
        if self.plec == "M":
            print("Mezczyzna")
        else:
            print("Kobieta")

    def przedstaw(self, czlowiek):
        print(f"Oto {czlowiek.imie}")

#Powstawanie obiektu
# "gotowanie z przepisu"
adam = Czlowiek("Adam", "M")
ewa = Czlowiek("Ewa", "K")

ewa.przedstaw_sie()
ewa.przedstaw(adam)
