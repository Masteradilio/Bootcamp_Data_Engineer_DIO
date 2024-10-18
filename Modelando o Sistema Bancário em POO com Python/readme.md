Sistema Bancário em Python
Este projeto é um sistema bancário simples desenvolvido em Python, que permite ao usuário realizar operações básicas como depósito, saque e exibição de extrato. Além disso, o sistema possibilita a criação de novos usuários e contas bancárias, listagem de contas existentes e controle de limite de saques diários.
Funcionalidades
Depósito: Permite o depósito de valores positivos na conta bancária do usuário.
Saque: Permite realizar saques com limite diário de saques e limite máximo por saque.
Extrato: Exibe todas as transações realizadas (depósitos e saques) e o saldo atual da conta.
Novo Usuário: Possibilita a criação de novos usuários com informações pessoais.
Nova Conta: Permite a criação de contas bancárias associadas a usuários existentes.
Listar Contas: Exibe todas as contas bancárias cadastradas no sistema.
Como o código funciona
O código está organizado em funções que desempenham tarefas específicas, tornando o programa modular e facilitando a manutenção:
Funções Principais
menu(): Exibe o menu de opções e captura a escolha do usuário.
depositar(saldo, valor, extrato, /): Realiza o depósito de um valor informado pelo usuário, atualiza o saldo e registra a operação no extrato.
sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques): Realiza saques, verifica se o saldo é suficiente, se o valor não excede o limite por saque e se o número máximo de saques diários não foi atingido.
exibir_extrato(saldo, /, *, extrato): Exibe todas as transações realizadas e o saldo atual.
criar_usuario(usuarios): Cria um novo usuário solicitando informações como CPF, nome, data de nascimento e endereço.
filtrar_usuario(cpf, usuarios): Busca um usuário na lista de usuários cadastrados pelo CPF.
criar_conta(agencia, numero_conta, usuarios): Cria uma nova conta bancária associada a um usuário existente.
listar_contas(contas): Lista todas as contas bancárias cadastradas, exibindo detalhes como agência, número da conta e titular.
Fluxo do Programa
A função main() controla o fluxo principal do programa:
Inicializa variáveis importantes, como limite de saques, agência, saldo inicial, limite de saque, extrato, número de saques, lista de usuários e contas.
Exibe o menu e captura a opção escolhida pelo usuário.
Com base na opção escolhida, chama a função correspondente.
O loop continua até que o usuário escolha a opção de sair.
Como executar o programa
Pré-requisitos
Ter o Python 3 instalado em seu computador. Você pode verificar se o Python está instalado executando python --version no terminal.
Um editor de código ou IDE (opcional, mas recomendado) como VSCode, PyCharm ou outro de sua preferência.
Passos para Execução
Clone o repositório ou copie o código para um arquivo na sua máquina local com o nome sistema_bancario.py.
Abra o terminal e navegue até o diretório onde o arquivo sistema_bancario.py está salvo.
Execute o programa com o seguinte comando:
bash


python sistema_bancario.py
Interaja com o programa seguindo as instruções exibidas no menu.
Utilizando o Programa
Ao executar o programa, você verá o seguinte menu:
javascript


================ MENU ================
[d] Depositar
[s] Sacar
[e] Extrato
[nc] Nova conta
[lc] Listar contas
[nu] Novo usuário
[q] Sair
=> 
Realizar um Depósito:
Escolha a opção [d].
Informe o valor que deseja depositar.
Realizar um Saque:
Escolha a opção [s].
Informe o valor que deseja sacar.
O programa irá verificar se o saque está dentro dos limites e se há saldo suficiente.
Exibir o Extrato:
Escolha a opção [e].
Será exibido o extrato com todas as transações e o saldo atual.
Criar um Novo Usuário:
Escolha a opção [nu].
Informe os dados solicitados: CPF, nome completo, data de nascimento e endereço.
Criar uma Nova Conta:
Escolha a opção [nc].
Informe o CPF do usuário ao qual a conta será associada.
Listar Contas:
Escolha a opção [lc].
Serão exibidas todas as contas cadastradas no sistema.
Sair do Programa:
Escolha a opção [q].
Detalhes Importantes
Limite de Saques:
O usuário pode realizar até 3 saques diários.
O limite máximo por saque é de R$ 500,00.
Caso o usuário exceda o número de saques ou não tenha saldo suficiente, o programa exibirá uma mensagem de erro.
Criação de Usuários e Contas:
É necessário criar um usuário antes de criar uma conta.
O CPF é utilizado como identificador único do usuário.
Ao criar uma conta, o programa associa a conta ao usuário existente com o CPF informado.
Validações:
O programa realiza várias validações, como:
Verificar se o valor do depósito ou saque é positivo.
Verificar se há saldo suficiente para o saque.
Impedir a criação de usuários com CPF já cadastrado.
