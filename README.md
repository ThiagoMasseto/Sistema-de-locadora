# 🎬 Sistema de Locadora em Python
## Projeto desenvolvido como exercício de **Orientação a Objetos em Python**.

Este projeto implementa um **sistema de locadora** em Python, onde é possível cadastrar clientes, registrar itens (filmes e jogos), listar registros e controlar empréstimos. <br>
A pedido do docente do senai via notion ( https://teal-arithmetic-d58.notion.site/Atividade-Sistema-de-Locadora-2697766264ab80b2bcc4ed54babd9ba3 )

---

## 📂 Estrutura do Projeto

- `classes.py` → contém todas as classes do sistema.
- `funcoes.py` → contém as funções que interagem com o usuário (menus e operações).
- `main.py` (opcional) → pode ser criado para rodar o sistema chamando as funções.

---

## 🏗️ Classes

### 🔹 `Locadora`
Responsável por armazenar e gerenciar clientes e itens.

**Atributos:**
- `__clientes` → lista de clientes
- `__itens` → lista de itens

**Métodos:**
- `getClientes()` / `setClientes()`
- `getItens()` / `setItens()`
- `cadastrarCliente(nome, cpf, idcliente)`
- `cadastrarItem(codigo, titulo)`
- `listarCliente()`
- `listarItem()`

---

### 🔹 `Item`
Classe base para qualquer item da locadora.

**Atributos:**
- `__codigo`
- `__titulo`
- `__disponivel` (booleano)

**Métodos:**
- `getCodigo()`, `setCodigo(codigo)`
- `getTitulo()`, `setTitulo(titulo)`
- `getDisponivel()`
- `alugar()` → torna o item indisponível
- `devolver()` → torna o item disponível

---

### 🔹 `Filme` (herda de `Item`)
Representa um filme.

**Atributos adicionais:**
- `__Genero`
- `__Duracao`

**Métodos:**
- `getGenero()` / `setGenero(genero)`
- `getDuracao()` / `setDuracao(duracao)`

---

### 🔹 `Jogo` (herda de `Item`)
Representa um jogo.

**Atributos adicionais:**
- `__Plataforma`
- `__Faixaetaria`

**Métodos:**
- `getPlataforma()` / `setPlataforma(plataforma)`
- `getFaixaetaria()` / `setFaixaetaria(faixaetaria)`

---

### 🔹 `Cliente`
Representa um cliente da locadora.

**Atributos:**
- `__nome`
- `__cpf`
- `__id`
- `__itensLocados` (lista de itens alugados)

**Métodos:**
- `getNome()`, `setNome(nome)`
- `getCPF()`, `setCpf(cpf)`
- `getId()`
- `getItensLocados()`, `setItensLocados(itens)`
- `locar(item)` → adiciona item à lista de locados (se disponível)
- `devolver(item)` → devolve item e o torna disponível
- `listarItens()` → retorna lista de itens locados

---

## ⚙️ Funções do Sistema (em `funcoes.py`)

### `cadastrar_clientes()`
- Solicita nome e CPF.
- Cria um cliente com ID automático.
- Adiciona à lista de clientes da locadora.

### `listar_clientes()`
- Exibe todos os clientes cadastrados.

### `registrar_itens()`
- Pergunta se o usuário deseja registrar **Filme** ou **Jogo**.
- Solicita código e título.
- Cadastra item na locadora.

### `listar_itens()`
- Exibe todos os itens cadastrados.

### `controlar_emprestimos()`
- Menu para locar ou devolver itens.
- O usuário seleciona um cliente.
- Permite:
  - **Locar item**: só é possível se o item estiver disponível.
  - **Devolver item**: remove da lista de locados do cliente e devolve ao estoque.

  ## 🚀 Fluxo de Uso

1. **Cadastrar Cliente** 
- Nome --> João Silva 
- CPF --> 123456789
- Cliente Adicionado com Sucesso!

2. **Cadastrar Item**
## O que voce deseja registrar?
- 1 - Filme
- 2 - Jogo
- 0 - Sair
## --> 1
- Código: 101
- Título: Vingadores
- Item cadastrado com sucesso!

3. **Listar Clientes**
- ID -> 1
- CLIENTE -> João Silva
- CPF -> 123456789
  
4. **Listar Itens**
- Título -> Vingadores
- Código -> 101

5. **Controle de Empréstimos**
## === Controle de Empréstimos ===
- 1 - Locar Item
- 2 - Devolver Item
- 0 - Voltar
## --> 1

## Clientes:
- 1 - João Silva <br>
**Digite o ID do cliente:** 1

**Itens disponíveis**: <br>
- Código: 101 | Título: Vingadores <br>
 Digite o código do item:  101 <br>
 Item 'Vingadores' alugado com sucesso!*
