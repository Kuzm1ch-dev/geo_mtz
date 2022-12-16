
import string

import random 
from datetime import datetime

from matplotlib.pyplot import step 


class data_generator:
    def __init__(self, w,h,step, cw,ch,v,p,x,y):
        self.step = step
        self.w = w 
        self.h = h
        self.cw = cw
        self.ch = ch
        self.v = v
        self.p = p
        self.x = x
        self.y = y
    def generate_data_file(self):
        #Заполняем дефолтные зачения
        array = [] 
        for i in range (2):
            row = []
            for j in range (self.h):
                row.insert(0,500)
            array.insert(len(array),row)

        
        #Остальные строки

        for i in range (self.w):
            row = []
            for j in range (self.h):
                row.insert(len(row)-1,self.p)
            array.insert(len(array),row)

        #Квадрат

        value = self.v

        for i in range (self.w):
            for j in range (self.h):
                if (i >= (self.y-1) and i <  (self.y-1) + self.ch and i < self.h) and (j >=  (self.x-1) and j <  (self.x-1) + self.cw and j < self.w):
                    array[i][j] = value

        f = open("Data.txt", "w")
        with f:
            f.write(f"{self.w} {self.h}"  + "\n")
            for r in array:
                f.write(' '.join(str(i) for i in r) + "\n")
        f.close()
        pass