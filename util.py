# import subprocess
import os

# def shell_exec(cmd_shell):
#     result = subprocess.run(cmd_shell, shell=True, stdout=subprocess.PIPE, text=True)

#     # 获取命令的标准输出
#     output = result.stdout
#     return output

def shell_exec(cmd_shell):
    # result = subprocess.run(cmd_shell, shell=True, stdout=subprocess.PIPE, text=True)
    # # 获取命令的标准输出
    # output = result.stdout
    # return os.system(cmd_shell)
    return os.popen(cmd_shell)
