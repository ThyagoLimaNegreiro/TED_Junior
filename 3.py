cardapio = {
    "1": ("Pizza Calabresa G", 59.90),
    "2": ("X-Burguer", 25.00),
    "3": ("Refrigerante 2L", 12.00),
    "4": ("Batata Frita G", 30.00)
}
pedidos = []
entregadores = ["Carlos", "Ana", "João"]

while True:
    print("\n--- DELIVERY - MENU ---")
    print("Cardápio:")
    for k, v in cardapio.items():
        print(f" {k}. {v[0]} - R${v[1]}")
    print("\n1. Fazer novo pedido")
    print("2. Ver pedidos")
    print("0. Sair")
    op = input("Escolha: ")

    if op == "1":
        nome = input("Nome do cliente: ")
        endereco = input("Endereço: ")
        itens_str = input("Digite os códigos (ex: 1,2,3): ").split(",")

        itens = []
        total = 0
        for i in itens_str:
            i = i.strip()
            if i in cardapio:
                itens.append(cardapio[i][0])
                total += cardapio[i][1]

        if not itens:
            print("Nenhum item válido")
            continue

        print(f"\n[1] {nome} selecionou: {itens}")
        print(f"[2] Confirmado - Total R${total:.2f}")
        pag = input("Forma pagamento (PIX/Cartão/Dinheiro): ")
        print(f"[3] Sistema enviou pedido para Restaurante")

        aceita = input("Restaurante aceita pedido? (s/n): ")
        if aceita.lower()!= "s":
            print("Pedido RECUSADO -> Estorno realizado")
            continue

        print("[4] Restaurante ACEITOU")
        print("[5] Pedido em PREPARO...")
        print(f"Entregadores disponíveis: {entregadores}")
        entreg = input("Escolha entregador: ")

        print(f"[6] Saiu para entrega com {entreg}")
        print(f"ENTREGUE para {nome} em {endereco} - Pago com {pag}!")

        pedidos.append({"cliente": nome, "itens": itens, "total": total, "entregador": entreg})

    elif op == "2":
        for p in pedidos:
            print(p)

    elif op == "0":
        break
    