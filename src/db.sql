
-- 歌手表
CREATE TABLE `artists` (
  `artist_id` bigint(20) NOT NULL,
  `artist_name` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`artist_id`),
  KEY `unique_id` (`artist_id`)
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

-- 评论表
CREATE TABLE `comments` (
  `comment_id` bigint(20) NOT NULL,
  `music_id` bigint(20) DEFAULT NULL,
  `content` varchar(255) DEFAULT NULL,
  `liked_count` int(10) DEFAULT NULL,
  `time` bigint(20) DEFAULT NULL,
  `user_id` bigint(20) DEFAULT NULL,
  `nickname` varchar(255) DEFAULT NULL,
  `user_img` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`comment_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

-- 歌词表
CREATE TABLE `lyrics` (
  `music_id` bigint(20) NOT NULL,
  `lyric` text DEFAULT NULL,
  PRIMARY KEY (`music_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

