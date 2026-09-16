from datetime import datetime, timedelta

class Livro:
    def __init__(self, isbn, titulo):
        self.isbn = isbn
        self.titulo = titulo
        self.disponivel = True
        self.fila = []

class Aluno:
    def __init__(self, mat, nome):
        self.mat = mat
        self.nome = nome
        self.livros = []
        self.multa = 0

livros = {}
alunos = {}

while True:
    print("\n--- BIBLIOTECA - MENU ---")
    print("1. Cadastrar livro")
    print("2. Cadastrar aluno")
    print("3. Realizar empréstimo")
    print("4. Devolver livro")
    print("5. Ver situação aluno")
    print("0. Sair")
    op = input("Escolha: ")

    if op == "1":
        isbn = input("ISBN: ")
        titulo = input("Título: ")
        livros[isbn] = Livro(isbn, titulo)
        print("Livro cadastrado!")

    elif op == "2":
        mat = input("Matrícula: ")
        nome = input("Nome: ")
        alunos[mat] = Aluno(mat, nome)
        print("Aluno cadastrado!")

    elif op == "3":
        mat = input("Matrícula aluno: ")
        isbn = input("ISBN livro: ")
        if mat not in alunos or isbn not in livros:
            print("Não encontrado")
            continue
        aluno = alunos[mat]
        livro = livros[isbn]

        if not livro.disponivel:
            livro.fila.append(aluno)
            print(f"2A: Livro '{livro.titulo}' INDISPONÍVEL -> {aluno.nome} entrou na fila. Posição {len(livro.fila)}")
        elif aluno.multa > 0:
            print(f"3A: Aluno com multa R${aluno.multa:.2f} -> Empréstimo BLOQUEADO")
        elif len(aluno.livros) >= 5:
            print("REGRA: Máximo de 5 livros por aluno")
        else:
            livro.disponivel = False
            aluno.livros.append(livro)
            dev = datetime.now() + timedelta(days=7)
            print(f"Empréstimo REGISTRADO! Devolução: {dev.strftime('%d/%m/%Y')}")

    elif op == "4":
        mat = input("Matrícula: ")
        isbn = input("ISBN: ")
        aluno = alunos.get(mat)
        livro = livros.get(isbn)
        if aluno and livro and livro in aluno.livros:
            atraso = input("Dias de atraso (0 se no prazo): ")
            atraso = int(atraso)
            if atraso > 0:
                aluno.multa += atraso * 2.50
                print(f"Multa gerada: R${aluno.multa:.2f}. Aluno bloqueado!")
            aluno.livros.remove(livro)
            livro.disponivel = True
            print("Devolução OK!")
            if livro.fila:
                prox = livro.fila.pop(0)
                print(f"Aviso: Livro liberado para {prox.nome} da fila!")

    elif op == "5":
        mat = input("Matrícula: ")
        if mat in alunos:
            a = alunos[mat]
            print(f"{a.nome} - Livros: {len(a.livros)} - Multa: R${a.multa}")

    elif op == "0":
        break