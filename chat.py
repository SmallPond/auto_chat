# !/usr/bin/env python
# _*_coding:utf-8 _*_

# python chat.py filename.txt

# 若输入的联系人不存在，则函数返回空列表
# 若存在且为此名字的联系人存在多个则返回多个
# 此程序暂时无法解决重复联系人的情况

import itchat
import time
import sys
import os
import urllib.request
import re

#_ task_file = sys.argv[1]
_task_file = 'task_file.txt'
_emoji_url = 'http://www.cnblogs.com/duojia/p/4552424.html'           # 爬取emoji表情




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
    try:
        fileHander = open(_task_file, 'r', encoding='utf-8')      # 读取任务配置文件
    except IOError as e:
        print('配置文件{0}不存在'.format(_task_file))
        print("## 正在创建{0}文件...".format(_task_file))
        os.mknod(_task_file)                                               # 创建文件
        print("请在配置文件{0}中输入你的定时任务".format(_task_file))
        print("定时任务输入格式青查看README.txt文件")

    fileList = fileHander.readlines()
    for line in fileList:
        if line[0] == '#':                                   # 配置文件中可使用‘#’开头注释一行
            continue
        else:
            if len(line) > 6:                                # 时间 对象 信息 至少为6个长度
                taskList.append(line.split())                # 以空格分开
            else:
                continue                                    # 跳过空行和不符合规定的行
    return taskList


# 开始任务
def start_task(taskList):
    is_info_correct = True                       # 输入信息是否正确
    task_count = 0
    is_send_complete = False
    contact = {}
    for task in taskList:
        print("--------------任务{0}-------------------".format(task_count))
        print("## 你设定的时间：{0}\n## 对象：{1}\n## 信息：{2}".format(task[0], task[1], task[2]))
        print("--------------------------------------\n")
        task_count += 1

    total_task = len(taskList)
    task_count = 0                                       # 清零 用于判断是否所有任务发送完成
    print("## 你共有{0}个定时发送的任务".format(total_task))

    # 加入用户取消判断

    while True:
        # 使用 strftime 格式化输出
        local_time_clock = time.strftime("%H:%M", time.localtime())  # 时钟：分钟
        for task in taskList:

            contact_list = itchat.search_friends(name=task[1])    # 调用用户搜索函数
            # 未返回联系人信息则进行群组信息的获取
            if len(contact_list) == 0:
                chatrooms_list = itchat.search_chatrooms(name=task[1])  # 调用群聊搜索函数
                # 群组信息获取失败，应该为用户输入信息错误
                if len(chatrooms_list) == 0:
                    print("你输入的联系人信息错误.请检查是否输入正确 -> 联系人{0}".format(task[1]))
                    is_info_correct = False
                    break
                else:
                    contact = chatrooms_list[0]                               # 取出最佳匹配
            else:
                contact = contact_list[0]

            if len(contact):
                if local_time_clock == task[0]:
                    contact.send(task[2])
                    print("###联系人:  '{0}'  的信息:   '{1}'  已经发送 ###".format(task[1], task[2]))
                    task_count += 1
                    #print("任务{0}".format(task_count))
                    if task_count == total_task:                   # 所有人文完成则退出程序
                        #print("计数已经到总任务数")
                        is_send_complete = True

            else:
                is_info_correct = False
                break                                              # 跳出for循环
        if is_info_correct is False:
            print("你联系人中没有'{0}',请确认联系人信息是否输入正确".format(task[1]))
            break                                                  # 跳出while 循环

        if is_send_complete is True:
            input("所有发送任务已经完成,请按任意键退出程序...")  # 等待用户结束程序
            break                                             # 跳出while 循环

        time.sleep(60)              # 睡眠1分钟





if __name__ == '__main__':

    login_chat_init()                      # 登录微信
    taskList = get_task()                  # 获取任务
    start_task(taskList)                   # 开始任务
    # contact = itchat.search_friends(name='一个宝贝儿')[0]
    # contact1 = itchat.search_friends(name='1234')
    # print(contact)
    # print(contact1)

