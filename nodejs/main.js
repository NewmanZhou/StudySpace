// 引入依赖包

var express = require('express')
var bodyParser = require('body-parser')

// 引入自定义的JS文件
var sum = require('./sum')

// 创建应用实例
var app = express()

// 判断请求体格式是不是表单格式，如果是的话会调用js库把请求体字符串转成对象
app.use(bodyParser.urlencoded({ extended: true }));

// 判断请求体格式是不是json, 如果是的话会调用JSON.parse方法
app.use(bodyParser.json())

// 创建路由
app.post('/get_num', function (req, res) {
    // 获取请求路径中传递的查询参数
    let result = req.body
    console.log("result", result)
    // 将客户端传递过来的属性 强制转换成整数类型
    let a = parseInt(result.a)
    let b = parseInt(result.b)
    result = sum.add(a, b)
    res.send(result.toString());    // 将结果返回，只支持字符串类型或者json格式。
})

app.listen(3000, () => {
    console.log("开启服务，端口3000")
})