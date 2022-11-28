import math as m
import tkinter as tk

expression = 0
n1 = 0
n2 = 0
pad = ''
printed_numbers = '0'

class Numbers():

    def n1(self):
        global pad
        pad = pad + '1'
        print (pad)
    
    def n2(self):
        global pad
        pad = pad + '2'
        print (pad)

    def n3(self):
        global pad
        pad = pad + '3'
        print (pad)

    def n4(self):
        global pad
        pad = pad + '4'
        print (pad)

    def n5(self):
        global pad
        pad = pad + '5'
        print (pad)

    def n6(self):
        global pad
        pad = pad + '6'
        print (pad)   

    def n7(self):
        global pad
        pad = pad + '7'
        print (pad) 

    def n8(self):
        global pad
        pad = pad + '8'
        print (pad)

    def n9(self):
        global pad
        pad = pad + '9'
        print (pad)

    def n0(self):
        global pad
        pad = pad + '0'
        print (pad)

    def point(self):
        global pad
        pad = pad + '.'
        print (pad)


def atualization():
    global printed_numbers
    label_expression.config(text = pad) 
    label_expression.after(100, atualization) 

def soma():
    global expression
    global printed_numbers
    global pad
    expression += int(pad)
    printed_numbers = printed_numbers + '+' + str(pad)
    pass

calculate = tk.Tk()
calculate.geometry('310x275')
numbers = Numbers()

label_expression = tk.Label(width=28, height=2,text='', bg='black', justify='right', foreground='white')
label_expression.place(x = 20, y=24)
atualization()

n1 = tk.Button(calculate, text=1, width=8, height=2, command=numbers.n1).place(x = 20, y=70)
n2 = tk.Button(calculate, text=2, width=8, height=2, command=numbers.n2).place(x = 90, y=70)
n3 = tk.Button(calculate, text=3, width=8,height=2,command=numbers.n3).place(x = 160, y=70)

n4 = tk.Button(calculate, text=4, width=8, height=2, command=numbers.n4).place(x = 20, y=120)
n5 = tk.Button(calculate, text=5, width=8, height=2, command=numbers.n5).place(x = 90, y=120)
n6 = tk.Button(calculate, text=6, width=8, height=2, command=numbers.n6).place(x = 160, y=120)

n7 = tk.Button(calculate, text=7, width=8, height=2, command=numbers.n7).place(x = 20, y=170)
n8 = tk.Button(calculate, text=8, width=8, height=2, command=numbers.n8).place(x = 90, y=170)
n9 = tk.Button(calculate, text=9, width=8, height=2, command=numbers.n9).place(x = 160, y=170)

div = tk.Button(calculate, text='/', width=8,height=2).place(x = 20, y=220)
n0 = tk.Button(calculate, text=0, width=8, height=2, command=numbers.n0).place(x = 90, y=220)
point = tk.Button(calculate, text='.', width=8, height=2, command=numbers.point).place(x = 160, y=220)
equal = tk.Button(calculate, text='=', width=8, height=2).place(x = 230, y=220)


delete = tk.Button(calculate, text='⌦', width=8,height=2).place(x = 230, y=20)
mult = tk.Button(calculate, text='*', width=8,height=2).place(x = 230, y=70)
sub = tk.Button(calculate, text='-', width=8, height=2).place(x = 230, y=120)
sum = tk.Button(calculate, text='+', width=8, height=2, command=soma).place(x = 230, y=170)
calculate.mainloop()
