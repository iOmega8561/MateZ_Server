START TRANSACTION;

CREATE TABLE webapp.user (
  `username` varchar(50) NOT NULL,
  `hashedpass` longtext NOT NULL,
  `avatar` varchar(100) NOT NULL,
  `region` varchar(5) NOT NULL,
  `fgames` longtext NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE webapp.user ADD CONSTRAINT `user_pk` PRIMARY KEY(`username`);

CREATE TABLE webapp.request (
  `uuid` varchar(100) NOT NULL,
  `user_id` varchar(100) NOT NULL,
  `game` varchar(100) NOT NULL,
  `time` int(8) NOT NULL,
  `mic` tinyint(1) NOT NULL,
  `region` varchar(3) NOT NULL,
  `pnumber` int(8) NOT NULL,
  `skills` longtext NOT NULL,
  `plat` varchar(10) NOT NULL,
  `gamemode` varchar(50) NOT NULL,
  `submitdate` datetime NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

ALTER TABLE webapp.request ADD CONSTRAINT `request_pk` PRIMARY KEY(`uuid`);
ALTER TABLE webapp.request ADD CONSTRAINT `request_user_fk` FOREIGN KEY(`user_id`) REFERENCES user(username) ON DELETE CASCADE;

COMMIT;