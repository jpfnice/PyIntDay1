import atexit

@atexit.register
def f():
    print("function f is invoked")

@atexit.register
def g():
    print("function g is invoked")
    
#atexit.register(f)
#atexit.register(g)


nb=23
print(nb**2)

