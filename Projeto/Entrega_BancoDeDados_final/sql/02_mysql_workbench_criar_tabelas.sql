/* DDL compatível com MySQL 8.0. Execute no MySQL Workbench usando Forward Engineer
   ou Database > Reverse Engineer para gerar o EER/modelo lógico (.mwb). */
CREATE SCHEMA IF NOT EXISTS `agenda_servicos`
  DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci;
USE `agenda_servicos`;

CREATE TABLE IF NOT EXISTS `Cliente` (
  `id_cliente` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(120) NOT NULL,
  `email` VARCHAR(254) NOT NULL,
  `telefone` VARCHAR(30) NOT NULL,
  PRIMARY KEY (`id_cliente`),
  CONSTRAINT `UQ_Cliente_email` UNIQUE (`email`)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Servico` (
  `id_servico` INT NOT NULL AUTO_INCREMENT,
  `descricao` VARCHAR(160) NOT NULL,
  `valor` DECIMAL(10,2) NOT NULL,
  PRIMARY KEY (`id_servico`),
  CONSTRAINT `CK_Servico_valor` CHECK (`valor` >= 0)
) ENGINE=InnoDB;

CREATE TABLE IF NOT EXISTS `Horario` (
  `id_horario` INT NOT NULL AUTO_INCREMENT,
  `data_hora` DATETIME NOT NULL,
  `confirmado` BOOLEAN NOT NULL DEFAULT FALSE,
  `id_cliente` INT NOT NULL,
  `id_servico` INT NOT NULL,
  PRIMARY KEY (`id_horario`),
  INDEX `IX_Horario_id_cliente` (`id_cliente`),
  INDEX `IX_Horario_id_servico` (`id_servico`),
  INDEX `IX_Horario_data_hora` (`data_hora`),
  CONSTRAINT `FK_Horario_Cliente` FOREIGN KEY (`id_cliente`)
    REFERENCES `Cliente` (`id_cliente`) ON UPDATE CASCADE ON DELETE RESTRICT,
  CONSTRAINT `FK_Horario_Servico` FOREIGN KEY (`id_servico`)
    REFERENCES `Servico` (`id_servico`) ON UPDATE CASCADE ON DELETE RESTRICT
) ENGINE=InnoDB;
