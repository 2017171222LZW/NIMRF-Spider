from pathlib import Path
from random import random
from time import sleep

import requests

from src.ReqestData import requestImgUrl
from utils.agents import getAgent

excludeLetters = ['?', '|', ':', '*', '"', '\\', '<', '>']
# 生成本条记录图像的保存路径
def getSavePath(args, row):
    prefix = Path(args.save_path)
    _type = row["zym"]
    _file = row["tpzlArr"][0]
    for letter in excludeLetters:
        _file = _file.replace(letter, '')
        _type = _type.replace(letter, '')
    if not (prefix / _type).exists():
        (prefix / _type).mkdir(exist_ok=True, parents=True)
    return Path(prefix / _type / _file)


# 实现图像自动下载保存功能
# @:args
# @:row 单条数据
def AutoSaveImg(args, row):
    # 生成本条记录图像的保存路径
    filename = getSavePath(args, row)
    url = requestImgUrl(args.img_entry_url, row, args.resolution)
    # 跳过重复数据
    if filename.exists():
        print("Skipped Image: ", url)
        return
    print("Downloading Image: ", url, end=' ')
    try:
        # 使用随机代理尝试下载图像并保存
        response = requests.get(url, headers=getAgent(args))
        with open(filename, "wb") as f:
            f.write(response.content)
        # 随机延迟避免被API服务器检测
        sleep(random() * args.delay_sec)
    except Exception as e:
        print("<Failed>: ", e)
    print("<Success>")

