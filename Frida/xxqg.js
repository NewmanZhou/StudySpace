
// 学习强国 app
// 欢迎页面 com.alibaba.android.rimet.biz.SplashActivity
// function hookTest() {
//     var utils = Java.use('cn.xuexi.android com.alibaba.android.rimet.biz.home.activity');
//     utils.generateRequest.implementation = function (a) {
//         console.log("Hook Start.......");
//         send("Success!");
//         return this.generateRequest(a);
//     }
// }

// package="cn.xuexi.android"
// function hook_xxqg() {
//     Java.perform(function () {
//         Java.enumerateLoadedClasses({
//             onMatch: function (name, handle) {
//                 if (name.indexOf("cn.xuexi.android") != -1) {
//                     // console.log(name)
//                     var clazz = Java.use(name)
//                     console.log(clazz)
//                     var methods = clazz.class.getDeclaredMethods()
//                     for (var i = 0; i < methods.length; i++) {
//                         console.log(methods[i])
//                     }
//
//                 }
//             },
//             onComplete: function () {
//
//             }
//         })
//
//     })
// }

function hook_okgo() {
    Java.perform(function () {
        var CacheCall  = Java.use("cn.trust.okgo.adapter.CacheCall")
        baseRequest = CacheCall.baseRequest
        console.log(JSON.stringify(baseRequest))
    })
}

function main() {
    Java.perform(function () {
        // hookTest();
    });
}

setImmediate(main);