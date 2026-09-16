class Disciplina:
    def __init__(self, cod, nome, cred, vagas, pre=None):
        self.cod = cod
        self.nome = nome
        self.cred = cred
        self.vagas = vagas
        self.ocup = 0
        self.pre = pre or []

class Aluno:
    def __init__(self, mat, nome, hist=None):
        self.mat = mat
        self.nome = nome
        self.hist = hist or []
        self.atual = []
        self.notas = {}

disciplinas = {
    "ALG101": Disciplina("ALG101", "Algoritmos", 4, 30),
    "POO201": Disciplina("POO201", "Programação OO", 4, 2, ["ALG101"]),
    "BD301": Disciplina("BD301", "Banco de Dados", 4, 30, ["POO201"]),
    "WEB401": Disciplina("WEB401", "Web", 4, 30, ["POO201"])
}
alunos = {}

while True:
    print("\n--- MATRÍCULA - MENU ---")
    print("1. Cadastrar aluno")
    print("2. Ver disciplinas")
    print("3. Realizar matrícula")
    print("4. Lançar nota (Professor)")
    print("5. Ver relatório aluno")
    print("0. Sair")
    op = input("Escolha: ")

    if op == "1":
        mat = input("Matrícula: ")
        nome = input("Nome: ")
        hist_str = input("Histórico já aprovadas (ex: ALG101,POO201 ou vazio): ")
        hist = [h.strip() for h in hist_str.split(",") if h.strip()]
        alunos[mat] = Aluno(mat, nome, hist)
        print(f"Aluno {nome} cadastrado com histórico {hist}")

    elif op == "2":
        for d in disciplinas.values():
            print(f" {d.cod} - {d.nome} - {d.cred}cr - Vagas {d.ocup}/{d.vagas} - Pré: {d.pre}")

    elif op == "3":
        mat = input("Matrícula aluno: ")
        if mat not in alunos:
            print("Aluno não encontrado")
            continue
        aluno = alunos[mat]
        print(f"Aluno: {aluno.nome} | Histórico: {aluno.hist}")
        cods_str = input("Códigos para matricular (ex: POO201,BD301): ")
        cods = [c.strip() for c in cods_str.split(",") if c.strip()]

        total_cred = sum(disciplinas[c].cred for c in cods if c in disciplinas)
        if total_cred > 28:
            print(f"REGRA VIOLADA: Limite 28 créditos por semestre! Solicitado {total_cred}")
            continue

        for cod in cods:
            if cod not in disciplinas:
                print(f"{cod} não existe")
                continue
            d = disciplinas[cod]
            # 3A
            if any(p not in aluno.hist for p in d.pre):
                print(f"3A: {d.nome} -> Pré-requisito {d.pre} NÃO atendido -> NEGADA")
                continue
            # 4A
            if d.ocup >= d.vagas:
                print(f"4A: {d.nome} -> Turma LOTADA ({d.vagas}) -> NEGADA")
                continue
            d.ocup += 1
            aluno.atual.append(d)
            print(f"[5] CONFIRMADA: {d.nome} ({d.cod})")

    elif op == "4":
        mat = input("Matrícula aluno: ")
        cod = input("Código disciplina: ")
        nota = float(input("Nota (0 a 10): "))
        if mat in alunos and cod in disciplinas:
            alunos[mat].notas[cod] = nota
            if nota >= 7 and cod not in alunos[mat].hist:
                alunos[mat].hist.append(cod)
            status = "APROVADO" if nota >= 7 else "REPROVADO"
            print(f"Nota lançada: {nota} - {status}")

    elif op == "5":
        mat = input("Matrícula: ")
        if mat in alunos:
            a = alunos[mat]
            print(f"\n--- Relatório {a.nome} ---")
            print(f"Histórico: {a.hist}")
            for d in a.atual:
                n = a.notas.get(d.cod, "Sem nota")
                print(f" {d.cod} {d.nome} - Nota: {n}")

    elif op == "0":
        break
    