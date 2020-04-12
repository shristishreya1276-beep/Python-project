import tkinter
import math

window = tkinter.Tk()
window.geometry("300x380")
window.title("calculator")

number1 = tkinter.Label(text = "First Number")
number1.grid(column = 0, row = 1)
number2 = tkinter.Label(text = "Second Number")
number2.grid(column = 0, row = 2)
operation = tkinter.Label(text = "1 for +, 2 for -, 3 for *, 4 for /")
operation.grid(column = 0, row = 3)

number1Entry = tkinter.Entry()
number1Entry.grid(column = 1, row =1)
number2Entry = tkinter.Entry()
number2Entry.grid(column = 1, row = 2)
operationEntry = tkinter.Entry()
operationEntry.grid(column =1, row =3)

def banana():
    if (operationEntry.get() == '1'):
        answer = int(number1Entry.get()) + int(number2Entry.get())
    elif (operationEntry.get() == '2'):
        answer = int(number1Entry.get()) - int(number2Entry.get())
    elif (operationEntry.get() == '3'):
        answer = int(number1Entry.get()) * int(number2Entry.get())
    elif (operationEntry.get() == '4'):
        answer = int(number1Entry.get()) // int(number2Entry.get())
    else:
        answer = "Enter valid response"
        
    texter=tkinter.Text(master=window,height=10,width=10)
    texter.grid(column=1,row=5)
    texter.insert(tkinter.END,answer)

        
button=tk.Button(window,text="Calculate",command=banana,bg="pink")
button.grid(column=1,row=4)

window.mainloop()
