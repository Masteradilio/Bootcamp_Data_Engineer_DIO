#Descrição da Solução:

* Função menu(): Apresenta as opções disponíveis ao usuário e captura a escolha.
  
* Função depositar(): Solicita o valor do depósito, verifica se é positivo, atualiza o saldo e registra o depósito no extrato.
  
* Função sacar(): Solicita o valor do saque e realiza várias verificações:
    Se o valor excede o saldo disponível.
    Se o valor excede o limite de saque por operação (R$500,00).
    Se o número máximo de saques diários (3) foi atingido.
    Se o valor é positivo.
    Atualiza o saldo, registra o saque no extrato e incrementa o contador de saques, se tudo estiver correto.
  
* Função exibir_extrato(): Mostra todos os depósitos e saques realizados, além do saldo atual. Se não houver movimentações, informa ao usuário.
  
* Função main(): Controla o fluxo do programa, inicializando as variáveis necessárias e executando as operações conforme a escolha do usuário.


Observações Importantes:
* O programa opera com um único usuário, conforme especificado.
* Os valores monetários são exibidos no formato R$ xxx.xx.
* O limite de três saques diários e o limite de R$500,00 por saque são respeitados.
* Todas as movimentações (depósitos e saques) são registradas para exibição no extrato.
* Caso o extrato não possua movimentações, é exibida a mensagem "Não foram realizadas movimentações."

  
Como utilizar:
Execute o programa.

No menu, digite a letra correspondente à operação desejada:
  * [d] para Depositar
  * [s] para Sacar
  * [e] para Extrato
  * [q] para Sair

Siga as instruções exibidas para cada operação.

O programa continuará executando até que a opção [q] (Sair) seja escolhida.
