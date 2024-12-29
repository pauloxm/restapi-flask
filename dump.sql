-- Database: `flask`

CREATE DATABASE IF NOT EXISTS flask;

USE flask;

-- Table structure for table `users`

CREATE TABLE IF NOT EXISTS `users` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `login` varchar(30) UNIQUE DEFAULT NOT NULL,
    `password` varchar(30) DEFAULT NOT NULL,
    `name` varchar(100) DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ;

-- Dumping data for table `users`

INSERT INTO `users` (
    `login`,`password`,`name`)
    values
    ('john','$2a$10$6hEqi3ZvVJRbVVaaxOC30eH2vaNTTCK/nD569KAILMqUBRT7KTW32','John Doe');
-- Password bcrypt 10x - john.doe
-- Table structure for table `tasks`

CREATE TABLE IF NOT EXISTS `tasks` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `description` varchar(45) DEFAULT NULL,
    `completed` int DEFAULT NULL,
    `ticket_id` varchar(11) UNIQUE DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ;

-- Dumping data for table `tasks`

INSERT INTO `tasks` (
    `description`,`completed`,`ticket_id`)
    values
    ('task 01','1','20241201001');

-- Table structure for table `healthcheck`

CREATE TABLE IF NOT EXISTS `healthcheck` (
    `id` bigint NOT NULL AUTO_INCREMENT,
    `status` TINYINT(1) DEFAULT NULL,
    PRIMARY KEY (`id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ;