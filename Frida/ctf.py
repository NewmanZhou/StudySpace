# -*- coding: utf-8 -*-
# @Time   : 2020/5/8 4:38 下午
# @Author : NewmanZhou
# @Desc : ==============================================
# Life is Short I Use Python!!!                      ===
# If this runs wrong,don't ask me,I don't know why;  ===
# If this runs right,thank god,and I don't know why. ===
# Maybe the answer,my friend,is blowing in the wind. ===
# ======================================================
# @Project : StudySpace
# @FileName: ctf.py.py
# @Software: PyCharm
import frida, sys

def on_message(message, data):
    if message['type'] == 'send':
        print("[*] {0}".format(message['payload']))
    else:
        print(message)

jscode = """
Java.perform(function () {
  // Function to hook is defined here
  var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');
    
   # //hook该类下的onCreate方法，重新实现它
   #  MainActivity.onCreate.implementation = function () {
   #      send("Hook Start...");
   #      //调用calc()方法，获取返回值
   #      var returnValue = this.calc();
   #      send("Return:"+returnValue);
   #      var result = (1000+returnValue)*107;
   #      //解出答案
   #      send("Flag:"+"SECCON{"+result.toString()+"}");
   #  }

  // Whenever button is clicked
  var onClick = MainActivity.onClick;
  onClick.implementation = function (v) {
    // Show a message to know that the function got called
    send('onClick');

    // Call the original onClick handler
    onClick.call(this, v);

    // Set our values after running the original onClick handler
    this.m.value = 0;
    this.n.value = 1;
    this.cnt.value = 999;

    // Log to the console that it's done, and we should have the flag!
    console.log('Done:' + JSON.stringify(this.cnt));
  };
});
"""

process = frida.get_usb_device().attach('com.example.seccon2015.rock_paper_scissors')
script = process.create_script(jscode)
script.on('message', on_message)
print('[*] Running CTF')
script.load()
sys.stdin.read()