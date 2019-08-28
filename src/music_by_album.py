"""
根据专辑 ID 获取到所有的音乐 ID
"""
import datetime
import math
import random
import time
import traceback
from concurrent.futures.process import ProcessPoolExecutor

import requests
from bs4 import BeautifulSoup

from src import sql, redis_util
from src.util.user_agents import agents


class Music(object):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        # 获取数据多了之后，就会被禁用访问,可以使用代理
        'Cookie': 'MUSIC_U=f8b73ab123ddad32d44c37546522e06bb123363f4b813922a1902f2ds2ceb750c52sd32ccbb1ab2b9c23asd3a31522c7067cce3c7469;',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/album?id=71537',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def save_music(self, album_id):
        params = {'id': album_id}
        # 获取专辑对应的页面
        agent = random.choice(agents)
        self.headers["User-Agent"] = agent
        url = 'https://music.163.com/album?id=' + album_id
        # 去redis验证是否爬取过
        check = redis_util.checkIfRequest(redis_util.musicPrefix, url)
        if (check):
            print("url:", url, "has request. pass")
            time.sleep(2)
            return
        r = requests.get('https://music.163.com/album', headers=self.headers, params=params)

        # 网页解析
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        body = soup.body
        # 保存redis去重缓存
        redis_util.saveUrl(redis_util.musicPrefix, url)
        musics = body.find('ul', attrs={'class': 'f-hide'}).find_all('li')  # 获取专辑的所有音乐
        if len(musics) == 0:
            return
        for music in musics:
            music = music.find('a')
            music_id = music['href'].replace('/song?id=', '')
            music_name = music.getText()
            try:
                sql.insert_music(music_id, music_name, album_id)
            except Exception as e:
                # 打印错误日志
                print(music, ' inset db error: ', str(e))
                # traceback.print_exc()
                time.sleep(5)


def saveMusicBatch(index):
    my_music = Music()
    offset = 1000 * index
    albums = sql.get_album_page(offset, 1000)
    print("index:", index, "offset:", offset, " albums :", len(albums), "start")
    for i in albums:
        try:
            my_music.save_music(i['album_id'])
        except Exception as e:
            # 打印错误日志
            print(str(i) + ' interval error: ' + str(e))
            time.sleep(5)
    print("index:", index, "finished")


def musicSpider():
    print("======= 开始爬 音乐 信息 ===========")
    startTime = datetime.datetime.now()
    print(startTime.strftime('%Y-%m-%d %H:%M:%S'))
    # 所有专辑数量
    albums_num = sql.get_all_album_num()
    print("所有专辑数量：", albums_num)
    # 批次
    batch = math.ceil(albums_num.get('num') / 1000.0)
    # 构建线程池
    pool = ProcessPoolExecutor(3)
    for index in range(0, batch):
        pool.submit(saveMusicBatch, index)
    pool.shutdown(wait=True)
    print("======= 结束爬 音乐 信息 ===========")
    endTime = datetime.datetime.now()
    print(endTime.strftime('%Y-%m-%d %H:%M:%S'))
    print("耗时：", (endTime - startTime).seconds, "秒")

# if __name__ == '__main__':
#     musicSpider()
