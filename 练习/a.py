import datetime


def detail_sql(self, task_show_time, task_start_time, task_end_time, task_play_count, task_play_all_count,
               task_play_increment, task_cost,
               task_shopping_price, task_shop_price, task_used_price, task_used_order, task_used_price_roi,
               task_used_one_price, task_used_order_price, task_used_income_roi, task_all_order):
    # sum = task_play_count + task_play_all_count
    # n = time.time()
    # # select task_play_count, b, c, d, e, f, g, a + b + c + d + e + f + g from dou_task_detail
    # task_start_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(n))
    # b = n - 10*60
    # task_end_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(b))
    dt = datetime.datetime.now().strftime("%Y-%m-%d  %H:%M:%S")
    sql = 'insert into dou_task_detail (task_show_time,task_start_time,task_end_time,task_play_count,task_play_all_count,task_play_increment,task_cost,task_shopping_price,task_shop_price,task_used_price,task_used_order,task_used_price_roi,task_used_one_price,task_used_order_price,task_used_income_roi,task_all_order) values(%s, %s,%s, %s,%s, "%s", "%s", "%s","%s", "%s", "%s", "%s","%s", "%s", "%s", "%s")'
    # item = {"task_show_time": task_show_time, "task_start_time": time.strftime("%Y-%m-%d %H:%M:%S"), "task_end_time": time.strftime("%Y-%m-%d %H:%M:%S"), "task_play_count": task_play_count,"task_play_all_count": task_play_all_count,"task_play_increment": task_play_increment,"task_cost": task_cost,
    #         "task_shopping_price": task_shopping_price, "task_shop_price": task_shop_price, "task_used_price": task_used_price,"task_used_price_roi": task_used_price_roi,"task_used_one_price": task_used_one_price,"task_used_order_price": task_used_order_price
    #         ,"task_used_income_roi": task_used_income_roi,"task_all_order": task_all_order}
    self.__cursor.execute(sql, (
    task_show_time, task_start_time, task_end_time, task_play_count, task_play_all_count, task_play_increment,
    task_cost, task_shopping_price, task_shop_price, task_used_price, task_used_order, task_used_price_roi,
    task_used_one_price,
    task_used_order_price, task_used_income_roi, task_all_order))
    self.__conn.commit()
