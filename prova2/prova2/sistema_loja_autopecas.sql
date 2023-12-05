-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 05/12/2023 às 02:08
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `sistema_loja_autopecas`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cliente`
--

CREATE TABLE `cliente` (
  `idCliente` int(100) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cliente`
--

INSERT INTO `cliente` (`idCliente`, `nome`, `email`) VALUES
(1, 'Kaila', 'kaila@gmail.com'),
(2, 'Ryller', 'Ryller@gmail.com'),
(3, 'Vinicius', 'Vinicius@gmail.com');

-- --------------------------------------------------------

--
-- Estrutura para tabela `detalhe_venda`
--

CREATE TABLE `detalhe_venda` (
  `idVenda` int(11) NOT NULL,
  `idProduto` int(11) NOT NULL,
  `quantidade` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `detalhe_venda`
--

INSERT INTO `detalhe_venda` (`idVenda`, `idProduto`, `quantidade`) VALUES
(1, 10, 30),
(2, 11, 12),
(3, 12, 7),
(4, 13, 1);

-- --------------------------------------------------------

--
-- Estrutura para tabela `estoque`
--

CREATE TABLE `estoque` (
  `idEstoque` int(11) NOT NULL,
  `idProduto` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

-- --------------------------------------------------------

--
-- Estrutura para tabela `produto`
--

CREATE TABLE `produto` (
  `idProduto` int(100) NOT NULL,
  `nome` varchar(100) NOT NULL,
  `preco` float NOT NULL,
  `quantidadeEmEstoque` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `produto`
--

INSERT INTO `produto` (`idProduto`, `nome`, `preco`, `quantidadeEmEstoque`) VALUES
(10, 'roda', 100, 902),
(11, 'parafuso', 5, 4770),
(12, 'alicate', 20, 269),
(13, 'chave', 40, 400),
(14, 'bateria', 100, 1000);

-- --------------------------------------------------------

--
-- Estrutura para tabela `venda`
--

CREATE TABLE `venda` (
  `idVenda` int(11) NOT NULL,
  `data` date NOT NULL,
  `total` float NOT NULL,
  `idCliente` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `venda`
--

INSERT INTO `venda` (`idVenda`, `data`, `total`, `idCliente`) VALUES
(1, '2023-12-04', 0, 1),
(2, '2023-12-04', 0, 2),
(3, '2023-12-04', 0, 3),
(4, '2023-12-04', 0, 1);

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `estoque`
--
ALTER TABLE `estoque`
  ADD PRIMARY KEY (`idEstoque`);

--
-- Índices de tabela `produto`
--
ALTER TABLE `produto`
  ADD PRIMARY KEY (`idProduto`);

--
-- Índices de tabela `venda`
--
ALTER TABLE `venda`
  ADD PRIMARY KEY (`idVenda`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
