CREATE TABLE `users` (
  `id` INT(11) NOT NULL AUTO_INCREMENT COMMENT 'user id',
  `name` VARCHAR(255) NOT NULL COMMENT 'user name',
  `password` VARCHAR(255) NOT NULL COMMENT 'encrypted password',
  `email` VARCHAR(255) NOT NULL UNIQUE COMMENT 'login id, email',
  `create_date` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP COMMENT 'registered day',
  `modify_date` DATETIME NOT NULL ON UPDATE CURRENT_TIMESTAMP COMMENT 'modified day',
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;