import json
from pathlib import Path

from src.ImgSaver import AutoSaveImg
from src.ReqestData import requestInfoList
from utils.options import zyglbm_ids
from utils.record import save_record, get_latest_logdir
from utils.template import template, record_log


# 实现爬虫核心引擎功能
# @:args 配置参数
def spider_engin(args):
    resume_log = None
    # 是否开启断电续传
    if args.resume:
        # 日志检测
        logf = get_latest_logdir()
        if logf is not None and Path(logf / 'log.json').exists():
            with open(logf / 'log.json', 'r', encoding='utf-8') as f:
                resume_log = json.load(f)
    if resume_log:
        print("Start resume spider from:", resume_log["path"])
    # Top level-class
    for idx, zi in enumerate(zyglbm_ids):
        # 跳过已经下载的内容
        if resume_log and idx < resume_log["zyglbm.id"]:
            continue
        # 记录当前爬取的样本所属的大类别
        template["zyglbm.id"] = zi
        # 第一次尝试，获取总样本数等相关参数
        log = requestInfoList(args)
        print("about ", log["total"], " rock images will be download.")
        # 爬取图像的info
        for page_num in range(resume_log["zyglbm.id"] if resume_log else 1,
                              log["total"] // args.batch_size + 1):
            # 设定info分页查询相关参数
            template["pageSize"] = args.batch_size
            template["pageNum"] = page_num
            log = requestInfoList(args)
            # 记录本次batch的相关信息
            record_log["zyglbm.id"] = idx
            record_log["log"] = log
            record_log["page_num"] = page_num
            record_log["pageSize"] = args.batch_size
            record_log["entry_url"] = args.entry_url
            # 保存日志
            save_record(record_log)
            # 遍历 rows 获取 img
            rows_loop(args, log["rows"], record_log)
            # 新的batch需要重置下载点
            record_log["start"] = 1

    print('Spider Completely.')


# 实现单页数据的爬取
# @:return None
# @:arg 配置参数
# @:rows 单页的所有记录
# @:recordLog 本次分页查询对应的本地日志对象
def rows_loop(args, rows, recordLog):
    for idx, row in enumerate(rows):
        if idx < recordLog["start"]:
            continue
        # 先保存下载点，发生下载失败，下次可接着下载进度
        recordLog["start"] = idx
        save_record(recordLog)
        # 自动下载保存图片
        AutoSaveImg(args, row)
