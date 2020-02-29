import numpy as np
import matplotlib.pyplot as plt
def rysuj():
    etykiety = ['Java', 'C', 'Python','C++','C#','Visual Basic .NET','JavaScript','PHP','SQL','Swift']
    wartosci = [17.25, 16.09, 10.31,6.20,4.80,4.74,2.09,2.05,1.84,1.49]
    plt.bar(etykiety, wartosci)
    plt.xticks(rotation=30)
    plt.ylabel('Udział w rynku[%]')
    plt.title('Najpopularniejsze języki programowania:')
    plt.show()

rysuj()