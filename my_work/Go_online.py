#!/usr/bin/python3
#测试 开发 运维

import os
import time
import subprocess
subprocess.getoutput('cp -r 部署文件/. .')
subprocess.getoutput('uwsgi --ini /Item/my_work/uwsgi.ini')
subprocess.getoutput('cp nginx.conf /etc/nginx')
subprocess.getoutput('service nginx start')
subprocess.getoutput('python SendEmail.py')
print('部署成功')

# for i in command_list :
#     i
#     print()

#os.system('command')  执行命令,执行成功返回0，否则返回一个随机的数字
#os.system('\nls\n')

#os.popen('command')   执行命令，但没有返回，就无法赋值给变量
#os.popen('touch k5.py')

#都是完成一个命令之后才继续执行，但是命令执行成功还是出错都会继续执行
#subprocess.getoutput('command')  执行命令，返回命令后的结果
#subprocess.getoutput('ls')
#x = subprocess.getoutput('ls')

#subprocess.getstatusoutput('command')  执行命令。返回命令后的状态0成功127出错，结果，为元组
#subprocess.getstatusoutput('touch1 k6.py')
#subprocess.getstatusoutput('touch1 k6.py')

#subprocess.check_call('command')  执行命令，返回结果和状态，正常为0 ，执行错误则抛出异常
#subprocess.check_call('touch k7.py')