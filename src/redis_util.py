import redis

# redis 连接
connection = redis.Redis(host='127.0.0.1', port=6379)

# redis工程前缀
projectPrefix = '163music:'
# 歌词前缀
lyricPrefix = projectPrefix + 'lyric:'
# 评论前缀
commentPrefix = projectPrefix + 'comment:'
# 歌曲前缀
musicPrefix = projectPrefix + 'music:'


# 查看key是否存在
def checkIfRequest(prefix, url):
    if url is None:
        raise Exception("redis checkIfRequest get no url")
    res = connection.exists(prefix + url)
    if res > 0:
        return True
    else:
        return False


# 保存key
def saveUrl(prefix, url):
    if url is None:
        raise Exception("redis saveUrl get no url")
    res = connection.set(prefix + url, url)
    if not res:
        raise Exception("redis saveUrl fail")
    return res
