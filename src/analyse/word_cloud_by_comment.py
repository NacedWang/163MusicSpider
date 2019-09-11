import datetime
import math

import jieba.analyse
import matplotlib.pyplot as plt
from matplotlib.image import imread
from wordcloud import WordCloud, STOPWORDS

from src import sql

if __name__ == '__main__':
    print("start analyse comment")
    startTime = datetime.datetime.now()
    print(startTime.strftime('%Y-%m-%d %H:%M:%S'))
    texts = []
    # 所有歌手数量
    comment_num = sql.get_all_comment_num()
    # 批次
    batch = math.ceil(comment_num.get('num') / 1000.0)
    print("batch:", batch)
    
    for index in range(0, batch):
        offset = 1000 * index
        comments = sql.get_comment_page(offset, 1000)
        print("index:", index, "offset:", offset, "artists :", len(comments), "start :", comments[0]['comment_id'])
        for item in comments:
            texts.append(item['content'])
    color_mask = imread("music.jpg")
    midTime = datetime.datetime.now()
    print("获取评论信息完毕，分析start:", midTime.strftime('%Y-%m-%d %H:%M:%S'))
    tags = jieba.analyse.extract_tags(str(texts), 1000, withWeight=True)
    data = {item[0]: item[1] for item in tags}

    word_cloud = WordCloud(scale=16,
                           font_path="msyh.ttc",
                           background_color="white",
                           max_words=400,
                           max_font_size=100,
                           width=1920,
                           mask=color_mask,
                           height=1080,
                           random_state=42).generate_from_frequencies(data)
    plt.figure()  # 创建一个图形实例
    plt.imshow(word_cloud)
    plt.axis("off")  # 不显示坐标尺寸
    plt.savefig('commentCloud.png', dpi=400)  # 指定分辨率
    # plt.show()

    print("finish analyse comment")
    endTime = datetime.datetime.now()
    print(endTime.strftime('%Y-%m-%d %H:%M:%S'))
    print("耗时：", (endTime - startTime).seconds, "秒")
