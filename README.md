Estive estudando e testando conexões entre Python e Banco de dados (nesse caso SQL Server pois já tenho familiaridade).

Nesse projeto meu objetivo foi criar uma conexão e selecionar os dados "cru" do banco de dados, tratar com pandas e exportar para um arquivo csv.

Pedi para o ChatGPT criar vários nomes, cpf e número de contas fictícios para poder usar, mas com algumas condições:
* Deveria conter erro de carácteres nos nomes para ser tratado depois.
* Deveria ter linhas repetidas para excluir depois.
* Deveria ter dados iguais em agências diferentes, esses vão ser mantidos (para testar se vai excluir esses também).

### Código 

* primeiramente importamos a biblioteca pandas e pyodbc.
* criamos uma conexão com o banco de dados SQL Server (no código deixei ocultado por motivos de segurança, já que usei meu servidor local).
* passamos a consulta ao banco de dados (nesse caso uma query simples, somente selecionando tudo da tabela).
* passamos para um DataFrame.
* fechamos a conexão.
* renomeamos as colunas para visualizar melhor.
* damos um "drop.duplicate()" pra remover todas as linhas duplicadas.
* usamos "replace" para trocar de "S" e "N" para "Sim" e "Não".
* deixamos o nome todo em Maiúsculo usando "upper()".
* usamos "stripper()" para remover espaços em branco no início e final do nome.
* print para ver os dados.
* salvamos tudo em um novo arquivo em formato csv.


### Tecnologias Usadas:
* Python com bibliotaca Pandas (para tratamento) e PYODBC (para conexão com banco de dados).
* Microsoft SQL Server para criar banco de dados, inserir dados e consultar.

