import numpy as np
import matplotlib.pyplot as plt
from rho import rho
from data_gen import data_generator
import visual



def main():
    
    print("Введите размерность: ")
    s = int(input())
    print("Введите сопротивление полупространства: ")
    p = int(input())
    print("Введите ширину Дайки : ")
    w = int(input())
    print("Введите высоту Дайки : ")
    h = int(input())
    print("Введите значение Дайки : ")
    v = int(input())
    print("Введите X позицию дайки: ")
    x = int(input())
    print("Введите Y позицию дайки: ")
    y = int(input())

    if (w > s or h > s):
        print("Размер Дайки превышает размерность")
        exit(0)

    g = data_generator(s,s,100,w,h,v,p,x,y)
    g.generate_data_file()
    data = rho('Data.txt') #Обрабатываем входные данные в отдельном классе

    gs_kw = dict(width_ratios=[15,1])

    #Вывод
    visual.visual_data(data, gs_kw) #Визуализация данных
    visual.curve_rho(data, gs_kw) #Визуализировать кривые rho кажущегося
    visual.rho_map(data, gs_kw) #Визуализировать карту rho кажущегося
    visual.curve_phi(data, gs_kw) #Визуализировать кривые phi
    visual.phi_map (data, gs_kw)#Визуализировать карту phi

    plt.show()


if __name__ == "__main__":
    main()
