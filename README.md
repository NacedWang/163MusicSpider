![](https://img.shields.io/badge/Python-3.7.4-blue.svg)

# 163MusicSpider
一个获取网易云音乐歌手、专辑、歌曲、评论、歌词等数据的Python爬虫

会将获取的数据存储至mysql

---
本爬虫未使用Scrapy框架，适合初学者查看使用

###### 作者也是一名python初学者


### 文件信息
1. 爬取所有的歌手信息 [artists.py](src/artists.py) 
2. 爬取专辑信息 [album_by_artist.py](src/album_by_artist.py)  
3. 爬取歌曲信息 [music_by_album.py](src/music_by_album.py)
4. 爬取歌词信息 [lyric_by_music.py](src/lyric_by_music.py)
5. 爬取评论信息（热评+前1000条） [comments_by_music.py](src/comments_by_music.py)
6. 建表sql [db.sql](src/db.sql)


### 使用方法
* 爬取所有数据
    ###### 运行main.py
    
* 爬取单独数据
    ###### 到src目录下 找到 【[文件信息](#文件信息)】 里的响应文件，解开最后一行的注释，运行
    


---
### 参考
[RitterHou/music-163](https://github.com/RitterHou/music-163)

[python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

#### 感谢以上对本工程的帮助和支持


### 统计信息
截止2019-08-26 
###### 已爬取31088歌手信息 ，17W专辑信息