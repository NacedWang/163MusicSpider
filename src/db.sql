
-- 歌手表
CREATE TABLE `artists` (
  `ARTIST_ID` bigint(20) NOT NULL,
  `ARTIST_NAME` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ARTIST_ID`),
  KEY `unique_id` (`ARTIST_ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 专辑表
CREATE TABLE `albums` (
  `album_id` bigint(20) NOT NULL,
  `artist_id` bigint(20) NOT NULL,
  `title` varchar(255) DEFAULT NULL,
  `img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`album_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--  音乐表
CREATE TABLE `musics` (
  `music_id` int(20) NOT NULL,
  `music_name` varchar(255) DEFAULT NULL,
  `album_id` int(20) NOT NULL,
  PRIMARY KEY (`music_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

