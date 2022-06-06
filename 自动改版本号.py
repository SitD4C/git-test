import time
import re
import os
import sys
import py7zr


#!/usr/bin/python
# -*- coding: utf-8 -*-


import re
import os
import tempfile

class Properties:

    def __init__(self, file_name):
        self.file_name = file_name
        self.properties = {}
        try:
            fopen = open(self.file_name, 'r')
            for line in fopen:
                line = line.strip()
                if line.find('=') > 0 and not line.startswith('#'):
                    strs = line.split('=')
                    self.properties[strs[0].strip()] = strs[1].strip()
        except Exception, e:
            raise e
        else:
            fopen.close()

    def has_key(self, key):
        return self.properties.has_key(key)

    def get(self, key, default_value=''):
        if self.properties.has_key(key):
            return self.properties[key]
        return default_value

    def put(self, key, value):
        self.properties[key] = value
        replace_property(self.file_name, key + '=.*', key + '=' + value, True)

def parse(file_name):
    return Properties(file_name)


def replace_property(file_name, from_regex, to_str, append_on_not_exists=True):
    file = tempfile.TemporaryFile()         #创建临时文件

    if os.path.exists(file_name):
        r_open = open(file_name,'r')
        pattern = re.compile(r'' + from_regex)
        found = None
        for line in r_open: #读取原文件
            if pattern.search(line) and not line.strip().startswith('#'):
                found = True
                line = re.sub(from_regex, to_str, line)
            file.write(line)   #写入临时文件
        if not found and append_on_not_exists:
            file.write('\n' + to_str)
        r_open.close()
        file.seek(0)

        content = file.read()  #读取临时文件中的所有内容

        if os.path.exists(file_name):
            os.remove(file_name)

        w_open = open(file_name,'w')
        w_open.write(content)   #将临时文件中的内容写入原文件
        w_open.close()

        file.close()  #关闭临时文件，同时也会自动删掉临时文件
    else:
        print "file %s not found" % file_name



def genTimeVersion():
    #十位
    #millis = int(time.time())
    #十三位
    millis = int(round(time.time() * 1000))
    return millis


if __name__ == '__main__':
    # currentPath  = os.path.dirname(sys.argv[0])
    currentPath  = os.getcwd()
    print(currentPath)
        
    # print(len(id))
    
#!/usr/bin/python
# -*- coding: utf-8 -*-

# import property

# file_path = '/Users/billy/Desktop/bak/test.properties' #要操作的properties文件的路径
# props = property.parse(file_path)   #读取文件
# props.put('key_a', 'value_a')       #修改/添加key=value
# print props.get('key_a')            #根据key读取value
# print "props.has_key('key_a')=" + str(props.has_key('key_a'))   #判断是否包含该key1
