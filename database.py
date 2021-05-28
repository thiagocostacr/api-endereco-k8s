import MySQLdb

conn = MySQLdb.connect(user='root', passwd='inmetrics', host='127.0.0.1', port=3306)

#conn.cursor().execute('DROP DATABASE `enderecos`;')

criar_tabela = '''SET NAMES utf8;
    CREATE DATABASE `enderecos`/*!40100 DEFAULT CHARACTER SET utf8 COLLATE utf8_bin */;
    USE `enderecos`;
    CREATE TABLE `endereco` (
        `id` int(11) NOT NULL AUTO_INCREMENT,
        `clienteId` int(11) NOT NULL,
        `logradouro` varchar(200) COLLATE utf8_bin NOT NULL,
        `bairro` varchar(50) COLLATE utf8_bin NOT NULL,
        `cidade` varchar(50) COLLATE utf8_bin NOT NULL,
        `estado` varchar(50) COLLATE utf8_bin NOT NULL,
        `pais` varchar(50) COLLATE utf8_bin NOT NULL,
        `ativado` boolean not null,
        PRIMARY KEY (`id`)
    ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;'''

conn.cursor().execute(criar_tabela)
