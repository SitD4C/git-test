import json
from operator import mod
from xml.etree import ElementTree as ET
import re
import logging

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
    autoXml()
    logger.warning('Mission ComplETe')