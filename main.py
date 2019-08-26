import datetime

from src import sql
from src.album_by_artist import albumSpider
from src.artists import artistSpider
from src.comments_by_music import commentSpider
from src.lyric_by_music import lyricSpider
from src.music_by_album import musicSpider

if __name__ == '__main__':
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
