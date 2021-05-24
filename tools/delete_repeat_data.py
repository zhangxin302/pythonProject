"""
author:张鑫
date:2021/5/17 9:33
"""


def delete_repeat_data():
    import pymongo
    client = pymongo.MongoClient('localhost', 27017)
    db = client.local
    collection = db.person

    for url in collection.distinct('name'):  # 使用distinct方法，获取每一个独特的元素列表
        num = collection.count({"name": url})  # 统计每一个元素的数量
        print(num)
        for i in range(1, num):  # 根据每一个元素的数量进行删除操作，当前元素只有一个就不再删除
            print('delete %s %d times ' % (url, i))
            # 注意后面的参数， 很奇怪，在mongo命令行下，它为1时，是删除一个元素，这里却是为0时删除一个
            collection.remove({"name": url}, 0)
        for i in collection.find({"name": url}):  # 打印当前所有元素
            print(i)
            print(collection.distinct('name'))  # 再次打印一遍所要去重的元素
