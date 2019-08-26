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
def insert_comments(music_id, comments, detail, connection0):
    with connection0.cursor() as cursor:
        sql = "INSERT INTO `comments` (`music_id`, `COMMENTS`, `DETAILS`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (music_id, comments, detail))
    connection0.commit()


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
        sql = "INSERT INTO `artists` (`ARTIST_ID`, `ARTIST_NAME`) VALUES (%s, %s)"
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
        sql = "SELECT `ARTIST_ID` FROM `artists` limit %s ,%s"
        cursor.execute(sql, (offset, size))
        return cursor.fetchall()


# 获取所有专辑的 数量
def get_all_album_num():
    with connection.cursor() as cursor:
        sql = "SELECT count(1) as num FROM `albums` "
        cursor.execute(sql, ())
        return cursor.fetchone()


# 分页获取专辑的 ID
def get_album_page(offset, size):
    with connection.cursor() as cursor:
        sql = "SELECT `album_id` FROM `albums` limit %s ,%s"
        cursor.execute(sql, (offset, size))
        return cursor.fetchall()


# 获取所有音乐的 ID
def get_all_music():
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `musics` ORDER BY music_id"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取前一半音乐的 ID
def get_before_music():
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `musics` ORDER BY music_id LIMIT 0, 800000"
        cursor.execute(sql, ())
        return cursor.fetchall()


# 获取后一半音乐的 ID
def get_after_music():
    with connection.cursor() as cursor:
        sql = "SELECT `music_id` FROM `musics` ORDER BY music_id LIMIT 800000, 1197429"
        cursor.execute(sql, ())
        return cursor.fetchall()


def dis_connect():
    connection.close()
