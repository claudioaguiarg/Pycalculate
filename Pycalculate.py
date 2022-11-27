import math as m
import tkinter as tk

expression = 0
pad = ''
printed_numbers = '0'

def numbers(num):
    global pad
    pad = pad + str(num)
    print(pad)

def atualization():
    global printed_numbers
    label_expression.config(text = printed_numbers) 
    label_expression.after(1000, atualization) 

def soma():
    global expression
    global printed_numbers
    global pad
    expression += int(pad)
    printed_numbers = printed_numbers + '+' + str(pad)
    pass

calculate = tk.Tk()
calculate.geometry('310x275')

label_expression = tk.Label(width=28, height=2, bg='black', justify='right', foreground='white')
label_expression.place(x = 20, y=24)

n1 = tk.Button(calculate, text=1, width=8, height=2, command=numbers(1)).place(x = 20, y=70)
n2 = tk.Button(calculate, text=2, width=8, height=2, command=numbers).place(x = 90, y=70)
n3 = tk.Button(calculate, text=2, width=8,height=2,command=numbers).place(x = 160, y=70)

n4 = tk.Button(calculate, text=4, width=8, height=2).place(x = 20, y=120)
n5 = tk.Button(calculate, text=5, width=8, height=2).place(x = 90, y=120)
n6 = tk.Button(calculate, text=6, width=8, height=2).place(x = 160, y=120)

n7 = tk.Button(calculate, text=4, width=8, height=2).place(x = 20, y=170)
n8 = tk.Button(calculate, text=5, width=8, height=2).place(x = 90, y=170)
n9 = tk.Button(calculate, text=6, width=8, height=2).place(x = 160, y=170)

div = tk.Button(calculate, text='/', width=8,height=2).place(x = 20, y=220)
n0 = tk.Button(calculate, text=0, width=8, height=2).place(x = 90, y=220)
point = tk.Button(calculate, text='.', width=8, height=2).place(x = 160, y=220)
equal = tk.Button(calculate, text='=', width=8, height=2).place(x = 230, y=220)


delete = tk.Button(calculate, text='⌦', width=8,height=2).place(x = 230, y=20)
mult = tk.Button(calculate, text='*', width=8,height=2).place(x = 230, y=70)
sub = tk.Button(calculate, text='-', width=8, height=2).place(x = 230, y=120)
sum = tk.Button(calculate, text='+', width=8, height=2, command=soma).place(x = 230, y=170)
calculate.mainloop()
