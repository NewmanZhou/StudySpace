function crc32(video_id) {
  var n = function() {
      for (var t = 0,
             e = new Array(256), n = 0; 256 != n; ++n) t = n,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        t = 1 & t ? -306674912 ^ t >>> 1 : t >>> 1,
        e[n] = t;
      return "undefined" != typeof Int32Array ? new Int32Array(e) : e
    } (),
    o = function(t) {
      for (var e, o, r = -1,
             i = 0,
             a = t.length; i < a;) e = t.charCodeAt(i++),
        e < 128 ? r = r >>> 8 ^ n[255 & (r ^ e)] : e < 2048 ? (r = r >>> 8 ^ n[255 & (r ^ (192 | e >> 6 & 31))], r = r >>> 8 ^ n[255 & (r ^ (128 | 63 & e))]) : e >= 55296 && e < 57344 ? (e = (1023 & e) + 64, o = 1023 & t.charCodeAt(i++), r = r >>> 8 ^ n[255 & (r ^ (240 | e >> 8 & 7))], r = r >>> 8 ^ n[255 & (r ^ (128 | e >> 2 & 63))], r = r >>> 8 ^ n[255 & (r ^ (128 | o >> 6 & 15 | (3 & e) << 4))], r = r >>> 8 ^ n[255 & (r ^ (128 | 63 & o))]) : (r = r >>> 8 ^ n[255 & (r ^ (224 | e >> 12 & 15))], r = r >>> 8 ^ n[255 & (r ^ (128 | e >> 6 & 63))], r = r >>> 8 ^ n[255 & (r ^ (128 | 63 & e))]);
      return r ^ -1
    },
    r = "/video/urls/v/1/toutiao/mp4/"+video_id + "?r=" + Math.random().toString(10).substring(2);
  "/" != r[0] && (r = "/" + r);
  var i = o(r) >>> 0;
  return ("https://ib.365yg.com"+r + "&s=" + i)
}
var url = crc32("v03004d00000bumk4u9k832e1p2fvh40");
console.log(url)


//https://ib.365yg.com/video/urls/v/1/toutiao/mp4/v03004d00000bumk4u9k832e1p2fvh40?r=8420980238022997&s=3947996439 ==> main_url base64解码
//http://v9-default.ixigua.com/ac5d19b82d615e8c6463820eb57a7945/5fae31fa/video/tos/cn/tos-cn-ve-4/c3252685ecd94eaebc0f168af72c785f/?a=2012&br=951&bt=317&cr=0&cs=0&cv=1&dr=0&ds=1&er=&l=202011131411430102040482261D0064AE&lr=&mime_type=video_mp4&qs=0&rc=M2tpc2g2bnhueDMzMzczM0ApMzg3NWk1aTs0Nzo3aGk8Nmcxcy8uLzU2MWpfLS1hLTBzczNhNDYtLjQxYWBeNjUtY2A6Yw%3D%3D&vl=&vr=
