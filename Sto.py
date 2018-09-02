import random

class Sto:
    svi_brojevi = list(range(37))

    #def ispisi_crne_brojeve(self):
     #   for

    def zavrti(self):
        dobijeni_broj = random.choice(self.svi_brojevi)
        print('Dobijeni broj je: ' + str(dobijeni_broj))
        return dobijeni_broj