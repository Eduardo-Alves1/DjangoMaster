class Cadeira:
    marca = "Desconhecida"
    cor = "Preto"
    modelo = "Concha"

    def levanta_cadeira(self):
        print("Levantando a cadeira")
    def abaixando_cadeira(self):
        print("Abaixando a cadeira")
    def essa_cadeira_e_loka(self, v1, v2):
        return v1 + v2


minha_cadeira = Cadeira()

minha_cadeira.levanta_cadeira()
minha_cadeira.abaixando_cadeira()
calculado = minha_cadeira.essa_cadeira_e_loka(10,10)
print(calculado)