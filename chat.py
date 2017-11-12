# !/usr/bin/env python
# _*_coding:utf-8 _*_
# python chat.py

# 若输入的联系人不存在，则函数返回空列表
# 若存在且为此名字的联系人存在多个则返回多个，默认使用第一个返回的用户
# 此程序暂时无法解决重复联系人的情况

# 2017.11.12  v1.0
# 判断操作系统， 在纯命令Linux系统中生成字符二维码
# 使用定时任务，不再简单的使用sleep方法
# 需要新安装库  pip install apscheduler

import itchat
import time
import os
import platform
from mychat import MyChat

# BlockingScheduler: 当调度器是你应用中唯一要运行的东西时使用。                         即阻塞
# BackgroundScheduler: 当你不运行任何其他框架时使用，并希望调度器在你应用的后台执行。
from apscheduler.schedulers.background import BackgroundScheduler


_task_file = 'task_file.txt'




def login_chat_init():
    # 区分Linux 与 Windows 系统
    os_paltform = platform.system()
    # 登录微信， hotReload热登录，一定时间内不需在扫描验证码, 显示字符二维码
    # for some linux system, width of block character is one instead of two, so enableCmdQR should be 2
    if os_paltform == "Windows":
        print("This is windows system\n")
        itchat.auto_login(hotReload=True)
    else:
        itchat.auto_login(hotReload=True, enableCmdQR=2)
    # 获取备注、微信号、昵称中的任何一项等于name键值的用户
    # 不含参数则获取自己的信息
    #I = itchat.search_friends()
    #I.send("hello")


# 通过读取文件来配置任务
def get_tasklist():
    '''
    :return: 读取任务文件，获得任务List
    '''
    taskList = []
    try:
        fileHander = open(_task_file, 'r', encoding='utf-8')      # 读取任务配置文件
    except IOError as e:
        print('配置文件{0}不存在'.format(_task_file))
        print("## 正在创建{0}文件...".format(_task_file))
        os.mknod(_task_file)                                               # 创建文件
        print("请在配置文件'{0}'中输入你的定时任务".format(_task_file))
        print("定时任务输入格式请查看README.txt文件")

    fileList = fileHander.readlines()
    # 信息过滤
    for line in fileList:
        if line[0] == '#':                                   # 配置文件中可使用‘#’开头注释一行
            continue
        else:
            if len(line) > 6:                                # 时间 对象 信息 至少为6个长度
                taskList.append(line.split())                # 以空格分开
            else:
                continue                                    # 跳过空行和不符合规定的行
    return taskList

def show_task(taskList):
    '''
    输出设定的任务
    :param taskList: 任务列表  调用get_task()返回
    :return:
    '''
    task_count = 0
    for task in taskList:
        print("--------------任务{0}-------------------".format(task_count))
        print("## 你设定的时间：{0}\n## 对象：{1}\n## 信息：{2}".format(task[0], task[1], task[2]))
        print("--------------------------------------")
        task_count += 1
    print("## 你共有{0}个定时发送的任务".format(task_count))

def get_task(taskList):
    '''
    获取任务， 转化为MyChat对象。  此处可以考虑和get_tasklist 合并，实现一步完成
    :param taskList:
    :return:
    '''
    contacts = []
    chatrooms_list = []
    contact_list = []
    is_info_correct = True  # 输入信息是否正确
    for task in taskList:
        contact_list = itchat.search_friends(name=task[1])  # 调用用户搜索函数
        # 未返回联系人信息则进行群组信息的获取
        if len(contact_list) == 0:
            # 调用群聊搜索函数
            chatrooms_list = itchat.search_chatrooms(name=task[1])
            # 群组信息获取失败，应该为用户输入信息错误
            if len(chatrooms_list) == 0:
                print("你输入的联系人信息错误.请检查是否输入正确 -> 联系人{0}".format(task[1]))
                # 信息输入错误
                is_info_correct = False
                break
            else:
                contacts.append(MyChat(chatrooms_list[0], task[0], task[1],task[2]))

        # 用户信息
        else:
            contacts.append(MyChat(contact_list[0], task[0], task[1], task[2]))

    if is_info_correct is False:
        return False
    else:
        return contacts


def run_task(chat_list):
    '''
    使用cron 形式开启线程，定时发送任务
    :param chat_list:
    :return:
    '''
    sched = BackgroundScheduler()
    time = []
    for chat_task in chat_list:
        time = chat_task.get_set_time().split(':')

        # print("{0}:{1}".format(time[0], time[1]))
        sched.add_job(chat_task.send, 'cron', hour=time[0], minute=time[1], second=0)
        sched.start()


if __name__ == '__main__':
    login_chat_init()                      # 登录微信
    taskList = get_tasklist()                  # 获取任务
    show_task(taskList)                              # 输出设定的任务
    chat_list = get_task(taskList)                   # 开始任务
    run_task(chat_list)
    print("配置成功")
    while True:
        # 主线程进入睡眠
        time.sleep(1000)
        pass


