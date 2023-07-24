'''
Author: MuZonghan
Date: 2021-07-23 15:20:07
LastEditTime: 2021-08-19 15:14:07
Descripition: 统计xml文件的类别数目
FilePath: /4pcodes/learncodes/xml_read2.py
'''
import os
import xml.dom.minidom
 
xml_path = '/home/trunk/muzklj/5datasets/bigdata/img-txt2/sec-all1-xml/'
files = os.listdir(xml_path)
 
gt_dict = {}
 
if __name__ == '__main__':
    
    for xm in files:
        xmlfile = xml_path + xm
        dom = xml.dom.minidom.parse(xmlfile)  # 读取xml文档
        root = dom.documentElement  # 得到文档元素对象
        filenamelist = root.getElementsByTagName("filename")
        filename = filenamelist[0].childNodes[0].data
        objectlist = root.getElementsByTagName("object")
        
        for objects in objectlist:
            namelist = objects.getElementsByTagName("name")
            objectname = namelist[0].childNodes[0].data
            if objectname == '-':
                print(filename)
            if objectname in gt_dict:
                gt_dict[objectname] += 1
            else:
                gt_dict[objectname] = 1
    dic = sorted(gt_dict.items(), key=lambda d: d[1], reverse=True)
    print(dic)
    # print(len(dic))