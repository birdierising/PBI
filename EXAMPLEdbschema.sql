CREATE DATABASE IF NOT EXISTS indoorplants;

USE indoorplants;

CREATE TABLE `plants` (
  `plantid` mediumint(25) NOT NULL AUTO_INCREMENT,
  `common_name` varchar(100) NOT NULL,
  `quantity` tinyint(50) DEFAULT 1,
  `latin_name` varchar(100) NOT NULL,
  `plant_group` varchar(100) NOT NULL,
  `date_acquired` bigint(11) NOT NULL,
  `vendor` varchar(100) NOT NULL,
  `sunlight` varchar(50) NOT NULL,
  `water` varchar(50) NOT NULL,
  `flowering` char(3) NOT NULL,
  `location` varchar(255) NOT NULL,
  `notes` varchar(255) NOT NULL,
  PRIMARY KEY (`plantid`),
  UNIQUE KEY `common_name` (`common_name`)
) ENGINE=InnoDB AUTO_INCREMENT=100 DEFAULT CHARSET=utf8mb;
