"""
author:张鑫
date:2021/5/13 10:28
"""
import schedule
import threading
import time


def work():
    print('work')


def study():
    print('study')


def game():
    print('game')


def work_every_day():
    threading.Thread(target=work).start()


def study_every_day():
    threading.Thread(target=study).start()


def game_every_day():
    threading.Thread(target=game).start()


def run():
    schedule.every(3).seconds.do(work_every_day)
    schedule.every(5).seconds.do(study_every_day)
    schedule.every(7).seconds.do(game_every_day)


if __name__ == '__main__':
    while 1:
        schedule.every().second.do(run)
        schedule.run_pending()
        time.sleep(10)
