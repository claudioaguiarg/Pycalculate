import math as m
import tkinter as tk

expression = 0
first_number = ''
second_number = ''
result = ''
pad = ''
printed_numbers = ''

class Numbers():
    
    def n1(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '1'
        pad = pad + '1'

       
    
    def n2(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '2'
        pad = pad + '2'
        

    def n3(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '3'
        pad = pad + '3'
        

    def n4(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '4'
        pad = pad + '4'
        

    def n5(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '5'
        pad = pad + '5'
        

    def n6(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '6'
        pad = pad + '6'
           

    def n7(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '7'
        pad = pad + '7'
         

    def n8(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '8'
        pad = pad + '8'
        

    def n9(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '9'
        pad = pad + '9'


    def n0(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '0'
        pad = pad + '0'
        

    def comma(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + ','
        pad = pad + '.'

    def plus(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + '+'

    def multi(self):
        global pad
        global printed_numbers
        printed_numbers = printed_numbers + 'x'
        
        


def atualization():
    global printed_numbers
    label_expression.config(text = printed_numbers) 
    label_expression.after(1, atualization) 

def soma():
    global first_number
    global second_number
    global pad
    global result
    global printed_numbers
    printed_numbers = printed_numbers + '+'
    
    if first_number == '' and result == '':
        first_number = float(pad)
        pad = ''
        

    else:
        if second_number == '' and result == '':
            second_number = float(pad)
            result = (first_number) + (second_number)
            pad = ''
            print(result)
        else:
            second_number = float(pad)
            result += second_number
            pad = ''
            print(result)

def equal():
    
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
comma = tk.Button(calculate, text=',', width=8, height=2, command=numbers.comma).place(x = 160, y=220)
equal = tk.Button(calculate, text='=', width=8, height=2).place(x = 230, y=220)


delete = tk.Button(calculate, text='⌦', width=8,height=2).place(x = 230, y=20)
mult = tk.Button(calculate, text='*', width=8,height=2, command=numbers.multi).place(x = 230, y=70)
sub = tk.Button(calculate, text='-', width=8, height=2).place(x = 230, y=120)
sum = tk.Button(calculate, text='+', width=8, height=2, command=soma).place(x = 230, y=170)
calculate.mainloop()
