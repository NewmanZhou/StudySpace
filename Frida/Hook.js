//采用 frida -U 包名 Hook.js  直接js注入的方式

function hookTest() {
    // var utils = Java.use('com.example.newmanzhou.newman.Money');
    // utils.getCalc.implementation = function (a, b) {
    //     a = 12;
    //     b = 20;
    //     var retval = this.getCalc(a, b);
    //     return retval
    // }
    var utils = Java.use('com.example.newmanzhou.newman.Utils');
    utils.getCalc.implementation = function (a, b) {
        console.log("Hook Start.......");
        send("Success!");
        return this.getCalc(0, 10);
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
        mon.num.value = 900;
        //send(mon.getInfo());
        return this.test(mon);
    }
}


function main() {
    Java.perform(function () {
        hookTest()
    });
}

setImmediate(main);