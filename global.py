x = 10

def modify_global():
    global x
    x = 20

modify_global()
print(x)  # 输出结果为 20

def outer_function():
    x = 10

    def inner_function():
        nonlocal x
        x = 30

    inner_function()
    print(x)  # 输出结果为 20

outer_function()

