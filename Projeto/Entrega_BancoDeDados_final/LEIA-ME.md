# Entrega — Sistema de Agendamento de Serviços

O modelo foi derivado do sistema enviado no repositório: cadastro de clientes e serviços e criação de horários vinculados a ambos.

## Arquivos

- `diagramas/modelo_conceitual.svg` — entidades e relacionamentos (Cliente 1:N Horário; Serviço 1:N Horário).
- `diagramas/modelo_logico.svg` — tabelas, atributos, tipos, PKs, FK e restrição única.
- `sql/01_sqlserver_criar_banco_e_tabelas.sql` — banco e tabelas usados pela aplicação final.
- `sql/02_mysql_workbench_criar_tabelas.sql` — DDL compatível com MySQL 8 para abrir no MySQL Workbench e gerar o modelo EER.
- `Projeto/` — código-fonte Streamlit adaptado para persistir no Microsoft SQL Server.

## Modelo de dados

`Cliente(id_cliente, nome, email, telefone)` possui vários horários. `Servico(id_servico, descricao, valor)` pode estar associado a vários horários. `Horario(id_horario, data_hora, confirmado, id_cliente, id_servico)` registra a reserva de um serviço por um cliente. As duas referências são obrigatórias; e-mail é único, valor não pode ser negativo.

## Gerar os arquivos nativos dos programas solicitados

O Workbench e o ERDPlus salvam modelos em formatos próprios vinculados às ferramentas. Este pacote contém diagramas vetoriais legíveis e DDL para reconstrução do modelo. No MySQL Workbench, importe `02_mysql_workbench_criar_tabelas.sql` por **File > Import > Reverse Engineer MySQL Create Script**, confira as três tabelas e salve o modelo como `.mwb`. No ERDPlus, crie as entidades e cardinalidades conforme `modelo_conceitual.svg`: `Cliente 1:N Horário` e `Serviço 1:N Horário`.

## Executar a aplicação

Consulte `Projeto/README_SQLSERVER.md`. O script SQL Server pode ser executado mais de uma vez: ele cria objetos ausentes e preserva as tabelas existentes.
