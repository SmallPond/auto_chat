# !/usr/bin/env python
# _*_coding:utf-8 _*_

# python chat.py filename.txt

import itchat
import time
import sys
import os

_set_time = "11：00"

_send_message = "It's time to go"
#_task_file = sys.argv[1]
_task_file = 'task_file.txt'

def login_chat_init():

    # 登录微信， hotReload热登录，一定时间内不需在扫描验证码
    itchat.auto_login(hotReload=True)
    # 获取备注、微信号、昵称中的任何一项等于name键值的用户
    # 不含参数则获取自己的信息
    #I = itchat.search_friends()
    #I.send("hello")
    #baby.send("hello")
    #print("## 你设定的时间：{0}\n## 对象：{1}\n## 信息：{2}".format(SET_TIME, Contacts, SEND_MESSAGE))
    #print("正在发送...")


# 通过读取文件来配置任务
def get_task():
    '''
    :return: 任务List
    '''
    taskList = []
    fileHander = open(_task_file, 'r', encoding='utf-8')      # 读取任务配置文件
    fileList = fileHander.readlines()
    for line in fileList:
        if line[0] == '#':                                   # 配置文件中可使用‘#’开头注释一行
            continue
        else:
            if len(line) > 6:                               # 时间 对象 信息 至少为6个长度
                taskList.append(line.split())                # 以空格分开
            else:
                continue                                    # 跳过空行和不符合规定的行
    return taskList


# 开始任务
def start_task(taskList):
    isInfoCorrect = True                       # 输入信息是否正确
    contact = ''
    for task in taskList:
        print("--------------------------------------")
        print("## 你设定的时间：{0}\n## 对象：{1}\n## 信息：{2}".format(task[0], task[1], task[2]))
        print("--------------------------------------\n")

    # 加入用户取消判断

    while True:
        # 使用 strftime 格式化输出
        local_time_clock = time.strftime("%H:%M", time.localtime())  # 时钟：分钟
        #print("现在时间为{0}".format(local_time_clock))
        for task in taskList:
            contact = itchat.search_friends(name=task[1])[0]
            if len(contact):
                if local_time_clock == task[0]:
                    contact.send(task[2])
                #else:
                    #contact.send("宝贝现在时间是:{0}, 我将在{1}通知你时间到了".format(local_time_clock, task[0]))
            else:
                print("你联系人中没有'{0}',请确认是否输入正确".format(task[1]))
                isInfoCorrect = False
                break
        time.sleep(60)              # 睡眠1分钟
        if isInfoCorrect == False:
            break


if __name__ == '__main__':
    #print(sys.argv[1])
    login_chat_init()
    taskList = get_task()
    start_task(taskList)



