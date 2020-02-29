     
def pascal(N:int): 
  
    table = [[0 for x in range(N)] for y in range(N)]  
    for line in range (0, N): 
        for i in range (0, line + 1): 
            if(i==0 or i==line): 
                table[line][i] = 1
                print(table[line][i], end = " ")  
            else: 
                table[line][i] = (table[line - 1][i - 1] + table[line - 1][i]) 
                print(table[line][i], end = " ")              
        print("\n", end = "")


N = 10 
pascal(N);