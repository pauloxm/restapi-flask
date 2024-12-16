-- Database: `flask`

CREATE DATABASE IF NOT EXISTS flask;

USE flask;

-- Table structure for table `tasks`

CREATE TABLE IF NOT EXISTS `tasks` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `description` varchar(45) DEFAULT NULL,
    `completed` int DEFAULT NULL,
    `ticket_id` varchar(11) UNIQUE DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ;

-- Dumping data for table `tasks`

INSERT INTO `tasks` (
    `description`,`completed`,`ticket_id`)
    values
    ('task 01','1','20241201001');