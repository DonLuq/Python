def fun(N):
    if N=='':
        print(0)
        return 0
    else:
        Suma=0
        Arg=N.split(' ')
        print(Arg)
        for i in Arg:
            Suma+=float(i)
        #print(Suma)
        print(Suma/len(Arg))
        return Suma/len(Arg)
        
        
N= input('Podaj argumenty po przecinku\n')      
        
fun(N)