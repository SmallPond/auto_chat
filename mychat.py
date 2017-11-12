# !/usr/bin/env python
# _*_coding:utf-8 _*_


class MyChat:
    def __init__(self, contact_obj, set_time, contact_name, message):
        self._contact_obj = contact_obj
        self._set_time = set_time
        self._contact_name = contact_name
        self._message = message
        self._is_send_done = 0

    def get_set_time(self):
        return self._set_time

    def send(self):
        print("###联系人:  '{0}'  的信息:   '{1}'  已经发送 ###".format(self._contact_name, self._message))
        self._contact_obj.send(self._message)
        self._is_send_done = 1
