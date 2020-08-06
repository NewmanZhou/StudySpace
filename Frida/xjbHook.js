
//Hook普通函数
function hookTest1(){
    var utils = Java.use("com.xiaojianbang.app.Utils");
    utils.getCalc.implementation = function(a, b){
        a = 123;
        b = 456;
        var retval = this.getCalc(a, b);
        console.log(a, b, retval);
        return retval;
    }
}
// .overload()
// .overload('com.xiaojianbang.app.Money')
// .overload('int')
//Hook重载函数
function hookTest2(){
    var utils = Java.use("com.xiaojianbang.app.Utils");
    var money = Java.use("com.xiaojianbang.app.Money");
    utils.test.overload('int').implementation = function(a){
        a = 888;
        var retval = this.test(money.$new("日元", 100000));//对象实例化
        console.log(a, retval);
        return retval;
    }
    utils.test.overload().implementation = function(){
        var retval = this.test();
        console.log(retval);
        return retval;
    }
    utils.test.overload('com.xiaojianbang.app.Money').implementation = function(a){
        var retval = this.test(a);
        console.log(retval);
        return retval;
    }
}
//Hook方法的所有重载
function hookTest3(){
    var utils = Java.use("com.xiaojianbang.app.Utils");
    //console.log(utils.test.overloads.length);
    for(var i = 0; i < utils.test.overloads.length; i++){
        utils.test.overloads[i].implementation = function(){
            //console.log(JSON.stringify(arguments));

            if(arguments.length == 0){
                return "调用了没有参数的";
            }else if(arguments.length == 1){
                if(JSON.stringify(arguments).indexOf("Money") != -1){
                    return "调用了Money参数的";
                }else{
                    return "调用了int参数的";
                }
            }

            //arguments[0] = 1000;
            //return this.test.apply(this, arguments);
        }
    }
}
//Hook构造函数
function hookTest4(){
    var money = Java.use("com.xiaojianbang.app.Money");
    money.$init.overload('java.lang.String', 'int').implementation = function(str, num){
        console.log(str, num);
        str = "欧元";
        num = 2000;
        this.$init(str, num);
    }
}
//修改类的字段
function hookTest5(){
    Java.perform(function(){
        //静态字段的修改
        var money = Java.use("com.xiaojianbang.app.Money");
        //console.log(JSON.stringify(money.flag));
        money.flag.value = "xiaojianbang";
        console.log(money.flag.value);

        //非静态字段的修改
        Java.choose("com.xiaojianbang.app.Money", {
            onMatch: function(obj){
                obj._name.value = "ouyuan"; //字段名与函数名相同 前面加个下划线
                obj.num.value = 150000;
            },
            onComplete: function(){

            }
        });
    });
}
//Hook内部类与匿名类
function hookTest6(){
    Java.perform(function(){
        var innerClass = Java.use("com.xiaojianbang.app.Money$innerClass");
        console.log(innerClass);
        innerClass.$init.implementation = function(a, b){
            a = "xiaojianbang";
            b = 888;
            return this.$init(a, b);
        }

        var xxx = Java.use("com.xiaojianbang.app.MainActivity$1");
        console.log(xxx);
        xxx.getInfo.implementation = function(){
            return "匿名类被Hook了"
        }


    });

}
//枚举已加载的所有类与枚举类的所有方法
function hookTest7(){
    Java.perform(function(){
        // Java.enumerateLoadedClasses({
        //     onMatch: function(name, handle){
        //         if(name.indexOf("com.xiaojianbang.app") != -1){
        //             console.log(name);
        //             var clazz = Java.use(name);
        //             console.log(clazz);
        //             var methods = clazz.class.getDeclaredMethods();

        //             for(var i = 0; i < methods.length; i++){
        //                 console.log(methods[i]);
        //             }

        //         }

        //     },
        //     onComplete: function(){

        //     }
        // });

        var classes = Java.enumerateLoadedClassesSync();
        for(var i = 0; i < classes.length; i++){
            if(classes[i].indexOf("com.xiaojianbang.app") != -1){
                console.log(classes[i]);
                var clazz = Java.use(classes[i]);
                var methods = clazz.class.getDeclaredMethods();
                for(var j = 0; j < methods.length; j++){
                    console.log(methods[j]);
                }
            }
        }
    });
}
//Hook类的所有方法
function hookTest8(){
    Java.perform(function(){
        var md5 = Java.use("com.xiaojianbang.app.MD5");
        var methods = md5.class.getDeclaredMethods();
        for(var j = 0; j < methods.length; j++){
            var methodName = methods[j].getName();
            console.log(methodName);

            for(var k = 0; k < md5[methodName].overloads.length; k++){

                md5[methodName].overloads[k].implementation = function(){
                    for(var i = 0; i < arguments.length; i++){
                        console.log(arguments[i]);
                    }
                    return this[methodName].apply(this, arguments);
                }
            }

        }

    });
}
//Hook动态加载的dex
function hookTest9(){
    Java.perform(function(){

        Java.enumerateClassLoaders({
            onMatch: function(loader){
                try {
                    if(loader.loadClass("com.xiaojianbang.app.Dynamic")){
                        Java.classFactory.loader = loader;
                        var Dynamic = Java.use("com.xiaojianbang.app.Dynamic");
                        console.log(Dynamic);
                        Dynamic.sayHello.implementation = function(){
                            return "xiaojianbang";
                        }
                    }
                } catch (error) {

                }
            }
            ,
            onComplete: function(){

            }
        });
    });
}
//java map类型的遍历与修改
function hookTest10(){
    Java.perform(function(){
        var ShufferMap = Java.use("com.xiaojianbang.app.ShufferMap");
        console.log(ShufferMap);
        ShufferMap.show.implementation = function(map){
            console.log(JSON.stringify(map));
            //Java map的遍历
            // var key = map.keySet();
            // var it = key.iterator();
            // var result = "";
            // while(it.hasNext()){
            //     var keystr = it.next();
            //     var valuestr = map.get(keystr);
            //     result += valuestr;
            // }
            // console.log(result);
            // return result;

            map.put("pass", "zygx8");
            map.put("guanwang", "www.zygx8.com");

            var retval = this.show(map);
            console.log(retval);
            return retval;

        }
    });
}

function hookTest11(){
    Java.perform(function(){
        //静态方法的主动调用
        var rsa = Java.use("com.xiaojianbang.app.RSA");
        var str = Java.use("java.lang.String");
        var base64 = Java.use("android.util.Base64");
        var bytes = str.$new("xiaojianbang").getBytes();
        console.log(JSON.stringify(bytes));
        var retval = rsa.encrypt(bytes);
        var result = base64.encodeToString(retval, 0);
        console.log(result);
        //非静态方法的主动调用1 (新建一个对象去调用)
        var res = Java.use("com.xiaojianbang.app.Money").$new("日元", 300000).getInfo();
        console.log(res);
        var utils = Java.use("com.xiaojianbang.app.Utils");
        res = utils.$new().myPrint(["xiaojianbang","is very good"," ","zygx8","is very good"]);
        console.log(res);
        //非静态方法的主动调用2 (获取已有的对象调用)
        Java.choose("com.xiaojianbang.app.Money",{
            onMatch: function(obj){
                if(obj._name.value == "美元"){
                    res = obj.getInfo();
                    console.log(res);
                }
            },
            onComplete: function(){

            }
        });

    });
}

function main(){
    Java.perform(function(){
        //hookTest1();
        //hookTest2();
        //hookTest3();
        //hookTest4();
        hookTest11();

    });
}

setImmediate(main);