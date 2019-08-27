"""
根据专辑 ID 获取到所有的音乐 ID
"""
import datetime
import math
import random
import time
from concurrent.futures.process import ProcessPoolExecutor

import requests
from bs4 import BeautifulSoup

from src import sql
from src.util.user_agents import agents


class Music(object):
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
        'Accept-Encoding': 'gzip, deflate, sdch',
        'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Cookie': '_ntes_nnid=7eced19b27ffae35dad3f8f2bf5885cd,1476521011210; _ntes_nuid=7eced19b27ffae35dad3f8f2bf5885cd; usertrack=c+5+hlgB7TgnsAmACnXtAg==; Province=025; City=025; NTES_PASSPORT=6n9ihXhbWKPi8yAqG.i2kETSCRa.ug06Txh8EMrrRsliVQXFV_orx5HffqhQjuGHkNQrLOIRLLotGohL9s10wcYSPiQfI2wiPacKlJ3nYAXgM; P_INFO=hourui93@163.com|1476523293|1|study|11&12|jis&1476511733&mail163#jis&320100#10#0#0|151889&0|g37_client_check&mailsettings&mail163&study&blog|hourui93@163.com; _ga=GA1.2.1405085820.1476521280; JSESSIONID-WYYY=fb5288e1c5f667324f1636d020704cab2f27ee915622b114f89027cbf60c38be2af6b9cbef2223c1f2581e3502f11b86efd60891d6f61b6f783c0d55114f8269fa801df7352f5cc4c8259876e563a6bd0212b504a8997723a0593b21d5b3d9076d4fa38c098be68e3c5d36d342e4a8e40c1f73378cec0b5851bd8a628886edbdd23a7093%3A1476623819662; _iuqxldmzr_=25; __utma=94650624.1038096298.1476521011.1476610320.1476622020.10; __utmb=94650624.14.10.1476622020; __utmc=94650624; __utmz=94650624.1476521011.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none)',
        'DNT': '1',
        'Host': 'music.163.com',
        'Pragma': 'no-cache',
        'Referer': 'http://music.163.com/',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
    }

    def save_music(self, album_id):
        params = {'id': album_id}
        # 获取专辑对应的页面
        agent = random.choice(agents)
        self.headers["User-Agent"] = agent
        r = requests.get('https://music.163.com/album', headers=self.headers, params=params)

        # 网页解析
        soup = BeautifulSoup(r.content.decode(), 'html.parser')
        body = soup.body
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
                print(music + ' inset db error: ' + str(e))
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
    pool = ProcessPoolExecutor(5)
    for index in range(0, batch):
        pool.submit(saveMusicBatch, index)
    pool.shutdown(wait=True)
    print("======= 结束爬 音乐 信息 ===========")
    endTime = datetime.datetime.now()
    print(endTime.strftime('%Y-%m-%d %H:%M:%S'))
    print("耗时：", (endTime - startTime).seconds, "秒")

# if __name__ == '__main__':
#     musicSpider()
