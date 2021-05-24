class MySQLPipeline:
    def __init__(self):
        database = name
        self.__conn = pymysql.connect(host=host, user=user, password=password, database=database, charset="utf8")
        self.__cursor = self.__conn.cursor(cursor=pymysql.cursors.DictCursor)
        self.cache_count = 0
        self.cache_list = []

    def list_sql(self, id, desc, video_play_url,play_increment,cost,shopping_click,shopping_price,shop_price,used_price,used_order,used_price_roi,used_one_price,used_order_price):
        count = "SELECT play_increment+cost+shopping_click+shopping_price+shop_price+used_price+used_order+used_price_roi+used_one_price+used_order_price AS Total FROM  `dou_task`;"
        sql = """INSERT INTO dou_task (id, desc, video_play_url,play_increment,cost,shopping_click,shopping_price,shop_price,used_price,used_order,used_price_roi,used_one_price,used_order_price)VALUES('%s', '%s','%s','%s', '%s', '%s','%s','%s', '%s', '%s','%s','%s','%s')"""

        self.__cursor.execute(sql,(id, desc, video_play_url,play_increment,cost,shopping_click,shopping_price,shop_price,used_price,used_order,used_price_roi,used_one_price,used_order_price))
        self.__conn.commit()

        self.__conn.rollback()

    def detail_sql(self,dou_task_id,id,show_time,start_time,end_time,play_count, play_all_count, play_increment, cost,
                   shopping_price, shop_price, used_price, used_order, used_price_roi,
                   used_one_price, used_order_price, used_income_roi, all_order):
        count2 = "SELECT task_play_count + task_play_all_count + task_play_increment + task_cost + task_shopping_price + task_shop_price + task_used_price + task_used_order + task_used_price_roi +task_used_one_price + task_used_order_price + task_used_income_roi + task_all_order AS Total FROM  `dou_task_detail`;"
        sql = """insert into dou_task_detail (dou_task_id,id,show_time,task_start_time,end_time,play_count,play_all_count,play_increment,cost,shopping_price,task_shop_price,used_price,used_order,used_price_roi,used_one_price,used_order_price,used_income_roi,all_order) values(%s,%s, %s,%s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s, %s, %s, %s,%s)"""
        try:
            self.__cursor.execute(sql,count2,(dou_task_id,id,show_time,start_time,end_time,play_count, play_all_count, play_increment, cost, shopping_price,shop_price, used_price, used_order, used_price_roi,used_one_price, used_order_price, used_income_roi, all_order))
            self.__conn.commit()
        except:
            self.__conn.rollback()

    def close_spider(self):
        # 关闭光标对象
        self.__cursor.close()
        # 关闭数据库连接
        self.__conn.close()