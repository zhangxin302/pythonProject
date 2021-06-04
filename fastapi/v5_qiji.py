#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2021/3/8 17:06
# @Author  : CoderCharm
# @File    : v5_qiji.py
# @Software: PyCharm
# @Github  : github/CoderCharm
# @Email   : wg_python@163.com
# @Desc    :
"""

第二版奇迹平台
    - 平行的第二个平台

和第二版 是一个账号，只是不同的展示


达中 数据

pip install sqlalchemy
pip install jinja2 aiofiles
pip install async-exit-stack async-generator

pip install python-jose


# 启动命令
nohup uvicorn v5_qiji:app --host=127.0.0.1 --port=8140 > v5.log 2>&1 &

kill -9 `lsof -t -i:8140`


http://dl.xinyunap.com/dladmin/advert/advert_list.html
登录名  公主
密码    096909

"""
import re
import math
import time
import hashlib
import traceback

import requests

from loguru import logger
from datetime import datetime
from typing import Generator, Union, Any

from parsel import Selector
from sqlalchemy import text
from sqlalchemy.orm import Session, sessionmaker
from fastapi import FastAPI, Request, Depends, Path, Body, APIRouter
from fastapi.exceptions import RequestValidationError
from fastapi.templating import Jinja2Templates
from sqlalchemy import create_engine
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore

from utils import create_access_token, check_jwt_token

Schedule = AsyncIOScheduler(
    jobstores={
        'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')
    }
)
Schedule.start()

# 线上
MYSQL_USER = "reptile3306"
MYSQL_PASSWORD = "reptILEke23491#3306"
MYSQL_HOST = "rm-m5e2qu1pjv9d4033r.mysql.rds.aliyuncs.com"
MYSQL_NAME = "cnzz_statistic"
MYSQL_PORT = 3306

# 测试
# MYSQL_USER = "root"
# MYSQL_PASSWORD = "Admin12345-"
# MYSQL_HOST = "172.16.137.129"
# MYSQL_NAME = "qiiji_db"
# MYSQL_PORT = 3306

# Mysql地址
SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{MYSQL_USER}:{MYSQL_PASSWORD}@" \
                          f"{MYSQL_HOST}/{MYSQL_NAME}?charset=utf8mb4"

engine = create_engine(SQLALCHEMY_DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

app = FastAPI(
    # debug=False,
    # openapi_url=None,
    # docs_url=None,
    # redoc_url=None,
    # swagger_ui_oauth2_redirect_url=None
)

headers = {
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"
}

templates = Jinja2Templates(directory="templates")

templates.env.block_start_string = '(% '  # 修改块开始符号
templates.env.block_end_string = ' %)'  # 修改块结束符号
templates.env.variable_start_string = '(( '  # 修改变量开始符号
templates.env.variable_end_string = ' ))'  # 修改变量结束符号
templates.env.comment_start_string = '(# '  # 修改注释开始符号
templates.env.comment_end_string = ' #)'  # 修改注释结束符号


def get_db() -> Generator:
    """
    获取sqlalchemy会话对象
    :return:
    """
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


# 简单定义返回
def resp_ok(*, code=0, msg="ok", data: Union[list, dict, str] = None) -> dict:
    return {"code": code, "msg": msg, "data": data}


def resp_fail(*, code=1, msg="fail", data: Union[list, dict, str] = None):
    return {"code": code, "msg": msg, "data": data}


def md5_hash(md5_data):
    """
    哈希数据
    :param md5_data:
    :return:
    """
    md5_value = hashlib.md5(md5_data.encode()).hexdigest()
    return md5_value


@app.exception_handler(RequestValidationError)
async def user_not_found_exception_handler(request: Request, exc: RequestValidationError):
    """
    token过期
    :param request:
    :param exc:
    :return:
    """
    logger.error(
        f"token 错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

    return {"code": 400, "msg": "请求参数错误"}


@app.exception_handler(Exception)
async def user_not_found_exception_handler(request: Request, exc: Exception):
    """
    token过期
    :param request:
    :param exc:
    :return:
    """
    logger.error(
        f"全局错误\nURL:{request.method}{request.url}\nHeaders:{request.headers}\n{traceback.format_exc()}")

    return {"code": 500, "msg": "其他错误"}


router = APIRouter()


@router.get("/multi/platform/{ad_ids}", include_in_schema=False)
async def query_target(
        request: Request,
        ad_ids: str = Path(..., title='指定的key'),
        *,
        db: Session = Depends(get_db)
):
    # 3667  和 4512    36674512kkkkk md5
    ad_list = ad_ids.split(",")
    if len(ad_list) <= 0:
        return {"code": -1, "msg": "格式错误"}

    ad_md5_id_list = []
    query_data = {}

    for index, ad_id in enumerate(ad_list):
        if ad_id:
            query_data[f"a{index}"] = ad_id
            ad_md5_id_list.append(f'qiji_key=:a{index}')

    query_task = " or ".join(ad_md5_id_list)

    sql = f"""SELECT ad_date, SUM(res_data) as res_data  from qiji_v5_data WHERE {query_task}
    GROUP BY ad_date ORDER BY ad_date DESC;"""

    ad_info_sql = f"""SELECT SUM(surplus_ip) as surplus_ip  from qiji_v5_ad_list WHERE {query_task};"""

    # 查询其中一个溢价即可 ad_list[0] 即可
    multiple_sql = f"""SELECT multiple from  qiji_v5_ad_list WHERE qiji_key=:qiji_key;"""

    data_info = db.execute(text(sql), query_data).fetchall()
    ad_info = db.execute(text(ad_info_sql), query_data).fetchone()
    multiple_info = db.execute(text(multiple_sql), {"qiji_key": ad_list[0]}).fetchone()

    # 溢价倍数
    multiple = multiple_info.multiple

    surplus_ip = math.ceil(int(ad_info.surplus_ip) * multiple)

    data_info = [{"ad_date": item.ad_date, "res_data": math.ceil(int(item.res_data) * multiple)} for item in data_info]

    return templates.TemplateResponse(
        "v4_target.html", {
            "request": request,
            "data_info": data_info,
            "ad_info": surplus_ip
        }
    )


@router.get("/chaoyue/login")
async def chaoyue_login(request: Request):
    return templates.TemplateResponse(
        "v5_login.html", {
            "request": request,
        }
    )


@router.post("/chaoyue/login")
async def auth_login(
        account: str = Body(..., embed=True),
        password: str = Body(..., embed=True)
):
    """
    简易的登录 就不通过数据库
    :param account:
    :param password:
    :return:
    """
    if account == "zhou" and password == "zhou":
        token = create_access_token(subject=account)
        return {"code": 0, "msg": "ok", "token": token}
    else:
        return {"code": 1, "msg": "用户名或密码错误!"}


@router.get("/chaoyue/admin")
async def chaoyue_admin(request: Request):
    return templates.TemplateResponse(
        "v5_admin.html", {
            "request": request,
        }
    )


@router.get("/chaoyue/crawl/plan")
async def chaoyue_crawl_plan(
        request: Request,
):
    """
    抓取指定url
    :return:
    """
    # logger.info(token)
    return templates.TemplateResponse(
        "v5_crawl_plan.html", {
            "request": request,
        }
    )


@router.get("/chaoyue/platform")
async def chaoyue_platform(
        token: Union[str, Any] = Depends(check_jwt_token),
        db: Session = Depends(get_db)
):
    sql = "SELECT platform from qiji_v5_data GROUP BY platform"

    platform_list = db.execute(text(sql)).fetchall()

    return {"code": 0, "msg": "ok", "data": platform_list}


@router.post("/chaoyue/data")
async def chaoyue_admin(
        token: Union[str, Any] = Depends(check_jwt_token),
        key_word: str = Body(None, alias="keyWord", embed=True),
        platform: str = Body(None, alias="platform", embed=True),
        db: Session = Depends(get_db)
):
    if key_word and platform:
        sql = """SELECT ad_id,ad_name,price,cate,multiple,surplus_ip,platform,qiji_key from qiji_v5_ad_list 
            where platform=:platform AND (ad_id LIKE '%' :key_word '%' OR ad_name LIKE '%' :key_word '%') """
    elif key_word and not platform:
        sql = """SELECT ad_id,ad_name,price,cate,multiple,surplus_ip,platform,qiji_key from qiji_v5_ad_list 
                   where ad_id LIKE '%' :key_word '%' OR ad_name LIKE '%' :key_word '%';"""
    elif platform and not key_word:
        sql = """SELECT ad_id,ad_name,price,cate,multiple,surplus_ip,platform,qiji_key from qiji_v5_ad_list 
                           where platform=:platform;"""
    else:
        sql = """SELECT ad_id,ad_name,price,cate,multiple,surplus_ip,platform,qiji_key from qiji_v5_ad_list;"""
    data_info = db.execute(text(sql), {"key_word": key_word, "platform": platform}).fetchall()

    return {"code": 0, "msg": "ok", "data": data_info}


@router.post("/chaoyue/multiple")
async def post_chaoyue_multiple(
        token: Union[str, Any] = Depends(check_jwt_token),
        multiple: float = Body(..., title="倍率", embed=True),
        qiji_key: str = Body(..., title="key", embed=True),
        db: Session = Depends(get_db),
):
    """
    更改溢价倍率
    :param token:
    :param multiple:
    :param qiji_key:
    :param db:
    :return:
    """
    multiple_sql = """UPDATE qiji_v5_ad_list SET multiple=:multiple WHERE qiji_key=:qiji_key"""

    db.execute(text(multiple_sql), {"multiple": multiple, "qiji_key": qiji_key})
    db.commit()

    return {"code": 0, "msg": "修改成功", "data": None}


@router.get("/crawl/all", tags=["schedule"], summary="获取所有job信息")
async def get_scheduled_syncs(
    token: Union[str, Any] = Depends(check_jwt_token),
):
    """
    获取所有job
    :return:
    """
    schedules = []
    for job in Schedule.get_jobs():
        schedules.append(
            {"job_id": job.id, "func_args": job.args, "cron_model": str(job.trigger),
             "next_run": str(job.next_run_time)}
        )
    return resp_ok(data=schedules)


# interval 固定间隔时间调度
@router.post("/crawl/schedule", tags=["schedule"], summary="开启定时:间隔时间循环")
async def add_interval_job(
        token: Union[str, Any] = Depends(check_jwt_token),
        cron_time: int = Body(120, title="循环间隔时间/秒,默认120s", embed=True),
        target_url: str = Body(..., title="任务id", embed=True),
):
    job_id = md5_hash(target_url)
    if len(target_url) <= 5:
        return resp_fail(msg="URL不能为空")

    res = Schedule.get_job(job_id=job_id)
    if res:
        return resp_fail(msg=f"{target_url} 任务已经存在")

    schedule_job = Schedule.add_job(crawl_task,
                                    'interval',
                                    args=(target_url,),
                                    seconds=cron_time,  # 循环间隔时间 秒
                                    id=job_id,  # job ID
                                    next_run_time=datetime.now()  # 立即执行
                                    )
    return resp_ok(data={"job_id": schedule_job.id})


@router.post("/crawl/del", tags=["schedule"], summary="移除任务")
async def remove_schedule(
        token: Union[str, Any] = Depends(check_jwt_token),
        job_id: str = Body(..., title="任务id", embed=True)
):
    res = Schedule.get_job(job_id=job_id)
    if not res:
        return resp_fail(msg=f"没有找到任务{job_id}")
    Schedule.remove_job(job_id)
    return resp_ok(msg="正常删除")


@router.post("/crawl/test", summary="URL请求测试")
async def crawl_test(
        token: Union[str, Any] = Depends(check_jwt_token),
        url: str = Body(..., title="任务id", embed=True)
):
    try:
        resp = crawl_task_test(url)
        return resp_ok(msg="解析正常", data=resp)
    except Exception as e:
        return resp_fail(msg=f"解析失败,出错{e}")


def crawl_task(target_url: str) -> None:
    """
    抓取指定内容
    :param target_url:
    :return:
    """
    logger.info("启动")
    db = SessionLocal()
    try:
        requests_and_parse_table(target_url, db)
    finally:
        db.close()
    logger.info(target_url, time.strftime("'%Y-%m-%d %H:%M:%S'"))


def requests_and_parse_table(url: str, db: Session):
    """
    :param url:  抓取链接地址
    :param db:  抓取链接地址
    :return:
    """
    logger.info(f"抓取url为{url}")
    resp = requests.get(url, headers=headers, verify=False, timeout=10)

    # 解析出文本你数据
    consume_ip, surplus_ip = parse_html_data(resp.text)

    logger.info(f"{consume_ip} - {surplus_ip}")

    qiji_key = md5_hash(url)

    el_select = Selector(text=resp.text)

    platform = el_select.xpath("//div[@id='content']/h1/text()").extract_first()
    logger.info(platform)

    sql = """INSERT into qiji_v5_ad_list(ad_id, href,consume_ip,surplus_ip,create_time,qiji_key,platform)values(:ad_id,
    :href,:consume_ip,:surplus_ip,:create_time,:qiji_key,:platform) ON DUPLICATE KEY 
    UPDATE consume_ip=:consume_ip,surplus_ip=:surplus_ip,platform:=platform;"""

    item = {"ad_id": qiji_key, "href": url, "consume_ip": consume_ip, "surplus_ip": surplus_ip,
            "create_time": time.strftime("%Y-%m-%d %H:%M:%S"), "qiji_key": qiji_key, "platform": platform}
    db.execute(text(sql), item)
    db.commit()

    tr_list = el_select.xpath("//tr")
    for item in tr_list[1:]:
        ad_date = item.xpath("./td[1]/text()").extract_first()
        res_data = item.xpath("./td[2]/text()").extract_first()

        logger.info(f"{ad_date} - {res_data}")

        data_sql = """INSERT IGNORE INTO qiji_v5_data (ad_id, ad_date, res_data, platform, qiji_key) VALUES(
                    :ad_id, :ad_date, :res_data, :platform, :qiji_key)"""

        db.execute(text(data_sql), {"ad_date": ad_date, "res_data": res_data, "ad_id": qiji_key, "platform": platform,
                                         'qiji_key': qiji_key, })

        update_sql = """UPDATE qiji_v5_data SET res_data=:res_data WHERE ad_date=:ad_date AND qiji_key=:qiji_key
        AND is_lock=0 AND platform=:platform"""

        db.execute(text(update_sql), {"res_data": res_data, "ad_date": ad_date,'qiji_key': qiji_key, "platform": platform})
        db.commit()


def parse_html_data(html_text: str):
    """
    解析文本数据
    :param html_text:
    :return:
    """
    # 消耗ip
    consume_ip = re.search(r"消耗:(.*?)IP", html_text)
    consume_ip = consume_ip.group(1)

    # 剩余ip
    surplus_ip = re.search(r"剩余:(.*?)IP", html_text)
    surplus_ip = surplus_ip.group(1)
    return consume_ip, surplus_ip


def crawl_task_test(url: str):
    logger.info(f"测试请求url {url}")
    resp = requests.get(url, headers=headers, verify=False, timeout=10)
    # 解析出文本数据
    consume_ip, surplus_ip = parse_html_data(resp.text)

    logger.info(f"{consume_ip} - {surplus_ip}")

    el_select = Selector(text=resp.text)
    platform = el_select.xpath("//div[@id='content']/h1/text()").extract_first()
    tr_list = el_select.xpath("//tr")
    day_consume = []
    for item in tr_list[1:6]:
        ad_date = item.xpath("./td[1]/text()").extract_first()
        res_data = item.xpath("./td[2]/text()").extract_first()
        day_consume.append({"ad_date": ad_date, "res_data": res_data})

    return {"consume_ip": consume_ip, "surplus_ip": surplus_ip, "platform": platform, "day_consume": day_consume}


app.include_router(router, prefix="/zhou")

if __name__ == '__main__':
    import uvicorn

    # 官方推荐是用命令后启动 在main.py同文件下下启动
    # uvicorn main:app --host=127.0.0.1 --port=8130 --workers=4
    uvicorn.run(app='v5_qiji:app', host="127.0.0.1", port=8140, reload=True, debug=True)

    # res = crawl_task_test("http://webadv.xinyunap.com/statistics?advert_id=A2BTY1NjB20")
    # logger.info(res)
    # crawl_task("http://adv.xinyunap.com/statistics?advert_id=DGleYwc2Vz0")
