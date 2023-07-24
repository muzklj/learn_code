#-*-coding:utf-8-*-
'''
Author: MuZonghan
Date: 2021-08-12 16:13:20
LastEditTime: 2021-08-13 15:51:39
Descripition: 遍历文件夹及其子文件夹文件, 输出文件路径
FilePath: /4pcodes/learncodes/file_path.py
'''

import os

root_path = '/home/trunk/muzklj/5datasets/highway'
# txt_path = '/home/trunk/muzklj/5datasets/highway/filename.txt'
txt_path = os.path.join(root_path, "filename.txt")
for foldname, subfolders, filenames in os.walk(root_path):
    
    for filename in filenames:
        # print(filename)
        if filename.endswith('.bag'):
            with open(txt_path, 'a') as f:
                f.write(os.path.join(foldname, filename)+'\n')

# file = open(txt_path, 'r')
# lines = file.readlines()
# for line in lines:
#     line = line.strip('\n')
#     input_path = line
#     output_path = line[:-4]
#     print(input_path)
#     print(output_path)
