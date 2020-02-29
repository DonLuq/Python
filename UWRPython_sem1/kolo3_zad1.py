x = 0
y = 0

ruch = input('Podaj sekwenscje:\n')
#ruch = ' D G D L P P P P'


def fun(ruch,x,y):
    droga = 0
    ruch = ruch.split();
    for i in range(len(ruch)):
        if ruch[i] == 'G' or ruch[i] == 'D' or ruch[i] == 'L' or ruch[i] == 'P':
            print('', end ='')
        else:
            print('Wprowadzono nie poprawna sekwencje')
            return 0
    print('Twoje dane',ruch)
    print('x0 =',x,'y0 =',y)
    for ele in ruch:
        if ele == 'G':
            y += 1
        if ele == 'D':
            y -= 1
        if ele == 'L':
            x -= 1
        if ele == 'P':
            x += 1
        droga += 1
    print('x =',x,'y =',y)
    print('Przebyta droga:',droga)
fun(ruch,0,0)