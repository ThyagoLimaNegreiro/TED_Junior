from datetime import datetime

class Paciente:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome
        self.consultas = []

class Medico:
    def __init__(self, id, nome, esp):
        self.id = id
        self.nome = nome
        self.esp = esp
        self.agenda = {} # data_hora -> id paciente

medicos = {}
pacientes = {}

while True:
    print("\n--- CLÍNICA - MENU ---")
    print("1. Cadastrar médico")
    print("2. Cadastrar paciente")
    print("3. Ver horários livres")
    print("4. Agendar consulta")
    print("0. Sair")
    op = input("Escolha: ")

    if op == "1":
        id = input("ID médico: ")
        nome = input("Nome: ")
        esp = input("Especialidade: ")
        medicos[id] = Medico(id, nome, esp)
        print("Médico cadastrado!")

    elif op == "2":
        id = input("ID paciente: ")
        nome = input("Nome: ")
        pacientes[id] = Paciente(id, nome)
        print("Paciente cadastrado!")

    elif op == "3":
        id = input("ID médico: ")
        if id not in medicos:
            print("Médico não encontrado")
        else:
            print(f"Horários livres Dr. {medicos[id].nome}:")
            for h in range(8, 18):
                slot = datetime.now().replace(hour=h, minute=0, second=0, microsecond=0)
                if slot not in medicos[id].agenda:
                    print(f" - {slot.strftime('%d/%m/%Y %H:%M')}")

    elif op == "4":
        pid = input("ID paciente: ")
        mid = input("ID médico: ")
        data_str = input("Data e hora (DD/MM/AAAA HH:MM): ")
        try:
            dt = datetime.strptime(data_str, "%d/%m/%Y %H:%M")
            if mid not in medicos or pid not in pacientes:
                print("Paciente ou médico não existe")
                continue
            # REGRA: máximo 3 consultas futuras
            futuras = [c for c in pacientes[pid].consultas if c > datetime.now()]
            if len(futuras) >= 3:
                print("5A: Paciente já tem 3 consultas futuras -> Operação CANCELADA")
                continue
            # REGRA + FLUXO 3A: horário ocupado
            if dt in medicos[mid].agenda:
                print("3A: Horário indisponível -> Sistema sugere novos horários:")
                for h in range(8, 18):
                    s = dt.replace(hour=h)
                    if s not in medicos[mid].agenda:
                        print(f" Sugestão: {s.strftime('%H:%M')}")
                continue

            medicos[mid].agenda[dt] = pid
            pacientes[pid].consultas.append(dt)
            print(f"CONFIRMADO: {pacientes[pid].nome} com Dr. {medicos[mid].nome} em {dt}")

        except Exception as e:
            print(f"Erro: {e}")

    elif op == "0":
        break