'''
Author: MuZonghan
Date: 2021-08-02 15:27:11
LastEditTime: 2021-08-12 10:49:48
Descripition: 读取图片并进行分类
FilePath: /4pcodes/home/trunk/muzklj/5datasets/bigdata/classify.py
'''
import glob
import cv2
import os
import shutil

files = glob.glob('/home/trunk/muzklj/5datasets/bigdata/classify/outputs/*.jpg')
file1 = '/home/trunk/muzklj/5datasets/bigdata/classify/false/'
file2 = '/home/trunk/muzklj/5datasets/bigdata/classify/true/'
# if not os.path.isfile(files):
#     print('%s not exist!'%(files))
# else:
#     fpath, fname = os.pardir.split(files)
#     print(fpath, fname)
if not os.path.exists(file1):
    os.mkdir(file1)
if not os.path.exists(file2):
    os.mkdir(file2)
    

for f in files:

    # width=1920
    # height=1080
    

    img = cv2.imread(f)
    cv2.namedWindow(os.path.basename(f), cv2.WINDOW_NORMAL)
    cv2.resizeWindow(os.path.basename(f), 1920,1080)
    # # cv2.setWindowProperty(f, cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)
    # cv2.moveWindow(os.path.basename(f), 100, 100)
    
    cv2.imshow(os.path.basename(f),img) #图片窗口以图片名称命名；
    k = cv2.waitKey(0)
    # print(f)
    # fpath, fname = os.path.split(f)
    # print(fpath, "#######",fname)
    # print(os.path.basename(f))
    if k == ord('f'):
        shutil.move(f, file1 + os.path.basename(f))
        # cv2.imwrite('use/'+os.path.basename(f),img) #将图片保存在当前目录下的use文件夹中,以原名称命名；
        cv2.destroyWindow(os.path.basename(f))
    elif k==ord('j'): 
        shutil.move(f, file2 + os.path.basename(f))
        cv2.destroyWindow(os.path.basename(f))
    elif k==ord(' '): 
        cv2.destroyWindow(os.path.basename(f))
    elif k==ord('q'):
        break
