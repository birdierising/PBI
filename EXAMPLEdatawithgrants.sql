-- grants for PBI database user
GRANT USAGE ON *.* TO `pbi`@`localhost` IDENTIFIED BY PASSWORD '*****************************************';
GRANT DELETE, EXECUTE, INSERT, SELECT, UPDATE ON `%plants`.* TO `pbi`@`localhost`;

-- test data
INSERT INTO `plants` VALUES (1,'Aloe Vera','','Succulents','2016-06-16','Sky Nursery','Strong','Minimal','Y','','');
INSERT INTO `plants` VALUES (2,'Bonnie Spider Plant','','Foliage','2016-06-16','Sky Nursery','Indirect','When dry','Y','','Cloned');
INSERT INTO `plants` VALUES (3,'Pink Stripe','','Tradescantia','2018-07-02','Sky Nursery','Strong','When dry','Y','','');
INSERT INTO `plants` VALUES (4,'Rubber','','Foliage','2018-07-26','Amazon','Strong','When dry','N','','');
INSERT INTO `plants` VALUES (5,'Sheep planter','','Succulents','2018-08-03','Home Depot','Strong','Minimal','N','','');
INSERT INTO `plants` VALUES (6,'Bill','','Nepenthes','2018-08-12','Home Depot','Strong','When dry','Y','','Cloned into Ted');
INSERT INTO `plants` VALUES (7,'Rattlesnake Calathea','','Calatheas','2018-08-15','Sky Nursery','Indirect','When dry','Y','','');
INSERT INTO `plants` VALUES (8,'Coffee','','Foliage','2018-08-15','Sky Nursery','Indirect, Bright','When dry','Y','','');
INSERT INTO `plants` VALUES (9,'Peacock Plant','','Calatheas','2018-09-01','Kate','Indirect, Bright','When dry','Y','','Cloned from Kate\'s');
INSERT INTO `plants` VALUES (10,'Draecena','','Foliage','2019-01-30','Sky Nursery','Unsure','Sometimes','N','','');
