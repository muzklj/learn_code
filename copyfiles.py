'''
Author: MuZonghan
Date: 2021-08-06 10:39:49
LastEditTime: 2021-08-19 13:34:40
Descripition: 复制文件 
    ## copy_nums: 复制数目
    ## file_ends: 复制文件后缀
    ## path_ori: 原文件夹路径 
    ## path_copy: 复制文件夹路径
FilePath: /4pcodes/learncodes/copyfiles.py
'''
# -*- coding: UTF-8 -*-
import os 
import shutil
from tqdm import tqdm

def copy_files():
    #os.walk 取得原路径下的文件夹路径, 子文件名称, 所有文件名
    for foldname, subfolders, filenames in os.walk(path_ori):
        for filename in filenames:
            #复制规定数量
            for i in range(copy_nums):
                #复制规定后缀文件
                if filename.endswith(file_ends):
                    new_name = filename.replace(file_ends,'_copy_'+str(i)+file_ends)
                    shutil.copyfile(os.path.join(foldname,filename), os.path.join(path_copy,new_name))

if __name__ == '__main__':
    copy_nums = 15
    file_ends = '.xml'
    path_ori = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/xml-match/'
    path_copy = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/xml-match1/'
    if not os.path.exists(path_copy):
        os.mkdir(path_copy)
    copy_files()

