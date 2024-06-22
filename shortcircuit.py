def func1():
    print("func1")
    return 1

def func2():
    print("func2")
    return 0

print(func2() and func1())
print(func1() or func2())
