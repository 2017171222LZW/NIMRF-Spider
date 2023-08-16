import json
import random
from time import sleep

import requests

from utils.agents import getAgent
from utils.template import template, log


# 获取信息列表
def requestInfoList(args):
    response = requests.request('GET', args.entry_url, params=template, headers=getAgent(args)).text
    response = json.loads(response)
    log["total"] = response["total"]
    log["rows"] = response["rows"]
    # random sleep
    sleep(random.random() * args.delay_sec)
    return log


def requestImgUrl(img_entry_url: str, row: dict, res: int):
    img_entry_url = img_entry_url.replace("%deptCode", row["deptCode"])
    img_entry_url = img_entry_url.replace("%tpzlArr", row["tpzlArr"][0])
    img_entry_url = img_entry_url.replace("%resolution", str(res))
    return img_entry_url
