# Sistema de Saúde Pet

Sistema de gerenciamento de saúde animal desenvolvido em Django, com o objetivo de facilitar o cadastro de pets e o acompanhamento de seu histórico clínico, reunindo informações sobre consultas, vacinas, exames, cirurgias e medicamentos.

> Projeto desenvolvido para as disciplinas PCC e PSW.

# Tecnologias

- Django
- Python
- HTML
- CSS
- JavaScript
- MySQL
- Bootstrap
  
## Como executar o projeto

### Pré-requisitos

* Python (versão 3.10 ou superior) instalado
* XAMPP instalado (com os serviços Apache e MySQL iniciados)

### 1. Clone o repositório:

git clone https://github.com/Helen-Teixeira-de-Souza/sistema-saude-pet.git

### 2. Crie e ative um ambiente virtual:

python -m venv venv
venv\Scripts\activate

### 3. Instale as dependências:

pip install -r requirements.txt

### 4. Configure o banco de dados:

Abra o painel de controle do XAMPP e clique em Start no MySQL.

Acesse o phpMyAdmin (http://localhost/phpmyadmin/) e crie um banco de dados vazio com o nome: pcc_saude_pet.

### 5. Execute as migrações do banco de dados:

python manage.py migrate

### 6. Inicie o servidor:

python manage.py runserver

### 7. Acesse o sistema no navegador:

http://127.0.0.1:8000/

## Funcionalidades do sistema

- Autenticação
- Gestão de Tutores
- Gestão de Profissionais
- Gestão de Pets
- Histórico de Saúde
- Registros Médicos:
  - Registro de consultas.
  - Controle de vacinas e datas de aplicação.
  - Registro de exames.
  - Registro de medicamentos.
  - Registro de cirurgias.

## Autoras

- Helen Souza
- Sara Rodrigues
- Tainá Ribeiro
