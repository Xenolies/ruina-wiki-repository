# 删除文件名中指定字符

import os

# 输入文件夹地址
path = "."
files = os.listdir(path)

# 输出所有文件名，只是为了看一下
for file in files:
    print(file)

# 获取旧名和新名
i = 0
for file in files:
    # old 旧名称的信息
    old = path + os.sep + files[i]
    # new是新名称的信息，这里的操作是删除了最前面的'考拉很忙o - '共8个字符
    new = path + os.sep + file.replace(' ','')
    #new = "E://音乐//武林外传//1-10" + os.sep + file[8:]
    # 新旧替换
    os.rename(old,new)
    i+=1
