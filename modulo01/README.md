# 🍧 Sistema de Vendas - Açaiteria (GUI Tkinter)

Este projeto consiste num **Sistema de Vendas para Açaiteria** desenvolvido em **Python**, que funciona via **Interface Gráfica de Usuário (GUI)** utilizando a biblioteca nativa **Tkinter**. O sistema permite cadastrar produtos via formulário, consultar o catálogo em tempo real e realizar vendas com cálculo de total e atualização automática do estoque.

---

## 👥 Visão Geral e Papéis do Projeto

O sistema foi estruturado considerando as necessidades de diferentes atores do negócio:

- **PO (Dono do Negócio):** Controle centralizado de vendas, catálogo visual e atualização automática de estoque em tempo real.
- **QA (Visão do Cliente):** Rapidez e facilidade na realização de pedidos através de campos intuitivos e alertas informativos (`messagebox`).
- **Tech / Dev (Programador):** Transição de linha de comando (CLI) para interface gráfica (GUI), mantendo validações de erros (`try/except`) e manipulação de estado.
- **UX (Designer):** Interface amigável construída com paleta de cores personalizada, auto-contraste para leitura dos dados e organização em painéis (Frames).
- **IA (Analista de Dados):** Dados padronizados de vendas e produtos prontos para integração com geração de relatórios e BI.

---

## 🔄 Ciclo de Vida do Desenvolvimento

1. **Planejamento:** Transição arquitetural do modelo CLI para Interface Gráfica (GUI).
2. **Análise:** Definição de layout, paleta de cores e fluxo de interação com formulários e botões.
3. **Desenvolvimento:** Construção das janelas, campos de entrada (`Entry`), caixas de texto (`Text`) e botões interativos (`Button`) usando Tkinter.
4. **Testes:** Validação da captura de entradas, tratamento de exceções de digitação (`ValueError`) e atualização dinâmica do painel de produtos.
5. **Implantação:** Execução do aplicativo gráfico direto no sistema operacional local.
6. **Manutenção:** Evolução futura do modelo fixo de variáveis para estruturas dinamizadas com Banco de Dados ou Listas/Dicionários.

---

## 🚀 Funcionalidades do Sistema

- **1 - Cadastrar Produto:** Formulário para registrar até 3 produtos com Nome, Estoque, Preço, Data de Validade e Descrição, com limpeza automática dos campos após o salvamento.
- **2 - Produtos em Estoque:** Painel centralizado que exibe o catálogo completo, preços formatados em R$, datas de validade e saldo de estoque.
- **3 - Realizar Venda:** Área dedicada para buscar produtos cadastrados pelo nome, informar a quantidade e processar a venda com mensagem de confirmação do valor total.
- **Tratamento de Erros:** Exibição de janelas de alerta (`messagebox`) em casos de dados inválidos (como digitar letras no estoque/preço) ou falta de estoque disponível.

---

## 🛠️ Tecnologias e Conceitos Utilizados

- **Linguagem:** Python 3
- **Interface Gráfica:** `tkinter` (Tk, Frame, Label, Entry, Button, Text, messagebox)
- **Paleta de Cores:** Estruturação em Hexadecimal para tematização personalizada da aplicação.
- **Tratamento de Exceções:** Bloco `try / except ValueError` para prevenir travamentos caso a entrada de preços e estoques seja incorreta.
- **Formatação e Manipulação de Strings:** `.upper()` para exibição, `.strip()` e `.lower()` para busca insensível a maiúsculas/minúsculas e formatador de moeda `:.2f`.

---

## 💻 Como Executar o Programa

### Pré-requisitos
- **Python 3.x** instalado no sistema (o Tkinter já vem instalado por padrão com o Python na maioria dos sistemas).

### Passo a Passo

1. **Baixar o Código:**
   Salve o código Python (por exemplo, `acaiteria_gui.py`) no seu computador.

2. **Abrir o Terminal:**
   Navegue até a pasta onde o arquivo foi salvo.

3. **Executar a Aplicação:**
   Execute o seguinte comando no terminal:
   ```bash
   python acaiteria_gui.py

  <Elicitation label="Refatorar para usar Listas e Dicionários no Tkinter" query="Como posso alterar o código da interface gráfica em Tkinter para usar listas/dicionários no lugar das variáveis fixas (p1, p2, p3) e cadastrar produtos sem limite?"/>

  <Elicitation label="Adicionar Banco de Dados SQLite ao sistema" query="Como posso conectar este sistema em Tkinter a um banco de dados SQLite para salvar os produtos e vendas permanentemente?"/>

  <Elicitation label="Exportar o projeto para um executável (.exe)" query="Como posso transformar este script Python em Tkinter em um arquivo executável (.exe) para rodar em qualquer computador?"/>

</ElicitationsGroup>

```
