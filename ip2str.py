"""
32位ip地址转成十进制字符串.

思路:
将这个32位二进制数分成四个8位的组，然后将每个8位组分别转换为对应的十进制数，最后将这四个十进制数拼接成一个字符串。

"""

def ip2str(ip):
    # 将32位IP地址转换为4个8位组
    ip_parts = [ip >> ((3-i) * 8) & 0xFF for i in range(4)]
    print(f'ip_parts: {ip_parts}')

    return ','.join(str(i) for i in ip_parts)

if __name__ == "__main__":
    # ip_address = 0xC0A8AABB  # 32位IP地址的示例值
    ip_address = 0b11000000101010001010101010111011
    ip_string = ip2str(ip_address)
    print(ip_string)
    breakpoint()