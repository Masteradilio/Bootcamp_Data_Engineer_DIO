# Sistema Bancário em Python

Este projeto é uma simulação de um sistema bancário desenvolvido em Python. O sistema permite que os usuários realizem operações bancárias básicas, como depósitos, saques, visualização de extratos, criação de novos usuários e contas, e listagem de contas existentes.

## Índice

- [Descrição do Projeto](#descrição-do-projeto)
- [Funcionalidades](#funcionalidades)
- [Como Executar o Programa](#como-executar-o-programa)
- [Exemplo de Uso](#exemplo-de-uso)
- [Estrutura do Código](#estrutura-do-código)
- [Contribuindo](#contribuindo)
- [Licença](#licença)

## Descrição do Projeto

O objetivo deste sistema bancário é fornecer uma interface simples de linha de comando que permita a interação do usuário com operações bancárias comuns. O projeto foi desenvolvido utilizando funções para modularizar o código e melhorar a legibilidade e manutenção.

## Funcionalidades

1. **Depósito**: Permite o depósito de valores positivos na conta. O valor é adicionado ao saldo e registrado no extrato.

2. **Saque**: Permite a realização de saques com as seguintes restrições:
   - Limite de **R$ 500,00** por saque.
   - Limite de **3 saques diários**.
   - O usuário deve ter saldo suficiente para realizar o saque.

3. **Extrato**: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual. Se não houver movimentações, informa que não foram realizadas movimentações.

4. **Novo Usuário**: Cadastra um novo usuário com CPF único. Caso o CPF já esteja cadastrado, impede a criação do usuário.

5. **Nova Conta**: Cria uma nova conta bancária vinculada a um usuário existente.

6. **Listar Contas**: Lista todas as contas bancárias cadastradas, exibindo informações como agência, número da conta e titular.

## Como Executar o Programa

### Pré-requisitos

- Python 3.x instalado no sistema.

### Passos para Execução

1. **Clone o repositório ou copie o código** para o seu ambiente local.

2. **Abra um terminal** na pasta onde o arquivo `sistema_bancario.py` está localizado.

3. **Execute o programa** com o seguinte comando:

   ```bash
   python sistema_bancario.py
   ```

4. **Interaja com o menu** que será apresentado, digitando as opções conforme solicitado.

## Exemplo de Uso

Ao executar o programa, será exibido um menu como o seguinte:

```
=============== MENU ================
[d]	Depositar
[s]	Sacar
[e]	Extrato
[nc]	Nova conta
[lc]	Listar contas
[nu]	Novo usuário
[q]	Sair
=> 
```

- **Para realizar um depósito**, digite `d` e siga as instruções.
- **Para realizar um saque**, digite `s` e siga as instruções.
- **Para visualizar o extrato**, digite `e`.
- **Para criar um novo usuário**, digite `nu` e forneça as informações solicitadas.
- **Para criar uma nova conta**, digite `nc` (é necessário ter um usuário cadastrado).
- **Para listar todas as contas**, digite `lc`.
- **Para sair do programa**, digite `q`.

## Estrutura do Código

O código é organizado em funções para facilitar a manutenção e a leitura. Abaixo, uma breve descrição de cada função:

- **`menu()`**: Exibe o menu de operações e captura a opção selecionada pelo usuário.

- **`depositar(saldo, valor, extrato, /)`**: Realiza a operação de depósito. Atualiza o saldo e o extrato se o valor for positivo.

- **`sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques)`**: Realiza a operação de saque. Verifica se o valor do saque não excede o saldo, o limite de saque e o número máximo de saques diários.

- **`exibir_extrato(saldo, /, *, extrato)`**: Exibe o extrato das transações realizadas e o saldo atual.

- **`criar_usuario(usuarios)`**: Cria um novo usuário após verificar se o CPF já está cadastrado.

- **`filtrar_usuario(cpf, usuarios)`**: Filtra e retorna um usuário com base no CPF informado.

- **`criar_conta(agencia, numero_conta, usuarios)`**: Cria uma nova conta bancária para um usuário existente.

- **`listar_contas(contas)`**: Lista todas as contas bancárias cadastradas.

- **`main()`**: Função principal que coordena a execução do programa e chama as demais funções conforme as operações selecionadas pelo usuário.



## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma _issue_ ou enviar um _pull request_.

## Licença

Este projeto está licenciado sob a licença MIT - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

Esperamos que este guia seja útil para entender como o código funciona e como executar o programa. Divirta-se explorando e aprimorando o sistema bancário!
