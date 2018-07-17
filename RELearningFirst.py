# -*- coding: utf-8 -*-
import re

# 正则的归纳整理

# 元字符
'''
《元字符》
.    匹配除换行符以外的任意字符。
[]   字符类，匹配方括号中包含的任意字符。
[^]  否定字符类。匹配方括号中不包含的任意字符。
*    匹配前面的子表达式零次或多次。
+    匹配前面的子表达式一次或多次。
？    匹配前面的子表达式零次或一次，或指明一个非贪婪限定符。
{n,m} 花括号，匹配前面字符至少n 次，但是不超过 m 次。
(xyz) 字符组，按照确切的顺序匹配字符xyz。
|     分支结构，匹配符号之前的字符或后面的字符。
\     转义符，它可以还原元字符原来的含义，允许你匹配保留字符[] () {} . * + ? ^ $ \ |
^     匹配行的开始。
$     匹配行的结束

'''

'''
1.1 英文句号
英文句号 . 是元字符的最简单的例子。 元字符 . 可以匹配任意单个字符。它不会匹配换行符和新行的字符。
例如正则表达式 .ar  表示：任意字符后面跟着一个字母 a ,再后面跟着一个字母 r 。

" .ar " ==> The car parked in the garage.
        ==>     car par           gar

'''

# match 从字符串其实位置开始匹配 开头没有符合规则的 就不再匹配 返回None
m = re.match('.ar','The car parked in the garage.')

# 匹配字符串中第一个 符合规则的 并返回 不再继续匹配
m = re.search('.ar','The car parked in the garage.')
print(m.group())

# 匹配所有符合规则的 并返回数组
m = re.findall('.ar','The car parked in the garage.')
print(m)

'''
1.2 字符集
字符集也称为字符类，方括号被用于指定字符集。使用字符集内的连字符来指定字符范围。方括号内的字符范围的顺序并不重要。
例如正则表达式[Tt]he,表示：大写T 或 小写t， 后面跟字母h，再后跟字母 e 。

"[Tt]he" => The car parked in the garage.

然而，字符集中的英文句号表示它字面的含义。正则表达式 ar[.] , 表示小写字母ar 后面再跟着一个英文句号 . 字符。 

"ar[.]" => A garage is a good place to park a car.
        =>                                      ar.

1.2.1 否定字符集
一般来说插入字符 ^ 表示一个字符串的开始，但是当他在方块内出现时，它会取消字符集。例如增则表达式 [^c]ar, 
表示： 除了字母 c 以外的任意字符，后面跟着字符 a ，再后面跟着一个字母 r 。

"[^c]ar" => The car parked in the garage.  
         =>         par           gar

'''

'''
1.3 重复
   + * ？ 用来指定子模式可以出现多少次。
1.3.1 星号
该符号 * 表示匹配上一个匹配规则 零次或多次。 正则表达式 a* 表示小写字母 a 可以重复零次或者多次。
但是他如果出现在字符集或者字符类之后，它表示整个字符集的重复。
例如正则表达式 [a-z]* , 表示：一行中可以包含任意数量的小写字母。

"[a-z]*" => The car parked in the garage #21.
         =>    he car parked in the garage

该 * 符号可以与元符号 . 用在一起，
用来匹配任意字符串 .*。该 * 符号可以与空格符 \s 一起使用，用来匹配一串空格字符。 
例如正则表达式 \s*cat\s*，表示: 零个或多个空格，后面跟小写字母 c，再后面跟小写字母 a，
再再后面跟小写字母 t，后面再跟零个或多个空格。

"\s*cat\s*" => The fat cat sat on the cat.
                       cat            cat

'''
m = re.findall('[a-z]*','The car parked in the garage #21.')
print(m)

m = re.findall('\s*cat\s*','The fat cat sat on the cat.')
print(m)

'''
1.3.2 加号
该符号 + 匹配上一个字符的一次或多次。例如正则表达式 c.+t , 
表示：一个小写字母c,后跟任意数量的字符，后跟小写字母t。
"c.+t" => The fat cat sat on the mat.
       =>         cat sat on the mat

'''
m = re.findall('c.+t','The fat cat sat on the mat.')
print(m)

'''
1.3.3 问号 
在正则表达式中，元字符 ？ 用来表示前一个字符是可选的。该符号匹配前一个字符的 零次或一次。
例如：正则表达式 [T]?he，表示: 可选的大写字母 T，后面跟小写字母 h，后跟小写字母 e。
"[T]?he" => The car is parked in the garage.
         => The                   he
'''
m = re.findall('[T]?he','The car is parked in the garage.')
print(m)