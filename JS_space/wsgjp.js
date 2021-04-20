var noticeCount = 0;
var noticeTemp = 0;
var noticeArray;
var noticeNoTip = "";
var errorCount = 0;
var currentProductid = 0;
var currentCompanyName = "";
var currentUserName = "";
var hostList = new Array("wsgjp.com.cn", "wsgjp.com", "mygjp.com");


var eye = 0;

function getBrowser() {
    var Browser = {};

    if (navigator.userAgent.indexOf(' MSIE ') > -1 || navigator.userAgent.indexOf('Trident/') > -1) {
        Browser.agent = Browser.InternetExplorer;
        Browser.isIE = true;

        var str = null;
        try {
            var win = window;
            for (var i = 0; i < 4; i++) {
                var str = win.__CarpaBrowser_IEVersion;
                if (str) break;
                win = win.parent;
                if (!win) break;
            }
        } catch (e) {
        } // 不知为何在IFrame中有的机器要出错

        var version = 0;
        if (str) {
            version = parseInt(str);
        } else if (navigator.userAgent.indexOf(' MSIE ') > -1) {
            version = parseFloat(navigator.userAgent.match(/MSIE\s(\d+\.\d+)/)[1]);
        } else {
            version = parseFloat(navigator.userAgent.match(/rv:(\d+\.\d+)/)[1]);
        }

        Browser.version = version;

        if (version >= 8) {
            Browser.isIE8 = true;
            if (version >= 9) {
                Browser.isIE9 = true;
            }
            Browser.isIE10 = version == 10;
            Browser.isIE11 = version == 11;
        } else if (version >= 7) {
            Browser.isIE7 = true;
        } else if (version >= 6) {
            Browser.isIE6 = true;
        }

        Browser.isStandard = Browser.isIE8;

        // remove css image flicker 抄自 Ext.js
        if (version < 7) {
            try {
                document.execCommand("BackgroundImageCache", false, true);
            } catch (e) {
            }
        }

        Browser.hasDebuggerStatement = true;
        Browser.name = "IE";
    } else if (navigator.userAgent.indexOf(' Firefox/') > -1) {
        Browser.agent = Browser.Firefox;
        Browser.isFirefox = true;
        Browser.version = parseFloat(navigator.userAgent.match(/\sFirefox\/(\d+\.\d+)/)[1]);
        Browser.name = 'Firefox';
        Browser.hasDebuggerStatement = true;
        Browser.charset = document.characterSet; // 特殊
    } else if (navigator.userAgent.indexOf(' AppleWebKit/') > -1) {
        Browser.agent = Browser.Safari;
        Browser.isSafari = true;
        Browser.isChrome = navigator.userAgent.indexOf(' Chrome/') > -1;
        if (Browser.isChrome) {
            Browser.name = 'Chrome';
            Browser.version = parseFloat(navigator.userAgent.match(/\sChrome\/(\d+(\.\d+)?)/)[1]);
        } else {
            Browser.name = 'Safari';
            Browser.version = parseFloat(navigator.userAgent.match(/\sAppleWebKit\/(\d+(\.\d+)?)/)[1]);
        }
        if (navigator.userAgent.indexOf(' Edge/') > -1) {
            Browser.isEdge = true;
        }
    } else if (navigator.userAgent.indexOf('Opera/') > -1) {
        Browser.agent = Browser.Opera;
        Browser.isOpera = true;
        Browser.name = "Opera";
    }
    return Browser;
}

function getCookie(cookie_name) {
    var allcookies = document.cookie;
    var cookie_pos = allcookies.indexOf(cookie_name);
    if (cookie_pos != -1) {
        cookie_pos = cookie_pos + cookie_name.length + 1;
        var cookie_end = allcookies.indexOf(";", cookie_pos);
        if (cookie_end == -1) {
            cookie_end = allcookies.length;
        }
        var value = unescape(allcookies.substring(cookie_pos, cookie_end));
    }
    return value;
};

function postLogin(isShowNotice, callback) {
    var productid = $('#product').val();
    var companyname = $('#company').val();
    var username = $('#username').val();
    var ref = window.location.href;
    var clientinfo = $('#hfclientinfo').val();

    var loginUrl = "/erp/login";

    if (productid == 19 || productid == 26) {
        loginUrl = "/zyx/login"
    }
    setMaxDigits(129);
    var key = new RSAKeyPair();
    var data = JSON.stringify({
        productId: productid,
        companyName: companyname,
        userName: encryptedString(key, encodeURIComponent(username)),
        password: encryptedString(key, $('#password').val()),
        rememberMe: $('#cb_RemenberMe').is(':checked'),
        https: getHttps(),
        showNotice: isShowNotice,
        validateId: getCookie("Vnumber"),
        validateCode: $('#txt_ValidateNumber').val(),
        ref: ref,
        clientinfo: clientinfo,
        ati: getCookie("_ati"),
        deviceId: getCookie("deviceId"),
        host: getHost()
    });
    window.sessionStorage.setItem("data", data);
    $.ajax({
        url: loginUrl,
        type: 'POST',
        data: data,
        contentType: "application/json",
        dataType: 'json',
        success: callback,
        error: function () {
            alert("登录失败,请稍后重试");
            $("#btnlogin").val("立即登录");
            $("#btnlogin").removeAttr("disabled");
        }
    });
};

function postFenxiaoLogin(isShowNotice, callback) {
    var companyname = $('#txt_buy').val();
    var supplier = $('#hfSupplier').val();
    setMaxDigits(129);
    var key = new RSAKeyPair();
    var data = JSON.stringify({
        productId: "15",
        companyName: companyname,
        supplierName: encryptedString(key, encodeURIComponent(supplier)),
        password: encryptedString(key, $('#password').val()),
        rememberMe: $('#cb_RemenberMe').is(':checked'),
        https: getHttps(),
        showNotice: isShowNotice
    });
    window.sessionStorage.setItem("data", data);
    $.ajax({
        url: "/c3/login",
        type: 'POST',
        data: data,
        contentType: "application/json",
        dataType: 'json',
        success: callback,
        error: function () {
            alert("登录失败,请稍后重试");
            $("#btnlogin").val("立即登录");
            $("#btnlogin").removeAttr("disabled");
        }
    });
}

function getErrorCount(productid, companyname, username) {
    if (!productid || !companyname || !username) {
        errorCount = 0;
        return;
    }
    setMaxDigits(129);
    var key = new RSAKeyPair();
    $.ajax({
        type: "POST",
        url: "/errorcount/get",
        contentType: "application/json",
        dataType: "json",
        data: JSON.stringify({
            productId: productid,
            companyName: companyname,
            userName: encryptedString(key, encodeURIComponent(username))
        }),
        async: false,
        success: function (result) {
            if (result) {
                if (result.code == "200") {
                    errorCount = result.data;
                    if (!errorCount) {
                        errorCount = 0;
                    }
                }
            }
        }
    });
}

function SwitchYzm() {
    var companyname = $("#company").val();
    var username = $("#username").val();
    var productid = $('#product').val();
    if ($("#tb2").attr("class") == "selected") {
        companyname = $("#txt_buy").val();
        username = $('#hfSupplier').val();
        productid = 15;
    }

    if (!companyname || !username) {
        return;
    }
    if (companyname != currentCompanyName || username != currentUserName || productid != currentProductid) {
        currentCompanyName = companyname;
        currentUserName = username;
        currentProductid = productid;
        getErrorCount(productid, companyname, username);
    }
    if (errorCount >= 3) {
        if ($('#yzmimg').is(':hidden')) {
            $('#yzmimg').click();
        }
        $("#tr_yzm").show();
    } else {
        $("#tr_yzm").hide();
    }
};

function continueLogin(data) {
    var isFenxiao = $("#tb2").attr("class") == "selected";
    if (noticeNoTip.length > 0) {
        var postData;
        if (isFenxiao) {
            postData = JSON.stringify({
                companyName: $('#txt_buy').val(),
                userName: $("#hfSupplier").val(),
                noticeHide: noticeNoTip,
                productId: 15
            });
        } else {
            postData = JSON.stringify({
                companyName: $('#company').val(),
                userName: $('#username').val(),
                noticeHide: noticeNoTip,
                productId: $('#product').val()
            });
        }
        $.ajax({
            url: "/notice/hide",
            type: 'POST',
            data: postData,
            async: false,
            contentType: "application/json",
            dataType: 'json',
            success: function (res) {
                if (res) {

                }
            }
        });
    }
    if (data != null && data.needSecondaryVerification != null && data.needSecondaryVerification) {
        window.sessionStorage.setItem("phone", data.phone);
        window.open(data.secondaryVerificationUrl, "_self");
        return;
    }
    if (!data) {
        var callback = function (res) {
            if (res) {
                if (res.code != "200") {
                    errorCount++;
                    if (res.message) {
                        alert(res.message);
                    } else {
                        alert("登录失败!")
                    }
                    $("#btnlogin").val("立即登录");
                    $("#btnlogin").removeAttr("disabled");
                    SwitchYzm();
                    return;
                }
                errorCount = 0;
                data = res.data;
                if (data) {
                    continueLogin(data);
                }
            }
        };
        if (isFenxiao) {
            postFenxiaoLogin(false, callback)
        } else {
            postLogin(false, callback);
        }
        return;
    }
    if ($('#cb_safelogin').is(':checked')) {
        data.loginUrl = data.loginUrl.replace("http:", "https:");
        if (data.loginUrl.indexOf("mygjp.com") > -1) {
            data.loginUrl.replace("mygjp.com", "wsgjp.com");
        }
    }

    if (data.post) {
        var browser = getBrowser();
        if (browser.isSafari && !browser.isChrome) {
            var fromDiv = '<div><form id="redirectForm" action="' + data.loginUrl + '" target="_top" name="redirectForm" method="post">';
            for (var key in data.arguments) {
                var input = '<input type="hidden" name="' + key + '" value="' + data.arguments[key] + '">';
                fromDiv += input;
            }
            fromDiv += '</form></div>';
            copyNodes(document.getElementById("formDiv"), parseToDOM(fromDiv));
            var form = $('#redirectForm');
            form.submit();
        } else {
            var formhtml = '<form id="redirectForm" action="' + data.loginUrl + '" target="_top" name="redirectForm" method="post"></form>';
            $('body').append(formhtml);
            var form = $('#redirectForm');
            for (var key in data.arguments) {
                var input = '<input type="hidden" name="' + key + '" value="' + data.arguments[key] + '">';
                form.append(input);
            }
            form.submit();
        }
    } else {
        var queryString = "";
        for (var key in data.arguments) {
            if (queryString != "") {
                queryString += "&";
            }
            queryString += key + "=" + data.arguments[key];
        }
        if (queryString) {
            if (data.loginUrl.indexOf('?') > 0) {
                top.location.href = data.loginUrl += "&" + queryString;
            } else {
                top.location.href = data.loginUrl += "?" + queryString;
            }
        } else {
            top.location.href = data.loginUrl;
        }
    }
}

function getHost() {
    if ($("#hfIsProxy").val() == "true") {
        return "wsgjp.com.cn";
    }
    var url = getUrl();
    var host = "wsgjp.com.cn";
    if (!url) {
        return host;
    }
    for (var i = 0; i < hostList.length; i++) {
        var value = hostList[i];
        if (url.indexOf(value) > -1) {
            host = value;
            break;
        }
    }
    return host;
}

function getHttps() {
    // var url = getUrl();
    // if (url.indexOf("https://") > -1 && url.indexOf("mygjp.com") < 0) {
    //     return true;
    // }
    // return false;
    if ($('#cb_safelogin').is(':checked')) {
        return true;
    } else {
        return false;
    }
}

function getUrl() {
    var url = "";
    try {
        url = top.location.href;
    } catch (e) {
        try {
            url = document.referrer;
        } catch (e) {
            url = document.location.href;
        }
    }
    return url;
}

function copyNodes(nodeTo, nodeFrom) {
    if (!nodeTo || !nodeFrom)
        return;

    var ownerDoc = (nodeTo.nodeType == Node.DOCUMENT_NODE ? nodeTo : nodeTo.ownerDocument);
    var nodes = nodeFrom.childNodes;
    // if (ownerDoc.importNode) {
    for (var i = 0; i < nodes.length; i++) {
        nodeTo.appendChild(ownerDoc.importNode(nodes[i], true));
        // }
        // } else {
        //     for (var i = 0; i < nodes.length; i++) {
        //         nodeTo.appendChild(nodes[i].cloneNode(true));
        //     }
    }
}

function parseToDOM(str) {
    var div = document.createElement("div");
    if (typeof str == "string")
        div.innerHTML = str;
    return div.childNodes[0];
}

function RSAKeyPair() {
    var encryptionExponent = "010001";
    var decryptionExponent = "";
    var modulus = "9A568982EE4BF010C38B5195A6F2DC7D66D5E6C02098CF25044CDD031AC08C6569D7063BB8959CB3FCB5AF572DE355AFA684AF7187948744E673275B494F394AF7F158841CA8B63BF65F185883F8D773A57ED731EDCD1AF2E0E57CD45F5F3CB4EBDD38F4A267E5ED02E7B44B93EDFFDADBDC8368019CD496BEC735BAF9E57125";
    this.e = biFromHex(encryptionExponent);
    this.d = biFromHex(decryptionExponent);
    this.m = biFromHex(modulus);
    this.digitSize = 2 * biHighIndex(this.m) + 2;
    this.chunkSize = this.digitSize - 11;
    this.radix = 16;
    this.barrett = new BarrettMu(this.m);
}

function encryptedString(key, s) {
    if (key.chunkSize > key.digitSize - 11) {
        return "Error";
    }
    var a = new Array();
    var sl = s.length;

    var i = 0;
    while (i < sl) {
        a[i] = s.charCodeAt(i);
        i++;
    }
    var al = a.length;
    var result = "";
    var j, k, block;
    for (i = 0; i < al; i += key.chunkSize) {
        block = new BigInt();
        j = 0;
        var x;
        var msgLength = (i + key.chunkSize) > al ? al % key.chunkSize : key.chunkSize;
        var b = new Array();
        for (x = 0; x < msgLength; x++) {
            b[x] = a[i + msgLength - 1 - x];
        }
        b[msgLength] = 0;
        // marker
        var paddedSize = Math.max(8, key.digitSize - 3 - msgLength);

        for (x = 0; x < paddedSize; x++) {
            b[msgLength + 1 + x] = Math.floor(Math.random() * 254) + 1;
        }

        b[key.digitSize - 2] = 2;
        // marker
        b[key.digitSize - 1] = 0;
        // marker

        for (k = 0; k < key.digitSize; ++j) {
            block.digits[j] = b[k++];
            block.digits[j] += b[k++] << 8;
        }
        var crypt = key.barrett.powMod(block, key.e);
        var text = key.radix == 16 ? biToHex(crypt) : biToString(crypt, key.radix);
        result += text + " ";
    }
    return result.substring(0, result.length - 1);
    // Remove last space.
}

var biRadixBase = 2;
var biRadixBits = 16;
var bitsPerDigit = biRadixBits;
var biRadix = 1 << 16; // = 2^16 = 65536
var biHalfRadix = biRadix >>> 1;
var biRadixSquared = biRadix * biRadix;
var maxDigitVal = biRadix - 1;
var maxInteger = 9999999999999998;


var maxDigits;
var ZERO_ARRAY;
var bigZero, bigOne;

function setMaxDigits(value)
{
	maxDigits = value;
	ZERO_ARRAY = new Array(maxDigits);
	for (var iza = 0; iza < ZERO_ARRAY.length; iza++) ZERO_ARRAY[iza] = 0;
	bigZero = new BigInt();
	bigOne = new BigInt();
	bigOne.digits[0] = 1;
}

setMaxDigits(20);

// The maximum number of digits in base 10 you can convert to an
// integer without JavaScript throwing up on you.
var dpl10 = 15;
// lr10 = 10 ^ dpl10
var lr10 = biFromNumber(1000000000000000);

function BigInt(flag)
{
	if (typeof flag == "boolean" && flag == true) {
		this.digits = null;
	}
	else {
		this.digits = ZERO_ARRAY.slice(0);
	}
	this.isNeg = false;
}


function biCopy(bi)
{
	var result = new BigInt(true);
	result.digits = bi.digits.slice(0);
	result.isNeg = bi.isNeg;
	return result;
}

function biFromNumber(i)
{
	var result = new BigInt();
	result.isNeg = i < 0;
	i = Math.abs(i);
	var j = 0;
	while (i > 0) {
		result.digits[j++] = i & maxDigitVal;
		i = Math.floor(i / biRadix);
	}
	return result;
}

function reverseStr(s)
{
	var result = "";
	for (var i = s.length - 1; i > -1; --i) {
		result += s.charAt(i);
	}
	return result;
}

var hexatrigesimalToChar = new Array(
 '0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z'
);

function biToString(x, radix)
	// 2 <= radix <= 36
{
	var b = new BigInt();
	b.digits[0] = radix;
	var qr = biDivideModulo(x, b);
	var result = hexatrigesimalToChar[qr[1].digits[0]];
	while (biCompare(qr[0], bigZero) == 1) {
		qr = biDivideModulo(qr[0], b);
		digit = qr[1].digits[0];
		result += hexatrigesimalToChar[qr[1].digits[0]];
	}
	return (x.isNeg ? "-" : "") + reverseStr(result);
}


var hexToChar = new Array('0', '1', '2', '3', '4', '5', '6', '7', '8', '9',
                          'a', 'b', 'c', 'd', 'e', 'f');

function digitToHex(n)
{
	var mask = 0xf;
	var result = "";
	for (i = 0; i < 4; ++i) {
		result += hexToChar[n & mask];
		n >>>= 4;
	}
	return reverseStr(result);
}

function biToHex(x)
{
	var result = "";
	var n = biHighIndex(x);
	for (var i = biHighIndex(x); i > -1; --i) {
		result += digitToHex(x.digits[i]);
	}
	return result;
}

function charToHex(c)
{
	var ZERO = 48;
	var NINE = ZERO + 9;
	var littleA = 97;
	var littleZ = littleA + 25;
	var bigA = 65;
	var bigZ = 65 + 25;
	var result;

	if (c >= ZERO && c <= NINE) {
		result = c - ZERO;
	} else if (c >= bigA && c <= bigZ) {
		result = 10 + c - bigA;
	} else if (c >= littleA && c <= littleZ) {
		result = 10 + c - littleA;
	} else {
		result = 0;
	}
	return result;
}

function hexToDigit(s)
{
	var result = 0;
	var sl = Math.min(s.length, 4);
	for (var i = 0; i < sl; ++i) {
		result <<= 4;
		result |= charToHex(s.charCodeAt(i))
	}
	return result;
}

function biFromHex(s)
{
	var result = new BigInt();
	var sl = s.length;
	for (var i = sl, j = 0; i > 0; i -= 4, ++j) {
		result.digits[j] = hexToDigit(s.substr(Math.max(i - 4, 0), Math.min(i, 4)));
	}
	return result;
}


function biAdd(x, y)
{
	var result;

	if (x.isNeg != y.isNeg) {
		y.isNeg = !y.isNeg;
		result = biSubtract(x, y);
		y.isNeg = !y.isNeg;
	}
	else {
		result = new BigInt();
		var c = 0;
		var n;
		for (var i = 0; i < x.digits.length; ++i) {
			n = x.digits[i] + y.digits[i] + c;
			result.digits[i] = n % biRadix;
			c = Number(n >= biRadix);
		}
		result.isNeg = x.isNeg;
	}
	return result;
}

function biSubtract(x, y)
{
	var result;
	if (x.isNeg != y.isNeg) {
		y.isNeg = !y.isNeg;
		result = biAdd(x, y);
		y.isNeg = !y.isNeg;
	} else {
		result = new BigInt();
		var n, c;
		c = 0;
		for (var i = 0; i < x.digits.length; ++i) {
			n = x.digits[i] - y.digits[i] + c;
			result.digits[i] = n % biRadix;
			// Stupid non-conforming modulus operation.
			if (result.digits[i] < 0) result.digits[i] += biRadix;
			c = 0 - Number(n < 0);
		}
		// Fix up the negative sign, if any.
		if (c == -1) {
			c = 0;
			for (var i = 0; i < x.digits.length; ++i) {
				n = 0 - result.digits[i] + c;
				result.digits[i] = n % biRadix;
				// Stupid non-conforming modulus operation.
				if (result.digits[i] < 0) result.digits[i] += biRadix;
				c = 0 - Number(n < 0);
			}
			// Result is opposite sign of arguments.
			result.isNeg = !x.isNeg;
		} else {
			// Result is same sign.
			result.isNeg = x.isNeg;
		}
	}
	return result;
}

function biHighIndex(x)
{
	var result = x.digits.length - 1;
	while (result > 0 && x.digits[result] == 0) --result;
	return result;
}

function biNumBits(x)
{
	var n = biHighIndex(x);
	var d = x.digits[n];
	var m = (n + 1) * bitsPerDigit;
	var result;
	for (result = m; result > m - bitsPerDigit; --result) {
		if ((d & 0x8000) != 0) break;
		d <<= 1;
	}
	return result;
}

function biMultiply(x, y)
{
	var result = new BigInt();
	var c;
	var n = biHighIndex(x);
	var t = biHighIndex(y);
	var u, uv, k;

	for (var i = 0; i <= t; ++i) {
		c = 0;
		k = i;
		for (j = 0; j <= n; ++j, ++k) {
			uv = result.digits[k] + x.digits[j] * y.digits[i] + c;
			result.digits[k] = uv & maxDigitVal;
			c = uv >>> biRadixBits;
			//c = Math.floor(uv / biRadix);
		}
		result.digits[i + n + 1] = c;
	}
	// Someone give me a logical xor, please.
	result.isNeg = x.isNeg != y.isNeg;
	return result;
}

function biMultiplyDigit(x, y)
{
	var n, c, uv;

	result = new BigInt();
	n = biHighIndex(x);
	c = 0;
	for (var j = 0; j <= n; ++j) {
		uv = result.digits[j] + x.digits[j] * y + c;
		result.digits[j] = uv & maxDigitVal;
		c = uv >>> biRadixBits;
		//c = Math.floor(uv / biRadix);
	}
	result.digits[1 + n] = c;
	return result;
}

function arrayCopy(src, srcStart, dest, destStart, n)
{
	var m = Math.min(srcStart + n, src.length);
	for (var i = srcStart, j = destStart; i < m; ++i, ++j) {
		dest[j] = src[i];
	}
}

var highBitMasks = new Array(0x0000, 0x8000, 0xC000, 0xE000, 0xF000, 0xF800,
                             0xFC00, 0xFE00, 0xFF00, 0xFF80, 0xFFC0, 0xFFE0,
                             0xFFF0, 0xFFF8, 0xFFFC, 0xFFFE, 0xFFFF);

function biShiftLeft(x, n)
{
	var digitCount = Math.floor(n / bitsPerDigit);
	var result = new BigInt();
	arrayCopy(x.digits, 0, result.digits, digitCount,
	          result.digits.length - digitCount);
	var bits = n % bitsPerDigit;
	var rightBits = bitsPerDigit - bits;
	for (var i = result.digits.length - 1, i1 = i - 1; i > 0; --i, --i1) {
		result.digits[i] = ((result.digits[i] << bits) & maxDigitVal) |
		                   ((result.digits[i1] & highBitMasks[bits]) >>>
		                    (rightBits));
	}
	result.digits[0] = ((result.digits[i] << bits) & maxDigitVal);
	result.isNeg = x.isNeg;
	return result;
}

var lowBitMasks = new Array(0x0000, 0x0001, 0x0003, 0x0007, 0x000F, 0x001F,
                            0x003F, 0x007F, 0x00FF, 0x01FF, 0x03FF, 0x07FF,
                            0x0FFF, 0x1FFF, 0x3FFF, 0x7FFF, 0xFFFF);

function biShiftRight(x, n)
{
	var digitCount = Math.floor(n / bitsPerDigit);
	var result = new BigInt();
	arrayCopy(x.digits, digitCount, result.digits, 0,
	          x.digits.length - digitCount);
	var bits = n % bitsPerDigit;
	var leftBits = bitsPerDigit - bits;
	for (var i = 0, i1 = i + 1; i < result.digits.length - 1; ++i, ++i1) {
		result.digits[i] = (result.digits[i] >>> bits) |
		                   ((result.digits[i1] & lowBitMasks[bits]) << leftBits);
	}
	result.digits[result.digits.length - 1] >>>= bits;
	result.isNeg = x.isNeg;
	return result;
}

function biMultiplyByRadixPower(x, n)
{
	var result = new BigInt();
	arrayCopy(x.digits, 0, result.digits, n, result.digits.length - n);
	return result;
}

function biDivideByRadixPower(x, n)
{
	var result = new BigInt();
	arrayCopy(x.digits, n, result.digits, 0, result.digits.length - n);
	return result;
}

function biModuloByRadixPower(x, n)
{
	var result = new BigInt();
	arrayCopy(x.digits, 0, result.digits, 0, n);
	return result;
}

function biCompare(x, y)
{
	if (x.isNeg != y.isNeg) {
		return 1 - 2 * Number(x.isNeg);
	}
	for (var i = x.digits.length - 1; i >= 0; --i) {
		if (x.digits[i] != y.digits[i]) {
			if (x.isNeg) {
				return 1 - 2 * Number(x.digits[i] > y.digits[i]);
			} else {
				return 1 - 2 * Number(x.digits[i] < y.digits[i]);
			}
		}
	}
	return 0;
}

function biDivideModulo(x, y)
{
	var nb = biNumBits(x);
	var tb = biNumBits(y);
	var origYIsNeg = y.isNeg;
	var q, r;
	if (nb < tb) {
		// |x| < |y|
		if (x.isNeg) {
			q = biCopy(bigOne);
			q.isNeg = !y.isNeg;
			x.isNeg = false;
			y.isNeg = false;
			r = biSubtract(y, x);
			// Restore signs, 'cause they're references.
			x.isNeg = true;
			y.isNeg = origYIsNeg;
		} else {
			q = new BigInt();
			r = biCopy(x);
		}
		return new Array(q, r);
	}

	q = new BigInt();
	r = x;

	// Normalize Y.
	var t = Math.ceil(tb / bitsPerDigit) - 1;
	var lambda = 0;
	while (y.digits[t] < biHalfRadix) {
		y = biShiftLeft(y, 1);
		++lambda;
		++tb;
		t = Math.ceil(tb / bitsPerDigit) - 1;
	}
	// Shift r over to keep the quotient constant. We'll shift the
	// remainder back at the end.
	r = biShiftLeft(r, lambda);
	nb += lambda; // Update the bit count for x.
	var n = Math.ceil(nb / bitsPerDigit) - 1;

	var b = biMultiplyByRadixPower(y, n - t);
	while (biCompare(r, b) != -1) {
		++q.digits[n - t];
		r = biSubtract(r, b);
	}
	for (var i = n; i > t; --i) {
    var ri = (i >= r.digits.length) ? 0 : r.digits[i];
    var ri1 = (i - 1 >= r.digits.length) ? 0 : r.digits[i - 1];
    var ri2 = (i - 2 >= r.digits.length) ? 0 : r.digits[i - 2];
    var yt = (t >= y.digits.length) ? 0 : y.digits[t];
    var yt1 = (t - 1 >= y.digits.length) ? 0 : y.digits[t - 1];
		if (ri == yt) {
			q.digits[i - t - 1] = maxDigitVal;
		} else {
			q.digits[i - t - 1] = Math.floor((ri * biRadix + ri1) / yt);
		}

		var c1 = q.digits[i - t - 1] * ((yt * biRadix) + yt1);
		var c2 = (ri * biRadixSquared) + ((ri1 * biRadix) + ri2);
		while (c1 > c2) {
			--q.digits[i - t - 1];
			c1 = q.digits[i - t - 1] * ((yt * biRadix) | yt1);
			c2 = (ri * biRadix * biRadix) + ((ri1 * biRadix) + ri2);
		}

		b = biMultiplyByRadixPower(y, i - t - 1);
		r = biSubtract(r, biMultiplyDigit(b, q.digits[i - t - 1]));
		if (r.isNeg) {
			r = biAdd(r, b);
			--q.digits[i - t - 1];
		}
	}
	r = biShiftRight(r, lambda);
	// Fiddle with the signs and stuff to make sure that 0 <= r < y.
	q.isNeg = x.isNeg != origYIsNeg;
	if (x.isNeg) {
		if (origYIsNeg) {
			q = biAdd(q, bigOne);
		} else {
			q = biSubtract(q, bigOne);
		}
		y = biShiftRight(y, lambda);
		r = biSubtract(y, r);
	}
	// Check for the unbelievably stupid degenerate case of r == -0.
	if (r.digits[0] == 0 && biHighIndex(r) == 0) r.isNeg = false;

	return new Array(q, r);
}

function biDivide(x, y)
{
	return biDivideModulo(x, y)[0];
}

function biModulo(x, y)
{
	return biDivideModulo(x, y)[1];
}

function biMultiplyMod(x, y, m)
{
	return biModulo(biMultiply(x, y), m);
}


function BarrettMu(m)
{
	this.modulus = biCopy(m);
	this.k = biHighIndex(this.modulus) + 1;
	var b2k = new BigInt();
	b2k.digits[2 * this.k] = 1; // b2k = b^(2k)
	this.mu = biDivide(b2k, this.modulus);
	this.bkplus1 = new BigInt();
	this.bkplus1.digits[this.k + 1] = 1; // bkplus1 = b^(k+1)
	this.modulo = BarrettMu_modulo;
	this.multiplyMod = BarrettMu_multiplyMod;
	this.powMod = BarrettMu_powMod;
}

function BarrettMu_modulo(x)
{
	var q1 = biDivideByRadixPower(x, this.k - 1);
	var q2 = biMultiply(q1, this.mu);
	var q3 = biDivideByRadixPower(q2, this.k + 1);
	var r1 = biModuloByRadixPower(x, this.k + 1);
	var r2term = biMultiply(q3, this.modulus);
	var r2 = biModuloByRadixPower(r2term, this.k + 1);
	var r = biSubtract(r1, r2);
	if (r.isNeg) {
		r = biAdd(r, this.bkplus1);
	}
	var rgtem = biCompare(r, this.modulus) >= 0;
	while (rgtem) {
		r = biSubtract(r, this.modulus);
		rgtem = biCompare(r, this.modulus) >= 0;
	}
	return r;
}

function BarrettMu_multiplyMod(x, y)
{
	/*
	x = this.modulo(x);
	y = this.modulo(y);
	*/
	var xy = biMultiply(x, y);
	return this.modulo(xy);
}

function BarrettMu_powMod(x, y)
{
	var result = new BigInt();
	result.digits[0] = 1;
	var a = x;
	var k = y;
	while (true) {
		if ((k.digits[0] & 1) != 0) result = this.multiplyMod(result, a);
		k = biShiftRight(k, 1);
		if (k.digits[0] == 0 && biHighIndex(k) == 0) break;
		a = this.multiplyMod(a, a);
	}
	return result;
}





setMaxDigits(129);
var key = new RSAKeyPair();
console.log(encryptedString(key, encodeURIComponent("cesssssss")))