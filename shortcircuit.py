def func1():
    print("func1")
    return 1

def func2():
    print("func2")
    return 0

print(func2() or func1())
print(func1() and func2())
