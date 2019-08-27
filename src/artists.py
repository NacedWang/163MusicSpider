"""
获取所有的歌手信息
"""
import datetime

import requests
from bs4 import BeautifulSoup

from src import sql

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh-CN,zh;q=0.8,en;q=0.6',
    'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Cookie': '_ntes_nnid=8400bf2c060bc31cf9594e45f27a3fec,1563176153301; _ntes_nuid=8400bf2c060bc31cf9594e45f27a3fec; mail_psc_fingerprint=3bb841d2e82c66a598e20c722a2bc7e6; _ga=GA1.2.1695844012.1563176156; hb_MA-BFF5-63705950A31C_source=www.baidu.com; vinfo_n_f_l_n3=83751e6d9da80baf.1.0.1565690525602.0.1565937929199; JSESSIONID-WYYY=G9GF8EdTBb4vKhW07sJl%2FzJ1SngYTglBRTjO7pWuQZWjmsrUoRtEe2oeB7UtNmUsBb%2FeQI3TUZOi9nMwMrvCRkuvXnto7BSelMqYKpBkcb8o2XwvYtH0WfechA2y6lehTIxYrSDXu6mY%5CRxDbsqTXGaKCPDzQsyo2l%2B26c4w3MB0WwJ7%3A1566543736167; _iuqxldmzr_=32; WM_NI=OoTiNDHx4qjSbYmG1PqXdQwej8FpE8h7U6NpcM3jHZDCQ6aI8rzlAViZue3Y9BfwmA7KveDdl0cNeAVoAYihzax6fSnCEvmHwaSDyUKE5YEOpbfQFz4guPGT%2F7J8cWqCR1o%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eeb6b843b7b5bc8bb663a2928ea2d54e929b9aaab7339af5a6a4e55db6f0a399ec2af0fea7c3b92a8db19c8acd508ca8fc92e959a287a3a8b45cb388acb2f66faae88a91c834ace99bd7cd7ca193fd8bcb52889d9fd7e443fcaeb68dc45eab86bb86b253fb9eaa98f04bf595ba86c770b0f0adafe84b96b18fbaec64babfb8d7e559ae9d8b97f044b5bf9da5fc5f899bfbbac845b4beaab2c572f8b9bbb1c660ede986d9e25db39d9ed2ee37e2a3; WM_TID=lKkihvPjbwBAUFVEBQZ45Y%2FzXbD7xygm',
    'DNT': '1',
    'Host': 'music.163.com',
    'Pragma': 'no-cache',
    'Referer': 'https://music.163.com/',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36'
}


def save_artist(group_id, initial):
    params = {'id': group_id, 'initial': initial}
    print("== 爬取数据参数 ==", params)
    r = requests.get('https://music.163.com/discover/artist/cat', headers=headers, params=params)
    # 网页解析
    soup = BeautifulSoup(r.content.decode(), 'html.parser')
    # print(soup)
    labels = soup.find_all('a', attrs={'class': 'cat-flag'})
    hot_artists = soup.find_all('a', attrs={'class': 'msk'})
    artists = soup.find_all('a', attrs={'class': 'nm nm-icn f-thide s-fc0'})

    if not group_id:
        for label in labels:
            try:
                group_id = label['data-cat']
                if group_id:
                    labelList.add(group_id)
            except KeyError as e:
                # error: has not attribute
                print(e)
        print(labelList)

    for artist in hot_artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)

    for artist in artists:
        artist_id = artist['href'].replace('/artist?id=', '').strip()
        artist_name = artist['title'].replace('的音乐', '')
        try:
            sql.insert_artist(artist_id, artist_name)
        except Exception as e:
            # 打印错误日志
            print(e)


labelList = set([])


def artistSpider():
    print("======= 开始爬 歌手 信息 =======")
    startTime = datetime.datetime.now()
    print(startTime.strftime('%Y-%m-%d %H:%M:%S'))
    save_artist(None, None)
    for i in labelList:
        for j in range(65, 91):
            save_artist(i, j)
    print("======= 结束爬 歌手 信息 =======")
    endTime = datetime.datetime.now()
    print(endTime.strftime('%Y-%m-%d %H:%M:%S'))
    print("耗时：", (endTime - startTime).seconds, "秒")

# if __name__ == '__main__':
#     artistSpider()
