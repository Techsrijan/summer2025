# def greet():
#     print('good morning')
#     msg()

# when a function call  itself it is called recursion
import sys
print(sys.getrecursionlimit())
print(sys.setrecursionlimit(2000))
def msg():
    print("everything is ok")
    #greet()
    msg()

msg()
#greet()
#msg()