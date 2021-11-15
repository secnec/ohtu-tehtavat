class Kirjanpito:

    def __init__(self):
        print('ping')
        self.tapahtumat = []

    def lisaa_tapahtuma(self, tapahtuma):
        self.tapahtumat.append(tapahtuma)

kirjanpito = Kirjanpito()