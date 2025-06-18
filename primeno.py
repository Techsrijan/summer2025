# n=int(input("enter any number"))
# i=2
# while i<=n-1:
#     if n%i==0:
#         print("Not Prime")
#         break
#
#     i=i+1
# else:
#     print("Prime no")




# for n in range(2,15):
#     i=2
#     while i <= n - 1:
#         if n%i==0:
#             #print("Not Prime=",n)
#             break
#
#         i=i+1
#     else:
#         print("Prime no=",n)



n=2
while n<=15:
    i = 2
    while i <= n - 1:
        if n%i==0:
            #print("Not Prime=",n)
            break
        i=i+1
    else:
        print("Prime no=",n)

    n=n+1