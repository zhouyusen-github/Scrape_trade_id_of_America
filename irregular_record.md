## pdf number
except from chapter00-99
year94 have chapter991-995 no 99
year95-99 have chapter991-997 no 99

## irregular format
1. 误读了后面description里by weight 95 percent里的95
对策进一步缩小正则匹配
   
    经过观察可以发现
    01型号
    " 11  "这种后面是两个空格
    "0101.20.10  00 "后面是一个空格
    
    95型号
    "0105.91.00  00  "后面是两个空格
    
    
    对策
    1. 改用行首匹配
        "0101.20.10  00 "匹配后再切割 

2. 2524.00.00 漏扫描
原因
   "10  "
   前面没有空格，所以正则对空格数的判断可能要自由化
   
a = re.match(r'\s*(\d\d)\s*', line)
        if a is not None:
            print(a.group(1))

新更改后
3. "99-113"," 12/31/2001" 错误扫描
4. "3904.69.50) ......"


"50 XXX"情况不管应该要求宁可多，不能漏

"9687"chapter

  Free (B,CA,E,IL,J) 25%
See 9906.87.01- 
9906.87.02 (MX
覆盖了正常的id号

建议 用判断这个字符是不是这个chapter来处理,有许多这种错误