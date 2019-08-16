#!/usr/bin/python
# -*- coding: utf-8 -*-
# @Time    : 2019-08-16 20:48
# @Author  : YuSwift
# @File    : main
# @Software: PyCharm

import yaml
import requests


class AutoBeijingEntry(object):
    def __init__(self):
        self.config_map = yaml.load(open("./config.yaml"), Loader=yaml.FullLoader)

    def get_beijing_entry_list(self):
        list_data = self.config_map["GetBeijingEntryList"]
        url = list_data["url"]
        headers = list_data["headers"]
        cookies = list_data["cookie"]

        data = ""
        for d in list_data["data"]:
            for k, v in d.items():
                param = str(k) + "=" + str(v) + "&"
                data += param

        return requests.post(url=url, headers=headers, cookies=cookies, data=data).json()

    def post_beijing_entry(self):
        entry = self.config_map["PostBeijingEntry"]
        url = entry["url"]
        headers = entry["headers"]
        cookies = entry["cookie"]

        data = ""
        for d in entry["data"]:
            for k, v in d.items():
                param = str(k) + "=" + str(v) + "&"
                data += param

        return requests.post(url=url, headers=headers, cookies=cookies, data=data)

if __name__ == "__main__":
    print(AutoBeijingEntry().get_beijing_entry_list())

