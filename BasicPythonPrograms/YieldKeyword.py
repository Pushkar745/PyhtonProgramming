def fun():
    s=0
    for i in range(10):
        s+=i
        return s     
    print(fun())

    #Yield KeyWord
    def fun1():
        s1=0
        for i in range(10):
            s+=i
            yield s1
    for i in  fun1():
        print(i)         