// setImmediate(function () {
//     Java.perform(function () {
//         var utils = Java.use("com.xiaojianbang.app.Utils")
//         utils.getCalc.implementation = function (a, b) {
//             a = 123;
//             b = 456;
//             var retval = this.getCalc(a, b)
//             console.log(a, b, retval)
//
//             return retval
//         }
//     });
// });

// hook 普通方法
function hookTest_01() {
    var utils = Java.use("com.xiaojianbang.app.Utils")
    utils.getCalc.implementation = function (a, b) {
        a = 123;
        b = 456;
        var retval = this.getCalc(a, b);
        console.log(a, b, retval);

        return retval
    }
}

// hook 重载方法
//.overload()
//.overload('int')
//.overload('com.xiaojianbang.app.Money')
function hookTest_02() {
    var utils = Java.use("com.xiaojianbang.app.Utils")
    var money = Java.use("com.xiaojianbang.app.Money")
    utils.test.overload().implementation = function () {
        var retval = this.test();
        console.log(retval)
        return retval
    }


    utils.test.overload('int').implementation = function (a) {
        var retval = this.test(money.$new("日元", 66));
        console.log(retval);
        return retval;
    }

    utils.test.overload("com.xiaojianbang.app.Money").implementation = function (a) {
        var retval = this.test(a);
        console.log(retval);
        return retval;
    }
}

// hook 方法的所有重载
function hookTest_03() {
    var utils = Java.use("com.xiaojianbang.app.Utils")
    var len = utils.test.overloads.length;
    // console.log(len)
//    遍历所有重载方法
    for (var i = 0; i < len; i++) {
        utils.test.overloads[i].implementation = function () {
            if (arguments.length == 0) {
                return "调用了没有参数的"
            } else {
                if (JSON.stringify(arguments).indexOf("Money") != -1) {
                    return "调用了Money有参数的"
                } else {
                    return "调用了int有参数的"
                }
            }
            // console.log(arguments.length);
            // return this.test.apply(this,arguments);
        }
    }
}

function hookTest_04() {
    var money = Java.use("com.xiaojianbang.app.Money")
    money.$init.overload("java.lang.String", 'int').implementation = function (str, num) {
        console.log(str, num)
        this.$init("美刀", 999)
    }
    money.name.implementation = function () {
        return "NewmanZhou"
    }
}


//hook 类静态字段的修改 private static String flag = "zygx8"
function hookTest_05() {
    var money = Java.use("com.xiaojianbang.app.Money")
    // console.log(JSON.stringify(money.flag));
    // send(money.flag.value);
    money.flag.value = "Newman"
    console.log(money.flag.value);

    // 非静态字段的修改
    Java.choose("com.xiaojianbang.app.Money", {
        onMatch: function (obj) {
            obj._name.value = "欧元"
            obj.num.value = 1234
        },
        onComplete: function () {

        }
    });
}

// hook 内部类
function hookTest_06() {
    var innerClass = Java.use("com.xiaojianbang.app.Money$innerClass")
    innerClass.$init.implementation = function (a, b) {
        a = "自己";
        b = 4321
        return this.$init(a, b)
    }

    // 匿名内部类
    var noNameClass = Java.use("com.xiaojianbang.app.MainActivity$1")
    noNameClass.getInfo.implementation = function () {
        return "Newman hook 匿名内部类";
    }

}

// hook 已经加载的所有的类，以及类的方法
function hookTest_07() {
    Java.perform(function () {
        // 枚举所有已经加载的类，类函数
        Java.enumerateLoadedClasses({
            onMatch: function (name, handle) {
                if (name.indexOf("com.xiaojianbang.app") != -1) {
                    // console.log(name)
                    var clazz = Java.use(name)
                    console.log(clazz)
                    var methods = clazz.class.getDeclaredMethods()
                    for (var i = 0; i < methods.length; i++) {
                        console.log(methods[i])
                    }

                }
            },
            onComplete: function () {

            }
        })

        // 枚举所有的类，及类函数
        // var classes = Java.enumerateLoadedClassesSync();
        // for (var i = 0; i < classes.length; i++) {
        //     if (classes[i].indexOf("com.xiaojianbang.app") != -1) {
        //         console.log(classes[i])
        //         var clazz = Java.use(classes[i])
        //         console.log(clazz)
        //         var methods = clazz.class.getDeclaredMethods()
        //         for (var j = 0; j < methods.length; j++) {
        //             console.log(methods[j])
        //         }
        //
        //     }
        // }
    })
}

// hook 类的所有方法
function hookTest_08() {
    Java.perform(function () {
        var md5 = Java.use("com.xiaojianbang.app.MD5")
        var methods = md5.class.getDeclaredMethods()
        for (var i = 0; i < methods.length; i++) {
            var methodName = methods[i].getName();
            console.log(methodName)

            // hook 类重载函数
            for (var k = 0; k < md5[methodName].overloads.length; k++) {
                md5[methodName].overloads[k].implementation = function () {
                    for (var j = 0; j < arguments.length; j++) {
                        console.log(arguments[i]);
                    }
                    return this[methodName].apply(this, arguments)
                }
            }
        }
    });
}

// hook 动态加载的 Dex
// 对手机 系统版本有要求。
function hookTest_09() {
    Java.perform(function () {
        Java.enumerateClassLoaders({
            onMatch: function (ld) {
                try {
                    if (ld.loadClass("com.xiaojianbang.app.Dynamic")) {
                        Java.classFactory.loader = ld;
                        var Dynamic = Java.use("com.xiaojianbang.app.Dynamic")
                        Dynamic.sayHello.implementation = function () {
                            return "NewmanHook 动态Dex";
                        }
                        console.log(Dynamic)
                    }

                } catch (e) {
                    console.log(e);
                }

            },
            onComplete: function () {

            }
        });
        // var Dynamic = Java.use("com.xiaojianbang.app.Dynamic")
        // console.log(Dynamic)
    });
}

// 遍历 HashMap
function hookTest_10() {
    Java.perform(function () {
        var ShufferMap = Java.use("com.xiaojianbang.app.ShufferMap");
        console.log(ShufferMap);
        ShufferMap.show.implementation = function (map) {
            console.log('测试数据');
            console.log(JSON.stringify(map));
            console.log({}.toString.call(map));
            // console.log(map.user);
            //Java map的遍历
            var key = map.keySet();
            var it = key.iterator();
            var result = "";
            while (it.hasNext()) {
                var keystr = it.next();
                var valuestr = map.get(keystr);
                result += valuestr;
            }
            console.log(result);
            return result;

            map.put("pass", "zygx8");
            map.put("guanwang", "www.zygx8.com");

            var retval = this.show(map);
            console.log(retval);
            return retval;

        }
    });
}

// Java 层的主动调用
function hookTest_11() {
    Java.perform(function () {
        // 静态方法的主要调用 (创建一个对象去调用)
        var rsa = Java.use("com.xiaojianbang.app.RSA")
        var java_class = Java.use("java.lang.String")
        var base_64 = Java.use("android.util.Base64")
        var bytes = java_class.$new("ceshiyixia").getBytes();
        var res = rsa.encrypt(bytes)
        var result = base_64.encodeToString(res, 0)
        console.log(result)

        // 非静态方法的主动调用 方式一
        var money = Java.use("com.xiaojianbang.app.Money")
        var getinfo = money.$new("欧元", 9981).getInfo()
        console.log(getinfo)

        var utils = Java.use("com.xiaojianbang.app.Utils")
        var str_res = utils.$new().myPrint(["测试", "输出", ":", "没问题啊！"])
        console.log(str_res)

        // 非静态方法的主动调用 方式二 （调用已经存在的对象）
        // 已经加载的类，对其非静态方法进行调用
        Java.choose("com.xiaojianbang.app.Money", {
            onMatch: function (obj) {
                if (obj._name.value == "欧元") {
                    var str_res = obj.getInfo()
                    console.log(str_res)
                }
            },
            onComplete: function () {

            }
        })
    });
}

// hook 函数的堆栈
function hookTest_12() {
    // .overload()
    // .overload('[B')
    // .overload('[B', 'int', 'int')
    function showStacks(){

        //var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Exception").$new());
        var stack = Java.use("android.util.Log").getStackTraceString(Java.use("java.lang.Throwable").$new());
        console.log(stack);

    }
    Java.perform(function(){
        //Java.cast() 强制类型转换
        //Java.openClassFile();
        //Java.registerClass
        //Java.array() 构造任意类型的数组
        showStacks();
        var MessageDigest = Java.use("java.security.MessageDigest");
        MessageDigest.digest.overload().implementation = function(){
            showStacks();
            return this.digest();
        }

    });
}

// 加载自己编写的dex 文件
function hookTest_13() {
    Java.perform(function () {
        Java.openClassFile("/data/local/tmp/xjbclasses.dex").load()
        var xiaojianbang = Java.use("com.xiaojianbang.test.xiaojianbang");

        var ShufferMap = Java.use("com.xiaojianbang.app.ShufferMap");
        ShufferMap.show.implementation = function(map){
            var retval = xiaojianbang.sayHello(map);
            console.log(retval);
            return retval;
        }
    })
}

// 程序启动 hook


function main() {
    Java.perform(function () {
        hookTest_01();
        // hookTest_02();
        // hookTest_03();
        // hookTest_04();
        // hookTest_06()
    });
}

//https://k.sina.cn/aj/mediaarticlelist?media_id=2793823365&show_num=10&page=1
//http://interface.sina.cn/kd/user_articlelist.d.json?uid=2793823365&page=1

setImmediate(main);