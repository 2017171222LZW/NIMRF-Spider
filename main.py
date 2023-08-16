import argparse
import sys
from pathlib import Path

sys.path.append(Path.root)

from src.engin import spider_engin
from utils.agents import user_agents


def get_args_parser():
    parser = argparse.ArgumentParser('N.I.M.R.F. Database Spider for Info and Img')
    # info save: ./output/info and ./output/images
    parser.add_argument('--save-path',
                        default='output/rocks-1920/',
                        help="Information's save-path")
    parser.add_argument('--entry-url',
                        default="http://www.nimrf.net.cn/prod-api/ykhs/web/ykData/list",
                        help="The root url of api, in order to screw info")
    parser.add_argument('--save-img',
                        default=False,
                        help="Save all img or not")
    parser.add_argument('--img-entry-url',
                        default="http://nimrf.cugb.edu.cn/ykhsimgs/%deptCode/%resolution/%tpzlArr",
                        help="The api of img request-get")
    parser.add_argument('--resolution',
                        default=1920,
                        type=int,
                        help="choice rock image resolution. options[200, 1920]")
    parser.add_argument('--tree-save',
                        default=True,
                        type=bool,
                        help="Save data by tree structure mode.")
    parser.add_argument('--source-map',
                        default=None,
                        help="The source type mapper for N.I.M.R.F.")
    parser.add_argument('--source-type',
                        default='rock',
                        help="options: rock,miner,fossil")
    parser.add_argument('--batch-size',
                        default=50,
                        type=int,
                        help="crawl images batch size")
    # parser.add_argument('--agent', default='Mozilla/5.0 (Windows NT 10.0; Win64; x64)
    # AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.81 Safari/537.36 Edg/94.0.992.50', help="User Agent for
    # Spider")
    # random agent
    parser.add_argument('--agent-list',
                        default=user_agents,
                        help="User Agents for Spider")
    # delay
    parser.add_argument('--delay-sec',
                        default=0.3,
                        help="Spider will be suspend when request too freq to be refuse by API server")
    # resume
    parser.add_argument('--resume',
                        default=False,
                        help="Auto resume data crawl")

    args = parser.parse_args()
    return args


if __name__ == '__main__':
    args = get_args_parser()
    spider_engin(args)
