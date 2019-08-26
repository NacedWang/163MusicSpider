import datetime
import sys
import os

from src import sql
from src.album_by_artist import albumSpider
from src.artists import artistSpider
from src.comments_by_music import commentSpider
from src.lyric_by_music import lyricSpider
from src.music_by_album import musicSpider

# 保存日志
class Logger(object):
    def __init__(self, filename="Default.log"):
        self.terminal = sys.stdout
        self.log = open(filename, "a")

    def write(self, message):
        self.terminal.write(message)
        self.log.write(message)

    def flush(self):
        pass


if __name__ == '__main__':
    path = os.path.abspath(os.path.dirname(__file__))
    type = sys.getfilesystemencoding()
    sys.stdout = Logger('log.txt')
    print("开始爬干净网易云音乐")
    startTime = datetime.datetime.now()
    print(startTime.strftime('%Y-%m-%d %H:%M:%S'))
    # 清空数据库
    sql.truncate_all()
    print("清空数据库完成")
    # 开始执行
    artistSpider()
    albumSpider()
    musicSpider()
    lyricSpider()
    commentSpider()
    endTime = datetime.datetime.now()
    print(endTime.strftime('%Y-%m-%d %H:%M:%S'))
    print("耗时：", (endTime - startTime).seconds, "秒")
