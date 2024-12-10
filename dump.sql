-- Database: `flask`

CREATE DATABASE IF NOT EXISTS flask;

USE flask;

-- Table structure for table `tasks`

CREATE TABLE IF NOT EXISTS `tasks` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `description` varchar(45) DEFAULT NULL,
    `completed` int DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=utf8 ;

-- Dumping data for table `tasks`

INSERT INTO `tasks` (
    `description`,`completed`)
    values
    ('task 01','1');