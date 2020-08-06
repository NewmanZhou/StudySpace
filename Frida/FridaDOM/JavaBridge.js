
function  rock_paper_scissors() {
  // Function to hook is defined here
  var MainActivity = Java.use('com.example.seccon2015.rock_paper_scissors.MainActivity');

  // Whenever button is clicked
  var onClick = MainActivity.onClick;
  onClick.implementation = function (v) {
    // Show a message to know that the function got called
    send('onClick');
    console.log('onClick');
    javaBridge()
    // Call the original onClick handler
    onClick.call(this, v);

    // Set our values after running the original onClick handler
    this.m.value = 10;
    this.n.value = 1;
    // this.cnt.value = 999;
    console.log(this.m.value)
    console.log(this.n.value)
    // Log to the console that it's done, and we should have the flag!
    console.log('Done:' + JSON.stringify(this.cnt));
  };
}





function javaBridge () {
  // Create an instance of java.lang.String and initialize it with a string
  var JavaString = Java.use('java.lang.String');
  var exampleString1 = JavaString.$new('Hello World, this is an example string in Java.');
  console.log('[+] exampleString1: ' + exampleString1);
  console.log('[+] exampleString1.length(): ' + exampleString1.length());

  // Create an instance of java.nio.charset.Charset, and initialize the default character set
  var Charset = Java.use('java.nio.charset.Charset');
  var charset = Charset.defaultCharset();
  // Create a byte array of a Javascript string
  var charArray = 'This is a Javascript string converted to a byte array.'.split('').map(function(c) {
    return c.charCodeAt(0);
  });

  // Create an instance of java.lang.String and initialize it through an overloaded $new,
  // with a byte array and a instance of java.nio.charset.Charset
  var exampleString2 = JavaString.$new.overload('[B', 'java.nio.charset.Charset').call(JavaString, charArray, charset)
  console.log('[+] exampleString2: ' + exampleString2);
  console.log('[+] exampleString2.length(): ' + exampleString2.length());

  // Intercept the initialization of java.lang.Stringbuilder's overloaded constructor,
  // and write the partial argument to the console
  var StringBuilder = Java.use('java.lang.StringBuilder');
  // We need to replace .$init() instead of .$new(), since .$new() = .alloc() + .init()
  var ctor = StringBuilder.$init.overload('java.lang.String');
  ctor.implementation = function (arg) {
    var partial = '';
    var result = ctor.call(this, arg);
    if (arg !== null) {
      partial = arg.toString().replace('\n', '').slice(0, 10);
    }
    // console.log('new StringBuilder(java.lang.String); => ' + result);
    console.log('new StringBuilder("' + partial + '");');
    return result;
  };
  console.log('[+] new StringBuilder(java.lang.String) hooked');

  // Intercept the toString() method of java.lang.StringBuilder and write its partial contents to the console.
  var toString = StringBuilder.toString;
  toString.implementation = function () {
    var result = toString.call(this);
    var partial = '';
    if (result !== null) {
      partial = result.toString().replace('\n', '').slice(0, 10);
    }
    console.log('StringBuilder.toString(); => ' + partial);
    return result;
  };
  console.log('[+] StringBuilder.toString() hooked');
}


function main() {
    Java.perform(function () {
        rock_paper_scissors()
    });
}

setImmediate(main);