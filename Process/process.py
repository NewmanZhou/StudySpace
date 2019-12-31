#-*- coding:utf-8 -*-

import psutil


def get_process_list(process_name, argvs=[]):
    pro_list = []
    for proc in psutil.process_iter():
        try:
            pinfo = proc.as_dict(attrs=['pid', 'name', 'cmdline'])
        except psutil.NoSuchProcess:
            continue
        if pinfo["name"].find(process_name) < 0:
            continue
        for argv in argvs:
            if argv not in pinfo["cmdline"]:
                break
        pro_list.append(proc)
    print(pro_list)
    return pro_list


if __name__ == "__main__":
    for value in get_process_list("scheduler_app", [0]):
        print(value)

