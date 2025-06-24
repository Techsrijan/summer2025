from functools import reduce
l=[2,4,3,6,65,224,231,88,12234]

result=list(filter(lambda a:a%2==0,l))
print(result,type(result))

# l2=[2,4,3,6,65,224,231,88,12234]
# result2=list(filter(lambda a:a%2!=0,l2))
# print(result2)

data=list(map(lambda a:a+10,result))
print(data)

output=reduce(lambda a,b:a+b,data)
print(output)

