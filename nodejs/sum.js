function add(a, b) {
    return a + b;
}

// 通过module.exports 对外公开的方法才可以访问
module.exports = {
    add
}