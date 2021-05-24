"""
author:张鑫
date:2021/5/17 9:34
"""


def delete_single_database_repeat_data():
    import pymongo
    client = pymongo.MongoClient('localhost', 27017)
    db = client.GifDB  # 这里是将要清洗数据的数据库名字
    for table in db.collection_names():
        print('table name is ', table)
        collection = db[table]
        for url in collection.distinct('gif_url'):  # 使用distinct方法，获取每一个独特的元素列表
            num = collection.count({"gif_url": url})  # 统计每一个元素的数量
            print(num)
            for i in range(1, num):  # 根据每一个元素的数量进行删除操作，当前元素只有一个就不再删除
                print('delete %s %d times ' % (url, i))
                # 注意后面的参数， 很奇怪，在mongo命令行下，它为1时，是删除一个元素，这里却是为0时删除一个
                collection.remove({"gif_url": url}, 0)
            for i in collection.find({"gif_url": url}):  # 打印当前所有元素
                print(i)
