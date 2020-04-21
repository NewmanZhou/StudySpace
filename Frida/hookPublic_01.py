# -*- coding: utf-8 -*-
# @Time   : 2020/4/20 8:33 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: hookPublic_01.py
# @Software: PyCharm
import codecs

import frida, sys

def message(message, data):
    if message["type"] == 'send':
        print("[on_message] message:", message['payload'], "data:", data)
    elif message['type'] == 'error':
        print("[on_message] message:", message['stack'], "data:", data)
    else:
        print(message)

with codecs.open('fridahook.js','r', 'utf-8') as f:
    jscode = f.read()

process = frida.get_remote_device().attach('com.example.newmanzhou.newman')
script = process.create_script(jscode)
script.on("message", message)
script.load()
sys.stdin.read()
