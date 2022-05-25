import json
from operator import mod
from xml.etree import ElementTree as ET
import re
import os
import logging
import zipfile
import py7zr


log_file = "D:\\Git Project\\测试用\\日志.txt"
logger = logging.getLogger(__name__)
logger.setLevel(level = logging.INFO)
fh = logging.FileHandler(log_file)
fh.setLevel(logging.DEBUG)
file_formatter = logging.Formatter('%(asctime)s\t%(levelname)s\t%(name)s\t%(message)s')
fh.setFormatter(file_formatter)
logger.addHandler(fh)
sh = logging.StreamHandler()
sh.setLevel(logging.WARNING)
stream_formatter = logging.Formatter('%(asctime)s|%(levelname)s|%(message)s')
sh.setFormatter(stream_formatter)
logger.addHandler(sh)





# # 解压缩
# with py7zr.SevenZipFile("Archive.7z", 'r') as archive:
#     archive.extractall(path="/tmp")


# # 这一部分只是用来解释os.walk的用法，在该脚本运行时不需执行------start
# dirpath = r'D:\\Git Project\\测试用'  # 这里指定需要压缩的文件夹
# for path, dirnames, filenames in os.walk(dirpath):  # 遍历文件夹及下面的子文件夹，path、dirnames、filenames依次是路径、目录名称、文件名称。
# # path是当前路径，dirnames是在当前路径下有文件夹时，给出文件夹名的列表，filenames是在当前路径下有文件时，给出文件名的列表
# # 之后进入列表dirnames中的第一个文件夹，重复上述过程。
#     # 下面print出来可以更好体会os.walk的用法
#     print(path)
#     print(dirnames)
#     print(filenames)
#     fpath = path.replace(dirpath, '')  # 把主路径去掉，只保留分路径，这样在压缩文件时就不会把需要压缩的文件夹的上层路径压缩进去
#     print(fpath)
# # 这一部分只是用来解释os.walk的用法，在该脚本运行时不需执行------end


def getZipDir(dirpath, outFullName):
    """
    压缩指定文件夹
    :param dirpath: 目标文件夹路径
    :param outFullName: 压缩文件保存路径+xxxx.zip
    :return: 无
    """
    zip = zipfile.ZipFile(outFullName, "w", zipfile.ZIP_DEFLATED)  # outFullName为压缩文件的完整路径
    for path, dirnames, filenames in os.walk(dirpath):
        # 去掉目标跟路径，只对目标文件夹下边的文件及文件夹进行压缩
        fpath = path.replace(dirpath, '')

        for filename in filenames:
            zip.write(os.path.join(path, filename), os.path.join(fpath, filename))
    zip.close()




def autoXml():
    tree = ET.parse('D:\\Git Project\\测试用\\test.xml')
    root = tree.getroot() 
    person3 = ET.Element('person', {'name':'Brown'}) 
    age3 = ET.SubElement(person3, 'age') 
    age3.text = '20' 
    gender3 = ET.SubElement(person3, 'gender') 
    gender3.text = 'male' 
    #向根节点添加新的⼦节点 
    root.append(person3)
    prettyXml(root)
    # 将根目录转化为树行结构
    tree.write("D:\\Git Project\\测试用\\test.xml", encoding="UTF-8" , xml_declaration=True)
    
    
    # fileData = ""
    # with open("D:\\Git Project\\测试用\\hello.txt", 'r',  encoding="utf-8") as f:
    #     for line in f:
    #         if re.search("vim", line):
    #             line = line.replace("vim", "notepad++")    
    #         fileData += line
    # with open("D:\\Git Project\\测试用\\hello.txt",'w', encoding="utf-8") as f:
    #     f.write(fileData)


def prettyXml(element, indent = '', newline = '\n', level=0):
    if element:  # 判断element是否有子元素  
        if element.text == None or element.text.isspace(): # 如果element的text没有内容  
            element.text = newline + indent * (level + 1)    
        else:  
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)  
    #else:  # 此处两行如果把注释去掉，Element的text也会另起一行  
        #element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level  
    temp = list(element) # 将elemnt转成list  
    for subelement in temp:  
        if temp.index(subelement) < (len(temp) - 1): # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致  
            subelement.tail = newline + indent * (level + 1)  
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个  
            subelement.tail = newline + indent * level  
        prettyXml(subelement, indent, newline, level = level + 1) # 对子元素进行递归操作  


 
if __name__ == "__main__":
    # areas = ['chinaocean', 'NWPacific', 'NEPacific', 'SWPacific', 'SEPacific', 'IndianOcean']
    # for area in areas:
    #     getZipDir('D:\\Git Project\\测试用', 'D:\\Git Project\\测试用' + '.7z')
     # 压缩
    with py7zr.SevenZipFile("D:\\Git Project\\测试用", 'w') as archive:
        archive.writeall("D:\\Git Project\\测试用2.7z")
