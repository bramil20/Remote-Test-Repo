from Covek import Covek

covek = Covek()
novac_za_kladjenje = 1000
i = 0

while novac_za_kladjenje >= 0 and novac_za_kladjenje <= 2000:
    novac_za_kladjenje = + covek.igraj_par_nepar('par', 20, novac_za_kladjenje)
    i = i + 1
    print("Ovo je iteracija broj: " + str(i))
    if novac_za_kladjenje <= 0:
        print('IZGUBILI STE SAV NOVAC U : ' + str(i) + '. POKUSAJU!')
    elif novac_za_kladjenje >= 2000:
        print('POBEDILI STE!')
