# Projeto de Coding Test da IGS

## Endpoints
- .../admin/ -> Endpoint para acessar a área administrativa do Django.

- .../employee/ -> Endpoint habilitado para listar e adicionar employees.

- .../employee/< id > -> Endpoint habilitado para listar e deletar um usuário.

## Banco de dados
Na raiz do projeto já se encontra o arquivo referente ao banco de dados SQLite3 local. 


# Executando o projeto
- Crie uma virtual env. 
      
     `python3 -m venv venv`

- Instale os dependências necessárias para executar o projeto. Rode o comando na raiz do projeto.
      
  `pip3 install -r requirements.txt`


- Execute o projeto executando o comando abaixo na raiz do projeto.

    `python3 manage.py runserver`