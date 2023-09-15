# 十六进制转十进制
num_16 = '0xf'
# 第一个参数是字符串 '0Xff' ,第二个参数是说明，这个字符串是几进制的数。  转化的结果是一个十进制数。
num_10 = int(num_16, 16)
print(f'num_16: {num_16}, num_10: {num_10}')

# 二进制转十进制
print(int('10100111110',2))

# 八进制转十进制
print(int('17',8))

# 十进制转十六进制
print(hex(1033))

# 二进制转十六进制，先转换为十进制，然后转换为十六进制
print(hex(int('101010',2)))

# 八进制转十六进制
print(hex(int('12',8)))

# 十进制转二进制
print(bin(10))

# 十六进制转二进制
print(bin(int('f',16)))

# 八进制转二进制
print(bin(int('12',8)))

## ASCII码转文字
print(chr(65))

# 文字转ASCII码
print(ord('A'))