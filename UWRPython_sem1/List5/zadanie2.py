#1 do 1999

N = int(input('Wprowadz liczbe z przedzialu od 1 do 1999:\n'))

Dict = [{0:'',1:'jeden',2:'dwa',3:'trzy',4:'cztery',5:'pięć',6:'sześć',7:'siedem',8:'osiem',9:'dziewięć',10:'dziesięć',
        11:'jedenaście',12:'dwanaście',13:'trzynaście',14:'czternaście',15:'piętnaście',16:'szesnaście',17:'siedemnaście',
        18:'osiemnaście',19:'dziewiętnaście'},
        {0:'',2:'dwadzieścia',3:'trzydzieści',4:'czterdzieści',5:'piędziesiąt',6:'sześćdziesiąt',
        7:'siedemdziesiąt',8:'osiemdziesiąt',9:'dziewięćdziesiąt'},
        {0:'',1:'sto',2:'dwieście',3:'trzysta',4:'czterysta',5:'pięćset',6:'sześćset',7:'siedemset',8:'osiemset',9:'dziewięćset'}]


def slovo(N:int):
    if(len(list(str(N)))==2 or len(list(str(N)))==1):
        if(N>0 and N<20):
            return Dict[0][N]
        if(N>19 and N<100):
            N_slov = list(str(N))
            X = Dict[1][int(N_slov[0])] + " " + Dict[0][int(N_slov[1])]
            return X
    if(len(list(str(N)))==3):
        N_slov = list(str(N))
        X = Dict[2][int(N_slov[0])]+ " " + Dict[1][int(N_slov[1])] + " " + Dict[0][int(N_slov[2])]
        return X
    if(len(list(str(N)))==4):
        N_slov = list(str(N))
        X = "tysiąc " + Dict[2][int(N_slov[1])]+ " " + Dict[1][int(N_slov[2])] + " " + Dict[0][int(N_slov[3])]
        return X
    
print(slovo(N))