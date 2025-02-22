class AkumaNoMi:
    def __init__(self, tipo, nome, status):
        self.tipo = tipo
        self.nome = nome
        self.status = status

    def __str__(self):
        return f"Tipo: {self.tipo}\nNome: {self.nome}\nStatus: {self.status}"

class Personagem:
    def __init__(self, nome, especie, origem, grupo, titulo, haki, akuma_no_mi):
        self.nome = nome
        self.especie = especie
        self.origem = origem
        self.grupo = grupo
        self.titulo = titulo
        self.haki = haki
        self.akuma_no_mi = akuma_no_mi

    def __str__(self):
        return (f"Nome: {self.nome}\nEspécie: {self.especie}\nOrigem: {self.origem}\nGrupo: {self.grupo}\n"
                f""f"TÍtulo: {self.titulo}\nHaki: {self.haki}\nAkuma no mi: {self.akuma_no_mi}\n")