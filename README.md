# mini_mercado_python
Este projeto simula um sistema de Ponto de Venda (PDV) para um mercado de pequeno porte. Ele permite realizar o fluxo completo de uma venda: desde a listagem de produtos até a emissão do cupom fiscal e cálculo de troco.

# 🛒 Sistema de Mercado Simples (CLI)

Um simulador de Ponto de Venda (PDV) desenvolvido em Python para o terminal. O sistema permite a seleção de produtos por código ou nome, trata entradas com acentuação e gera um cupom fiscal detalhado.

## ✨ Funcionalidades
- **Busca Híbrida:** Encontre produtos digitando o ID numérico ou o nome.
- **Tratamento de Texto:** Sistema inteligente que ignora acentos e diferenciação entre maiúsculas/minúsculas.
- **Carrinho Dinâmico:** Exibição de subtotal a cada item adicionado.
- **Cupom Fiscal:** Impressão formatada dos itens, total e cálculo de troco.

## Lógica de Normalização de Dados
Um dos desafios deste projeto foi garantir que o sistema fosse resiliente a variações de entrada do usuário. Para isso, implementei uma função de Normalização de Strings:

Remoção de Acentos: Utilizei um mapeamento (dicionário) de caracteres acentuados para suas versões base. Isso permite que entradas como "maçã", "maca" ou "MAÇÃ" sejam processadas corretamente.

Case Insensitivity: Apliquei o método .lower() em conjunto com a limpeza de espaços em branco (.strip()), garantindo que a comparação entre a entrada do usuário e o banco de dados de produtos seja padronizada.

Busca Híbrida: O sistema identifica automaticamente se a entrada é um dígito (ID) ou texto (Nome), direcionando para a lógica de busca mais eficiente em cada caso.

## 🛠️ Tecnologias
- **Python 3.13**
- Conceitos aplicados: Dicionários, Listas, Manipulação de Strings, Tratamento de Exceções (`try/except`) e Loops.
