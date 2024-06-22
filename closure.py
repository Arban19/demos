def foo():
    x = "Ole at the wheel"
    def bar():
        print(x)
    return bar

z = foo()
z()
