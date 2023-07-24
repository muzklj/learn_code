'''
Author: MuZonghan
Date: 2021-07-23 11:53:09
LastEditTime: 2021-08-12 11:11:01
Descripition: 统计xml文件的类别数目
FilePath: /4pcodes/learncodes/xml_read.py
'''
# -*- coding:utf-8 -*-

import os
import xml.etree.ElementTree as ET
import numpy as np
# np.set_printoptions(suppress=True, threshold=np.nan)  ###python2
import sys
np.set_printoptions(suppress=True, threshold=sys.maxsize) ####python3 threshold=sys.maxsize
import matplotlib
from PIL import Image
 
def parse_obj(xml_path, filename):
    tree=ET.parse(xml_path+filename)
    objects=[]
    for obj in tree.findall('object'):
        obj_struct={}
        obj_struct['name']=obj.find('name').text
        # print(obj.find('name').text)
        objects.append(obj_struct)
    return objects
 
 
def read_image(image_path, filename):
    im=Image.open(image_path+filename)
    W=im.size[0]
    H=im.size[1]
    area=W*H
    im_info=[W,H,area]
    return im_info
 
 
if __name__ == '__main__':
    xml_path='/home/trunk/muzklj/5datasets/smalldata/xml-val/'
    filenamess=os.listdir(xml_path)
    filenames=[]
    for name in filenamess:
        name=name.replace('.xml','')
        filenames.append(name)
    recs={}
    obs_shape={}
    classnames=[]
    num_objs={}
    obj_avg={}
    # class1 = 0
    # class2 = 0
    # class3 = 0
    # class4 = 0
    for i,name in enumerate(filenames):
        recs[name]=parse_obj(xml_path, name+ '.xml' )
        # print(recs[name])
        # for j in range(len(recs[name])):
        # if {'name': '3-1'} in recs[name] or {'name': '3-2'} in recs[name] or {'name': '3-4'} in recs[name]:
        #     class1 = class1 + 1
        # if {'name': '3-2'} in recs[name]:
        #     class2 = class2 + 1
        # if {'name': '3-4'} in recs[name]:
        #     class3 = class3 + 1
        # if {'name': '4-2'} in recs[name]:
        #     class4 = class4 + 1

    for name in filenames:
        # print(name)
        for object in recs[name]:
            if object['name'] not in num_objs.keys():
                num_objs[object['name']]=1
            else:
                num_objs[object['name']]+=1
                
            if object['name'] not in classnames:
                classnames.append(object['name']) ###存储标签名称
            if object['name'] == 'busd':
                print(name)
    for name in classnames:
        print('{}:{}个'.format(name,num_objs[name]))

    # print(class1,class2,class3,class4)
    print('信息统计完毕。')
 
 