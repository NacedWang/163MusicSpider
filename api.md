### 内容转自 [Archiewyq/music_163](https://github.com/Archiewyq/music_163)

> 作者不保证可行性

用户信息：
http://music.163.com/api/v1/user/detail/373540275
373540275为用户id

用户歌单列表
http://music.163.com/api/user/playlist/?offset=1&limit=10&uid=373540275
offset为偏移量，limit为每页返回条数，uid为用户id

用户关注者列表
http://music.163.com/api/user/getfolloweds/373540275
373540275为用户id

用户动态
http://music.163.com/api/event/get/373540275
373540275为用户id

电台列表
http://music.163.com/api/dj/program/373540275
373540275为电台主播id

歌单详情
http://music.163.com/api/playlist/detail?id=2765813847
2765813847为歌单id

歌词获取
http://music.163.com/api/song/lyric?id=1363686359&lv=1&kv=1&tv=-1
id为歌曲id，tv=-1(不翻译) tv=1(翻译)

歌曲评论：
http://music.163.com/api/v1/resource/comments/R_SO_4_26075485?limit=10&offset=100
26075485为歌曲id，limit为每页评论数，offset为评论数偏移量

专辑详情
https://music.163.com/api/album/18903
18903为专辑id

专辑评论：
http://music.163.com/api/v1/resource/comments/R_AL_3_18903
18903为专辑id

搜索
http://music.163.com/api/search/suggest?s=%E7%8E%8B%E8%8F%B2&type=2
s为搜索关键字，type为搜索类型：1(默认，单曲搜索) 10(专辑搜索) 100(歌手搜索) 1000(歌单搜索) 1002(用户搜索) 1004(mv搜索)

歌词搜索
http://music.163.com/api/song/media?id=34367845
34367845为歌曲id

歌手mv
https://music.163.com/api/artist/mvs?artistId=6460
artistId为歌手id

歌手专辑
https://music.163.com/api/artist/albums/6460
6460为歌手id