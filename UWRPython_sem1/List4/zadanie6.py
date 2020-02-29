
#def conv(x,y,z):

RGB=''
RGB_new=[]
while RGB=='':
    RGB =(input('Podaj pelne kodowanie w formacie RGB: 255,255,255:\n')).split(',')
    #print(RGB)
    for i in range(0,3):
        if len(RGB)!=3:
            print('Za malo danych')
            RGB=''
            break
        if float(RGB[i])>255 or float(RGB[i])<0:
            print("{} nie nalezy do przedzialu (0,255)".format(int(RGB[i])))
            RGB=''
            break
        
for i in range(0,3):
    RGB_new.append(float(RGB[i])/255)        
#print(RGB_new)
R = float(RGB_new[0])
G = float(RGB_new[1])
B = float(RGB_new[2])
Cmax = max(R,G,B)
Cmin = min(R,G,B)
delta = Cmax - Cmin
if delta == 0:
    H = 0
if Cmax == R and delta!=0:
    H = 60*(((G-B)/delta)%6)
if Cmax == G and delta!=0:
    H = 60*((B-R)/delta+2)
if Cmax == B and delta!=0:
    H = 60*((R-G)/delta+4)
if Cmax==0:
    S = 0
if Cmax!=0:
    S = delta/Cmax*100
V = Cmax*100
print("Przeliczamy: RGB({},{},{}) = HSV({},{}%,{}%)".format(RGB[0],RGB[1],RGB[2],round(H,0),round(S,1),round(V,1)))
         
        
        


