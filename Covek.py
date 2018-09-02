from Sto import Sto


class Covek:
    sto = Sto()
    novac = 0

    def novac_za_kladjenje(self, novac):
        self.novac = novac
        print('Spreman novac za kladjenje = ' + str(self.novac))

    def spremanje_uloga(self, ulog):
        print("Ulazete: " + str(ulog) + "RSD")
        return ulog;

    def odigraj_na_broj(self, broj):
        if broj >= 0 or broj <= 36:
            return broj
        else:
            print("Nepostojeci broj!")
            return -1

    def igraj_par_nepar(self, par_nepar, ulog, novac_za_kladjenje):
        trenutno_stanje = novac_za_kladjenje
        if par_nepar is not 'par' and par_nepar is not 'nepar':
            print('Molimo vas unesite par ili nepar!!!')
            return 0
        else:
            print('Odlucili ste se za: ' + str(par_nepar).upper())
            print('--------------------------------------')
            print('Trenutno stanje vaseg kredita: ' + str(trenutno_stanje))
            print('--------------------------------------')
            dobijeni_broj = self.sto.zavrti()
            dobitak = 0 - ulog
            if dobijeni_broj == 0:
                print('Nazalost izgubili ste: ' + str(dobitak))
            elif dobijeni_broj % 2 == 0:
                print('Dobijeni broj je PARAN')
                print('--------------------------------------')
                if par_nepar is 'par':
                    dobitak += ulog*2
                    print('Cestitamo! Dobili ste: ' + str(dobitak))
                else:
                    dobitak = dobitak - ulog
                    print('Nazalost izgubili ste: ' + str(dobitak))
                # return dobitak
            else:
                print('Dobijeni broj je NEPARAN')
                if par_nepar is 'nepar':
                    dobitak += ulog*2
                    print('Cestitamo! Dobili ste: ' + str(dobitak))
                else:
                    print('Nazalost izgubili ste: ' + str(dobitak))
        trenutno_stanje += dobitak
        print('Trenutno stanje: ' + str(trenutno_stanje))
        return trenutno_stanje
