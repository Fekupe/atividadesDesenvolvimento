class Aluno:
    def __init__(self, nome, cpf):
        self.nome = nome
        self.cpf = cpf

class Equipe:
    def __init__(self, projeto, participantes):
        self.projeto = projeto
        self.participantes = participantes

class GerenciadorEquipes:
    def __init__(self):
        self.equipes = []

    def criarEquipe(self, projeto, participantes):
        for equipe in self.equipes:
            if equipe.projeto == projeto:
                for participante in participantes:
                    if participante in equipe.participantes:
                        print("A equipe não pode ser criada pois há um aluno que já participa de outra equipe com o mesmo projeto.")
                        return
        nova_equipe = Equipe(projeto, participantes)
        self.equipes.append(nova_equipe)
        print("Equipe criada com sucesso!")

gerenciador = GerenciadorEquipes()

aluno1 = Aluno("João", "123456789")
aluno2 = Aluno("Maria", "987654321")
aluno3 = Aluno("Pedro", "111222333")

gerenciador.criarEquipe("Projeto A", [aluno1, aluno2])
gerenciador.criarEquipe("Projeto B", [aluno3])

gerenciador.criarEquipe("Projeto A", [aluno1, aluno3])