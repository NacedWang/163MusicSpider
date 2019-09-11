"""
一般 Python 用于连接 MySQL 的工具：pymysql
"""
import pymysql.cursors

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123',
                             db='test',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


# 保存评论
def insert_comment(commentId, music_id, content, likedCount, time, userId, nickname, userImg):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `comments` (`comment_id`, `music_id`, `content`, `liked_count`, `time`, `user_id`, `nickname`, `user_img`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        cursor.execute(sql, (commentId, music_id, content, likedCount, time, userId, nickname, userImg))
    connection.commit()


# 获取所有歌词 数量
def get_all_comment_num():
    with connection.cursor() as cursor:
        sql = "SELECT count(1) as num FROM `comments`  where comment_id >= 0"
        cursor.execute(sql, ())
        return cursor.fetchone()

# 分页获取歌词信息
def get_comment_page(offset, size):
    with connection.cursor() as cursor:
        sql = "SELECT comment_id,`content` FROM `comments`  where comment_id >= 0 order by comment_id limit %s ,%s"
        cursor.execute(sql, (offset, size))
        return cursor.fetchall()


# 保存歌词
def insert_lyric(music_id, lyric):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `lyrics` (`music_id`, `lyric`) VALUES (%s, %s)"
        cursor.execute(sql, (music_id, lyric))
    connection.commit()


# 获取所有歌手的 数量  评论到 192913  歌词 64551
def get_all_music_num():
    with connection.cursor() as cursor:
        sql = "SELECT count(1) as num FROM `musics`  where music_id >= 192913"
        cursor.execute(sql, ())
        return cursor.fetchone()


# 分页获取歌手的 ID
def get_music_page(offset, size):
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `musics`  where music_id >= 192913 order by music_id limit %s ,%s"
        cursor.execute(sql, (offset, size))
        return cursor.fetchall()


# 保存音乐
def insert_music(music_id, music_name, album_id):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `musics` (`music_id`, `music_name`, `album_id`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, music_name, album_id))
    connection.commit()


# 保存专辑
def insert_album(album_id, artist_id, title, img):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `albums` (album_id, artist_id, title, img ) VALUES (%s, %s,%s,%s)"
        cursor.execute(sql, (album_id, artist_id, title, img))
    connection.commit()


# 保存歌手
def insert_artist(artist_id, artist_name):
    with connection.cursor() as cursor:
        sql = "INSERT INTO `artists` (`artist_id`, `artist_name`) VALUES (%s, %s)"
        cursor.execute(sql, (artist_id, artist_name))
    connection.commit()


# 获取所有歌手的 数量
def get_all_artist_num():
    with connection.cursor() as cursor:
        sql = "SELECT count(1) as num FROM `artists` "
        cursor.execute(sql, ())
        return cursor.fetchone()


# 分页获取歌手的 ID
def get_artist_page(offset, size):
    with connection.cursor() as cursor:
        sql = "SELECT `artist_id` FROM `artists` limit %s ,%s"
        cursor.execute(sql, (offset, size))
        return cursor.fetchall()


# 获取所有专辑的 数量 歌曲到 36504028
def get_all_album_num():
    with connection.cursor() as cursor:
        sql = "SELECT count(1) as num FROM `albums` where album_id > 36503960 "
        cursor.execute(sql, ())
        return cursor.fetchone()


# 分页获取专辑的 ID
def get_album_page(offset, size):
    with connection.cursor() as cursor:
        sql = "SELECT `album_id` FROM `albums` where album_id > 36503960 limit %s ,%s"
        cursor.execute(sql, (offset, size))
        return cursor.fetchall()


# 获取所有音乐的 ID
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `musics` ORDER BY music_id"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()


# 清库
def truncate_all():
    with connection.cursor() as cursor:
        sql = "truncate table artists"
        cursor.execute(sql, ())
        sql = "truncate table albums"
        cursor.execute(sql, ())
        sql = "truncate table musics"
        cursor.execute(sql, ())
        sql = "truncate table comments"
        cursor.execute(sql, ())
        sql = "truncate table lyrics"
        cursor.execute(sql, ())
    connection.commit()
