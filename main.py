# FUNÇÃO PARA REMOVER OS ACENTOS NOS NOMES DOS PRODUTOS (input)
def remover_acentos(texto):
    mapa = {'á':'a','à':'a','ã':'a','â':'a','é':'e','ê':'e','í':'i','ó':'o','ô':'o','õ':'o','ú':'u','ç':'c'}
    for acento, sem_acento in mapa.items():
        texto = texto.replace(acento, sem_acento)
    return texto

#EXIBIR MENU COM PRODUTOS (CÓDIGO, NOME, PREÇO)
def exibir_menu(produtos):
    print("\n" + "="*35)
    print("         TABELA DE PRODUTOS")
    print("="*35)
    for codigo, (nome, preco) in produtos.items():
        print(f"{codigo:>2} - {nome:<20} - R${preco:>6.2f}")
    print("="*35)

#LISTA DE PRODUTOS
def sistema_mercado():
    produtos = {
         # HORTIFRÚTI
        1: ("Banana", 5.50), 
        2: ("Maçã", 8.90), 
        3: ("Tomate", 7.20), 
        4: ("Cebola", 4.50),
        5: ("Batata", 5.00), 
        6: ("Alface", 3.00), 
        7: ("Cenoura", 4.80), 
        8: ("Limão", 6.00),
        9: ("Alho (pacote)", 5.00), 

        # MERCEARIA
        10: ("Ovos (dúzia)", 12.00), 
        11: ("Arroz (5kg)", 28.90),
        12: ("Feijão", 8.50), 
        13: ("Açúcar", 4.20), 
        14: ("Café", 18.00), 
        15: ("Óleo", 6.50),
        16: ("Macarrão", 4.00), 
        17: ("Farinha de Trigo", 5.50), 
        18: ("Sal", 2.50),
        19: ("Molho de Tomate", 2.20), 
        20: ("Milho de Pipoca", 5.00), 
        21: ("Farinha de Milho", 4.50),
        22: ("Vinagre", 3.80), 

        # LATICÍNIOS E PADARIA
        23: ("Leite", 5.20), 
        24: ("Manteiga", 12.00), 
        25: ("Iogurte", 3.50),
        26: ("Queijo", 7.00), 
        27: ("Presunto", 5.00), 
        28: ("Pão de Forma", 7.50),
        29: ("Pão Francês (un)", 1.00), 
        30: ("Requeijão", 8.50), 

        # CARNES E CONGELADOS
        31: ("Frango (kg)", 19.00),
        32: ("Carne Moída (kg)", 32.00), 
        33: ("Calabresa", 24.00), 
        34: ("Salsicha (kg)", 15.00),
        35: ("Hambúrguer", 2.50), 
        36: ("Lasanha", 13.50), 
        37: ("Nuggets", 14.00),
        38: ("Água", 2.00), 

        # BEBIDAS
        39: ("Refrigerante", 9.00), 
        40: ("Suco", 12.00),
        41: ("Cerveja (lata)", 4.50), 
        42: ("Vinho", 25.00), 

        # LIMPEZA E HIGIENE
        43: ("Detergente", 2.20),
        44: ("Sabão em Pó", 14.00), 
        45: ("Amaciante", 11.00), 
        46: ("Papel Higiênico", 6.00),
        47: ("Sabonete", 2.50), 
        48: ("Pasta de Dente", 4.00), 
        49: ("Shampoo", 12.00),

        # DOCES E PETISCOS
        50: ("Bolacha", 3.20), 
        51: ("Chocolate", 5.50), 
        52: ("Salgadinho", 6.00)
    }

    exibir_menu(produtos)
    carrinho = []
    total = 0.0

    # COMPRA/SELEÇÃO DE PRODUTOS
    while True:
        # Tratamento da entrada: minúsculo, sem espaços e sem acentos
        entrada_raw = input("\nCódigo ou Nome (ou '0' para sair): ").strip().lower()
        entrada = remover_acentos(entrada_raw)

        # Finalizar compra
        if entrada in ['0', 'sair']:
            break

        item_encontrado = None

        if entrada.isdigit():
            codigo_int = int(entrada)
            if codigo_int in produtos:
                item_encontrado = produtos[codigo_int]
        else:
            for cod, (nome, preco) in produtos.items():
                if entrada == remover_acentos(nome.lower()):
                    item_encontrado = (nome, preco)
                    break
        
        if item_encontrado:
            nome, preco = item_encontrado
            carrinho.append((nome, preco))
            total += preco
            print(f"[+] {nome} - R$ {preco:.2f} | Subtotal: R$ {total:.2f}")
        else:
            print("[!] Produto não encontrado.")

    # Finalização
    if total > 0:
        print("\n" + "="*30)
        print("         CUPOM FISCAL")
        print("="*30)
        for item, valor in carrinho:
            print(f"{item:<18} R$ {valor:>7.2f}")
        print("-" * 30)
        print(f"TOTAL:             R$ {total:>7.2f}")
        print("="*30)

        # Pagamento cliente e troco
        while True:
            try:
                pagamento = float(input("\nValor pago pelo cliente: R$ "))
                if pagamento >= total:
                    print(f"Troco: R$ {pagamento - total:.2f}")
                    print("Venda finalizada com sucesso!")
                    break
                else:
                    print(f"Faltam R$ {total - pagamento:.2f}")
            except ValueError:
                print("Por favor, digite um valor numérico.")
    else:
        print("\nCarrinho vazio. Operação encerrada.")

if __name__ == "__main__":
    sistema_mercado()
