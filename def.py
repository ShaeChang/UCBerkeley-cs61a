def f1(x):
    def f2(x):
        return x
    return f2
f1(5)(6)