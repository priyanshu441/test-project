from email import message
from socket import timeout
from turtle import title
from plyer import notification
title =input('What is your title \n') 
message=input('enter your message \n') 
notification.notify(title=title,message=message,app_icon=None,timeout=10,toast= False)


