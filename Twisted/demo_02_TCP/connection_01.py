import frida, sys


def on_message(message, data):
    if message['type'] == 'send':
       print("[*] {0}".format(message['payload']))
    else:
        print(message)

js_code = '''
       Java.perform(function(){
       var hook_Activity = 
       Java.use('jianshu.foundation.util.q');  hook_Activity.a.overload("java.lang.String").imple
       mentation = function(arg1){
       var return1 = this.a(arg1);
       send("arg1:"+ arg1);
       send("result:" + return1)
       return return1;
   }
     });
    ''' 
session = frida.get_usb_device().attach("com.jianshu.haruki")
script = session.create_script(js_code)
script.on('message', on_message)
script.load()
sys.stdin.read()