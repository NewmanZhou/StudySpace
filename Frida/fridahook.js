// Frida 入门， 来自B站视频资源小肩膀14节课 AppDemo自行编写
// Hook 静态方法、对象类、重写方法的加载、对象创建以及参数的更改
Java.perform(function () {
    var utils = Java.use('com.example.newmanzhou.newman.Utils');
    utils.getCalc.implementation = function (a, b) {
        console.log("Hook Start.......");
        send("Success!");
        return this.getCalc(10, 10);
    }
    var money = Java.use('com.example.newmanzhou.newman.Money');
    //money.$init.overload("int","java.lang.String").implementation = function(a, b){
    //    send("Success!")
    //    return this.$init(1000, "美元")
    //}

    utils.test.overload('com.example.newmanzhou.newman.Money').implementation = function (obj) {
        console.log("Hook Start.......");
        send("Success!");
        send(obj.num.value);
        var mon = money.$new(1000, "港币");
        mon.num.value = 400;
        //send(mon.getInfo());
        return this.test(mon);
    }
});