CREATE DATABASE IF NOT EXISTS indoorplants;

USE indoorplants;

CREATE TABLE `plants` (
  `plantid` mediumint(25) NOT NULL AUTO_INCREMENT,
  `common_name` varchar(100) DEFAULT NULL,
  `latin_name` varchar(100) DEFAULT NULL,
  `plant_group` varchar(100) DEFAULT NULL,
  `date_acquired` date DEFAULT NULL,
  `vendor` varchar(100) DEFAULT NULL,
  `sunlight` varchar(50) DEFAULT NULL,
  `water` varchar(50) DEFAULT NULL,
  `flowering` char(1) DEFAULT NULL,
  `location` varchar(255) DEFAULT NULL,
  `notes` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`plantid`),
  KEY `common_name` (`common_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

