try:
    a = int(input("Enter Any number"))
    b = int(input("Enter Any number"))
    c=a/b
    print("C=",c)

except ValueError:
    print("you have entered a character")
except  ZeroDivisionError:
    print(" B can not be zero")
except Exception:
    print("something went wrong")
finally:
    print("thank You for using Program")
    print(u"\u0915\u092c\u0942\u0924\u0930")
    print(u"\U0001F602")