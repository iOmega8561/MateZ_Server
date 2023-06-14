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

INSERT INTO webapp.user (`username`, `hashedpass`, `avatar`, `region`, `fgames`) VALUES
('Aryan70', 'e0d0a8a9779f75750c64a45bb350ea59', 'user5', 'in', '[\"ARK: Survival Evolved\", \"Apex Legends\", \"COD: Warzone 2\", \"Counter Strike: GO\"]'),
('ciao', 'dac0ddf5740ba64f8f2fb1f9f24ab0c1', 'user11', 'it', '[\"League of Legends\", \"Counter Strike: GO\"]'),
('DemoUser', 'fe01ce2a7fbac8fafaed7c982a04e229', 'user2', 'it', '[\"League of Legends\", \"Minecraft\"]'),
('iOmega', '2270e50625bf9912f6df2951eb7e1ac4', 'user5', 'it', '[\"League of Legends\", \"Apex Legends\", \"Dota 2\", \"Grand Theft Auto V\", \"Minecraft\", \"ARK: Survival Evolved\"]'),
('jv999', '0df94bb298da1d3693147ae8b5a9ea8c', 'user12', 'in', '[\"Grand Theft Auto V\", \"COD: Warzone 2\", \"Counter Strike: GO\", \"Dota 2\", \"Valorant\", \"War Thunder\", \"World of Warcraft\"]'),
('NekoLau', 'f987b397be999621d41b7b0fe3ea7984', 'user0', 'it', '[\"Minecraft\", \"COD: Warzone 2\", \"Grand Theft Auto V\"]'),
('vk2908', 'a4b9d50f5c812864e885d8ac85aed1d1', 'user14', 'in', '[\"Fifa 23\"]');

INSERT INTO webapp.request (`uuid`, `user_id`, `game`, `time`, `mic`, `region`, `pnumber`, `skills`, `plat`, `gamemode`, `submitdate`) VALUES
('295585c2-3778-4d72-bb41-89f9b4fbbd02', 'iOmega', 'ARK: Survival Evolved', 5, 0, 'it', 1, '[]', 'PC', 'Official PVP', '2023-06-12 16:06:23'),
('60979293-7367-42e9-968d-40ff07891988', 'ciao', 'Minecraft', 10, 1, 'it', 1, '[]', 'PC', 'Vanilla Survival', '2023-05-30 17:39:36'),
('69e796ca-65d6-4b23-8677-a559faf83fe9', 'jv999', 'Fifa 23', 30, 1, 'in', 1, '[]', 'PC', 'Pro Club', '2023-06-12 17:58:47'),
('732d08b8-dfea-4009-b397-df02a4a3dee0', 'NekoLau', 'Minecraft', 20, 1, 'it', 5, '[]', 'PC', 'Bedwars', '2023-06-13 16:35:45'),
('8cc0d3e5-5684-441d-8821-19f728aba6d0', 'jv999', 'Counter Strike: GO', 90, 1, 'in', 1, '[\"Support\"]', 'PC', 'Competitive', '2023-06-12 17:58:14'),
('8f389478-4af0-4dd8-b1f4-0743a9da0b3b', 'ciao', 'Valorant', 15, 0, 'it', 2, '[\"Duelist\"]', 'PC', 'Spike Rush', '2023-06-03 14:53:52'),
('ba108fae-4cc6-44d7-bd87-c35d6ad9ad1a', 'iOmega', 'League of Legends', 5, 0, 'it', 1, '[]', 'PC', 'Ranked Flex', '2023-06-05 13:51:15'),
('f51465bd-e5de-4196-a354-389c3645a307', 'ciao', 'ARK: Survival Evolved', 50, 1, 'it', 1, '[]', 'XBOX', 'Non Dedicated Session', '2023-06-03 14:53:32'),
('f8e84b8c-c081-46a6-b3e1-16f56d165798', 'jv999', 'ARK: Survival Evolved', 5, 0, 'it', 1, '[]', 'PC', 'Small tribe PVP', '2023-06-13 15:57:13');

COMMIT;