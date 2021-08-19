'''
Author: MuZonghan
Date: 2021-08-03 13:11:56
LastEditTime: 2021-08-19 15:15:01
Descripition: 匹配同名不同后缀的文件
    ## ori_file: 匹配原文件路径
    ## all_file: 挑选总文件路径
    ## match_path: 匹配后的文件路径
FilePath: /4pcodes/learncodes/matchfile.py
'''
# -*- coding: UTF-8 -*-

import os
import shutil
from tqdm import tqdm

def img_match(ori_file, all_file, match_path):
    if not os.path.exists(match_path):
        os.mkdir(match_path)
    list = os.listdir(ori_file)
    # print(list)
    print("Waitting for a while...")
    j = 0
    for i in list:
        if i.endswith('.jpg'):
            img_name = all_file + i[:-4] + '.xml'
            # print(img_name)
            # print(os.path.exists(img_name))
            if os.path.exists(img_name):
                j = j + 1
                # name = img_name.replace('bus','sec-all-img')
                # print(name)
                shutil.copy(img_name, match_path)
                # print(img_name)
    print(str(j) + " Done!")

if __name__ == "__main__":
    ori_file = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/sec-all1-img/'
    all_file = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/xml/'
    match_path = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/sec-all1-xml/'
    img_match(ori_file, all_file, match_path)
