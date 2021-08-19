'''
Author: MuZonghan
Date: 2021-07-29 16:31:26
LastEditTime: 2021-08-16 17:24:57
Descripition: 挑选存在规定类别的txt文件,并匹配图片
    ## path_ori: 总目录文件夹,包含txt以及img文件
    ## path_select_txt: 挑选出的txt文件目录
    ## path_select_img: 挑选出的img文件目录
FilePath: /4pcodes/learncodes/select.py
'''
import os
import sys
import shutil


select_classes = ['2']
path_ori = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/txt-match1/'
path_select_txt = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/txt0/'
# path_select_img = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/select-img/'
if not os.path.exists(path_select_txt):
    os.mkdir(path_select_txt)
# if not os.path.exists(path_select_img):
#     os.mkdir(path_select_img)

label_list = os.listdir(path_ori)
# print(label_list)
num = 0
for filename in label_list:
    if filename.endswith('.txt'):
        f_ori = open(path_ori + filename, 'r')
        lines = f_ori.readlines()
        img_name = filename[:-4]+'.jpg'
        for line in lines:
            line1 = line.strip('\n').split(" ")
            # print(line[0])
            if line[0] in select_classes:
                # print(line[0])
                num = num+1
                # print(num)
                # shutil.copyfile(os.path.join(path_ori,filename), os.path.join(path_select_txt,filename))
                # shutil.copyfile(os.path.join(path_ori,img_name), os.path.join(path_select_img,img_name))
                break
                # continue
print("done", str(num))


