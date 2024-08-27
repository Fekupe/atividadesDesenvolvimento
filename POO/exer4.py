class Aluno:
    def __init__(self, nome, curso, tempoSemDormir):
        self.nome = nome
        self.curso = curso
        self.tempoSemDormir = tempoSemDormir

    def estudar(self,qtdHoras):
        novaHora = self.tempoSemDormir+qtdHoras
        return f"Estude {qtdHoras} horas que também serão {novaHora} horas sem dormir"
    
    def dormir(self,qtdHorasSono):
        novaHoraSono = self.tempoSemDormir - qtdHorasSono
        return f"Durma por {qtdHorasSono} horas e terá ficado {novaHoraSono} horas sem dormir"
    
aluno = Aluno("André","Python",8)
print(aluno.estudar(4))
print(aluno.dormir(8))