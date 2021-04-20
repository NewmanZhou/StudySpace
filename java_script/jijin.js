
function i(e) {
    var t = this.list.find(function (t) {
        return t.fundName.trim() === e.slice(7).trim()
    }).fundCode.toString()
        , a = Object(c.b)(this.key, this.iv, t);
    this.tipFlag = !1,
        window.open("fundDetails.html?id=" + a)

    a = r.Latin1 = {
        stringify: function (e) {
            for (var t = e.words, n = e.sigBytes, i = [], r = 0; r < n; r++) {
                var o = t[r >>> 2] >>> 24 - r % 4 * 8 & 255;
                i.push(String.fromCharCode(o))
            }
            return i.join("")
        },
        parse: function (e) {
            for (var t = e.length, n = [], i = 0; i < t; i++)
                n[i >>> 2] |= (255 & e.charCodeAt(i)) << 24 - i % 4 * 8;
            return new d.init(n, t)
        }
    }
}


console.log(i("华夏成长"))