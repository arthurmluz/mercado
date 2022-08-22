# Backend Controle de Estoque de um Mercado

#### Framework: Flask
#### Banco de dados: Postgreesql (uso de SQL Alchemy)
- #### Instância do banco de dados está rodando em Google Cloud (encerrarei ela dia 01/09/2022);
- #### Informações para conexão do banco devem ser alterados no 'secrets' (estão no email enviado);

#### O arquivo principal para executar a API é manage.py;
#### Todos os requerimentos para a execução podem ser encontrados em requirements.txt
#### Exemplo para execução: `python3 manage.py flask`


# Diagrama da aplicação:

![imagem diagrama da aplicação](util/mercado_diagram.png)

# Imagem da API swagger
![imagem diagrama da aplicação](util/api_mercado_swagger.png)
#### Recomendado testar a API pelo próprio swagger.

## Features:

- Feature 1,2 e 3: Inclusão/Alteração/Remoção de novos itens no estoque
  - foram criados alguns itens estoque e eles podem ter quantidades adicionadas e removidas pelo PUT /estoque;
  - recebe id e quantidade como parâmetros no body para que seja feito a alteração;
  - falta: inclusão/remoção de itens para itens estoque
- Feature 4: Consulta de itens
  - foi criado um endpoint GET que retorna todos os itens em estoque `/estoque`; 
- Feature 5, 7: Consulta de itens por setor / consulta de prateleiras por setor
  - foi criado um endpoint GET `/estoque/setor/<setor_name>` que recebe uma string de nome de setor,
exemplo 'padaria' e retorna a lista de prateleiras naquele setor, e dentro de cada prateleira os seus itens;
- Feature 6: Consulta de itens por prateleira
- foi criado um endpoint GET `/estoque/prateleira/<prateleira_id>` que recebe um id de prateleira (existem de 1-7)
e retorna as informações da prateleira e todos os itens nela presentes;

  
#### Observações:
- Não foi possível implementar frontend;
- Features 8-11 (opcionais) não foram realizadas;
- Script de criação e inserção de itens do banco de dados utilizado está na pasta utils;
- Nunca havia criado uma API desde o começo em flask, apenas feito adições a APIs já existentes, 
nas quais namespace e blueprints já estavam configuradas;
- Gostaria de ter tido mais tempo para dedicar ao desenvolvimento;
