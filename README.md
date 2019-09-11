![](https://img.shields.io/badge/Python-3.7.4-blue.svg)

# 163MusicSpider
一个获取网易云音乐歌手、专辑、歌曲、评论、歌词等数据的Python爬虫

会将获取的数据存储至`mysql`，并通过将url保存至 `redis` 做防重复爬取处理(网易云OS：你不要过来啊.jpg)

---
本爬虫未使用Scrapy框架，适合初学者查看使用

> 作者也是一名python初学者



<h3 id='file'>文件信息</h3>

1. 爬取所有的歌手信息 [artists.py](src/artists.py) 
2. 爬取专辑信息 [album_by_artist.py](src/album_by_artist.py)  
3. 爬取歌曲信息 [music_by_album.py](src/music_by_album.py)

    > 爬的多了可能被禁
                                                         
4. 爬取歌词信息 [lyric_by_music.py](src/lyric_by_music.py)
5. 爬取评论信息（热评+前1000条） [comments_by_music.py](src/comments_by_music.py)
6. 建表sql [db.sql](src/db.sql)

7. 评论词云分析 [word_cloud_by_comment.py](src/analyse/word_cloud_by_comment.py)

8. 评论词云分析结果 [commentCloud.png](src/analyse/commentCloud.png)

### 使用方法
* 爬取所有数据
    ###### 运行main.py
    
* 爬取单独数据
    ###### 到src目录下 找到 【[文件信息](#file)】 里的相应文件，解开最后两行的注释，运行
    
* 线程数设置
    ###### 每个文件都有一个  `pool = ProcessPoolExecutor(5)` 这个数字就是并发线程数，如果设置的过大会引起网易云的发爬虫机制，导致爬取失败
    
> *****爬取的时候注意下并发数，给网易云减少些服务器压力*****
    
### 更新计划
1. 爬取评论信息里的关联评论，能够使评论形成关联的故事
2. 爬取歌单信息，及歌单里包含的音乐
3. 形成数据分析报表，如：歌手歌曲排行、热门评论排行、用户评论排行、热门词汇、歌曲/歌手评论排行榜

---
### 参考
[RitterHou/music-163](https://github.com/RitterHou/music-163)

[python教程](https://www.liaoxuefeng.com/wiki/1016959663602400)

[Archiewyq/music_163](https://github.com/Archiewyq/music_163)

#### 感谢以上对本工程的帮助和支持


### 统计信息
> 截止2019-09-11
>> 已爬取33439歌手信息 ，290772专辑信息 ， 1802483歌曲信息 ，622398评论信息 ，2W+歌词信息

####  更新记录

| 时间 | 内容 | 备注 |
| ----- | ---- | ---- |
| 2019-08-28 | 增加redis，防重复爬取，增加网易云api文档 |  |
| 2019-09-11 | 增加评论词云分析，及60W+评论分析结果 ||
|  |  |  |