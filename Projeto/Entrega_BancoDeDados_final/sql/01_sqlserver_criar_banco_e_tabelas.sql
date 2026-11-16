/* Banco: AgendaServicos | SQL Server 2016+
   Execute este arquivo no SSMS conectado a uma instância com permissão para criar banco. */
IF DB_ID(N'AgendaServicos') IS NULL
    CREATE DATABASE AgendaServicos;
GO
USE AgendaServicos;
GO

IF OBJECT_ID(N'dbo.Cliente', N'U') IS NULL
CREATE TABLE dbo.Cliente (
    id_cliente INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_Cliente PRIMARY KEY,
    nome       NVARCHAR(120) NOT NULL,
    email      NVARCHAR(254) NOT NULL,
    telefone   NVARCHAR(30)  NOT NULL,
    CONSTRAINT UQ_Cliente_email UNIQUE (email)
);
GO

IF OBJECT_ID(N'dbo.Servico', N'U') IS NULL
CREATE TABLE dbo.Servico (
    id_servico INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_Servico PRIMARY KEY,
    descricao  NVARCHAR(160) NOT NULL,
    valor      DECIMAL(10,2) NOT NULL,
    CONSTRAINT CK_Servico_valor CHECK (valor >= 0)
);
GO

IF OBJECT_ID(N'dbo.Horario', N'U') IS NULL
CREATE TABLE dbo.Horario (
    id_horario INT IDENTITY(1,1) NOT NULL CONSTRAINT PK_Horario PRIMARY KEY,
    data_hora  DATETIME2(0) NOT NULL,
    confirmado BIT NOT NULL CONSTRAINT DF_Horario_confirmado DEFAULT (0),
    id_cliente INT NOT NULL,
    id_servico INT NOT NULL,
    CONSTRAINT FK_Horario_Cliente FOREIGN KEY (id_cliente)
        REFERENCES dbo.Cliente (id_cliente),
    CONSTRAINT FK_Horario_Servico FOREIGN KEY (id_servico)
        REFERENCES dbo.Servico (id_servico)
);
GO

IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID(N'dbo.Horario') AND name = N'IX_Horario_data_hora')
    CREATE INDEX IX_Horario_data_hora ON dbo.Horario (data_hora);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID(N'dbo.Horario') AND name = N'IX_Horario_id_cliente')
    CREATE INDEX IX_Horario_id_cliente ON dbo.Horario (id_cliente);
IF NOT EXISTS (SELECT 1 FROM sys.indexes WHERE object_id = OBJECT_ID(N'dbo.Horario') AND name = N'IX_Horario_id_servico')
    CREATE INDEX IX_Horario_id_servico ON dbo.Horario (id_servico);
GO
