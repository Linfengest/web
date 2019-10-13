#用于记录和Test
#测试 开发 运维

#测试用户: test开头
#测试用户密码： test12346

#request.user.username 获取用户名
#Go_online 部署文件
#dockerlife 使用自己已经年弄好的基础镜像只使用几条命令，解耦合的文件路径

#用于重定向url
#from django.shortcuts import reverse,redirect
#return redirect(reverse("show:upload"))
# 使用 from django.http import HttpResponsePermanentRedirect
# HttpResponsePermanentRedirect 重定向到展示文件的页面。这里的 code 唯一标示一个文件。
#     return HttpResponsePermanentRedirect("/s/" + code)
# from django.views.generic.simple import redirect_to
# (r'^test/$', redirect_to, {'url': '/author/'}),

#os.path.abspath(__file__)  当前文件路径
#os.path.dirname((os.path.abspath(__file__))  当前文件所在文件目录路径

#html判断用户是否登陆
#user.is_authenticated

import os
# x = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
x = os.path.abspath(__file__)
print(x)