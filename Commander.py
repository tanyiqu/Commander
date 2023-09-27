
import easygui
import sys
from util import shell_exec

args = sys.argv
path = ''

if len(args) == 2:
    path = args[1]

else:
    exit(0)

cmds = []

# 读取文件内容
with open(path, 'r', encoding='utf8') as f:
    for line in f:
        cmds.append(line.strip())
        path
    pass

# print(cmds)

# import time

for cmd in cmds:
    # start = time.time()
    shell_exec(cmd)
    # end = time.time()
    # print(end - start)
    pass





# 弹出提示框
# easygui.msgbox(path, "提示")
