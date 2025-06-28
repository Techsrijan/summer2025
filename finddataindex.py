st=input("enter any text")
print("you Entered=",st)
search='t'
count=0
for i in st:
    #print(i)
    if i==search:
        print("item found at location=",count)
        break
    count=count+1
else:
    print("item not found")


print("from string method=",st.index('t'))