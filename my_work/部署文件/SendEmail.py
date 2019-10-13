#邮件编辑器
from email.header import Header
from email.mime.text import MIMEText
#邮件发送模块
import smtplib
#服务器信息

def SendEmail(email,name,subject,text):
    from_addr = '13263183766@163.com'
    password = 'qq157793728' #授权码
    smtp_server = 'smtp.163.com'

    #收件人地址
    #to_addr = '157793728@qq.com'
    to_addr = email

    msg = MIMEText(text,'plain','utf-8')
    msg['From'] = from_addr  #邮件 发件人名字
    msg['To'] = name      #邮件 发件人名字
    msg['Subject'] = Header(subject,'utf-8') #邮件主题
    #msg = MIMEText('error 运行出错','plain','utf-8')
    #msg['From'] = from_addr  #邮件 发件人名字
    #msg['To'] = 'admin'      #邮件 发件人名字
    #msg['Subject'] = Header('运行状态','utf-8') #邮件主题
        
    try:
        server = smtplib.SMTP(smtp_server,25)
        server.login(from_addr,password)
        server.sendmail(from_addr,[to_addr],msg.as_string())
        server.quit()
        print('邮件发送成功')
    except:
        print('email：发送失败')

if __name__=='__main__':
    Send=SendEmail('157793728@qq.com','admin','运行状态','网站已经部署上线')
