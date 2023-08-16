template = {
    "pageNum": 1,
    "pageSize": 10,
    "zyglbm.id": 13,
    "zyglbm.category": 3,
    "zyglbm.pageNum": 1,
    "zyglbm.pageSize": 1000,
    "delFlag": 0
}

log = {
    "total": -1, # 未更新
    "rows": [] # 空列表
}

record_log = {
        "zyglbm.id": -1, # zyglbm.id的索引
        "log": log, # 日志数据
        "start": 0,  # 当前页开始下载的位置
        "id": -1,  # 日志id号
        "path": '', # 日志文件路径
        "page_num": -1,  # 页码
        "pageSize": -1,  # 页大小
        "entry_url": "" # 请求url
}