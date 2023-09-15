def convert(s):
    if not s:
        return 
    
    n = len(s)
    
    s2 = s
    while '%' in s2:
        i = s2.rfind('%')
        # print(f'i: {i}, s2:{s2}')
        if i == 0:
            s2 = chr(int(s2[1:3], 16))
        else:
            s2 = s2[:i] + chr(int(s2[i+1:i+3], 16)) + s2[i+3:]
            # print(s2)
    return s2        

T = int(input())
for _ in range(T):
    s = input()
    print(convert(s))

## 用栈
# def decode(stack):
#     val1 = stack.pop()
#     val2 = stack.pop()
#     ch = chr(int(val1+val2,16))
#     if ch == '%':
#         stack = decode(stack)
#     else:
#         stack.append(ch)
#     return stack

# def main():
#     N = int(input())
#     for i in range(N):
#         s = str(input())
#         stack = []
#         for c in s[::-1]:
#             if c != '%':
#                 stack.append(c)
#             else:
#                 stack = decode(stack)
#         print("".join(stack[::-1]))
# main()