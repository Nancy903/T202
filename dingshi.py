import requests
import time
import ssl
from apscheduler.schedulers.background import BackgroundScheduler

def openUrl():
    requests.get("https://www.baidu.com")
    ssl._create_default_https_context = ssl._create_unverified_context
    print("Access to success.")

if __name__ == '__main__':
    # 创建后台执行的 schedulers
    scheduler = BackgroundScheduler()

    # 每隔5分钟执行一次
    scheduler.add_job(openUrl, 'interval', minutes=5)

    # 启动调度任务
    scheduler.start()
    while True:
        time.sleep(5)