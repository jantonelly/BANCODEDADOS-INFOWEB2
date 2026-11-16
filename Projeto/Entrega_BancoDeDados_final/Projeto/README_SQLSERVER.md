# Sistema de agendamento — SQL Server

Aplicação Streamlit para cadastro de clientes, serviços e horários, adaptada para persistência em Microsoft SQL Server.

## Requisitos

- Python 3.10 ou superior
- Microsoft SQL Server (local, Express ou remoto)
- Microsoft ODBC Driver 18 for SQL Server

## Preparação

1. No SQL Server Management Studio, execute `../sql/01_sqlserver_criar_banco_e_tabelas.sql`.
2. Crie um ambiente virtual, instale `requirements.txt` e copie `.env.example` para `.env`.
3. Ajuste `SQLSERVER_SERVER`, credenciais e demais opções em `.env`. Com autenticação integrada do Windows, deixe usuário e senha vazios.
4. Execute `streamlit run index.py` nesta pasta.

O usuário SQL precisa ter permissão para selecionar, inserir, atualizar e excluir dados nas tabelas do banco configurado. As credenciais ficam somente no `.env`, que não deve ser compartilhado.
