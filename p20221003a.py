data = list()
n = input("num=")
for i in range( int(n) ):
    s = input("score=")
    data.append( int(s) )
print("最高分：",max(data))
