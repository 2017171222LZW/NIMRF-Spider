import json
from pathlib import Path


def get_config():
    with open('config.json', 'r', encoding='utf-8') as f:
        config = json.load(f)
        return config


def save_record(record: dict):
    config = get_config()

    assert record.get("id") is not None
    assert record.get("path") is not None
    assert record.get("log") is not None
    # allocated log id and path
    if record["id"] <= 0:
        record["id"] = config["count"]
        config["count"] += 1
        record["path"] = config["dir"] + config["logs_name_prefix"] + str(record["id"])
    # log path
    path = Path('.').absolute() / Path(record["path"])
    # print(path)
    Path.mkdir(path, exist_ok=True, parents=True)
    # write log file
    with open(path / 'log.json', 'w', encoding='utf-8') as f:
        json.dump(record, f, ensure_ascii=False)
    # update config
    with open('config.json', 'w', encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False)


def get_latest_logdir():
    config = get_config()
    if config["count"] <= 1:
        return None
    path = Path('.').absolute() / (config["dir"] + config["logs_name_prefix"] + str(config["count"] - 1))
    # print(path)
    return path


if __name__ == '__main__':
    # save_record({"id": -1, "log": {}, "path": ""})
    get_latest_logdir()
