# gastos
Este é um aplicativo simples para gerenciar seus gastos mensais. Você pode adicionar, excluir e visualizar os gastos, além de acompanhar as prestações restantes e o valor de cada prestação.

## Funcionalidades

- Adicionar um novo gasto: você pode adicionar um novo gasto, fornecendo o nome, as prestações restantes e o valor de cada prestação.
- Excluir um gasto: você pode excluir um gasto existente da lista.
- Visualizar os gastos: você pode visualizar a lista de gastos, organizados pelo número de prestações, do menor para o maior.
- Atualizar os gastos: as prestações são automaticamente atualizadas a cada mês. Quando as prestações chegam a 0, o objetivo é removido da lista automaticamente.

## Pré-requisitos

- Python 3.x

## Como executar o aplicativo

1. Clone este repositório para o seu ambiente local.
2. Certifique-se de ter o Python instalado em seu sistema.
3. Navegue até o diretório do projeto no terminal.
4. Execute o seguinte comando para iniciar o aplicativo: gastos.py
5. Siga as instruções exibidas no menu para usar o aplicativo.

## Como funciona o armazenamento dos dados

- Os dados dos gastos são armazenados em um arquivo binário chamado `gastos.pkl`.
- Quando você adiciona, exclui ou atualiza um gasto, os dados são salvos automaticamente no arquivo.
- Na próxima execução do aplicativo, os dados salvos são carregados para que você possa retomar de onde parou.

## Licença

Este projeto está licenciado sob a [Licença MIT](https://opensource.org/licenses/MIT).  
