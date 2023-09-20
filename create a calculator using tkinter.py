from tkinter import Tk, Entry, Button, StringVar

# Tkinter is a module in python that is used to create GUIs(Graphical user interfaces)
# tk is the main window/ root window for you application.
# Entry is for text input
# stringvar is a special variable used in tkinter ro manage the widget values dynamically

class Calculator:
    def __init__(self, window):  # master is an instance of tkinter and is used to represent the main application window
        window.title("Calculator")
        window.geometry('357x420+0+0')
        # (widthxheight+x+y) it specifies the window's width and height, and the position on the screen
        window.config(bg='gray')
        window.resizable(False, False)
        # user is unable to change the size of the GUI window, both horizontally and vertically
        
        self.equation = StringVar() # used to store and update the contents of the calculator's display
        self.entry_value = ' '
        Entry(width=17, bg='lightblue', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)      


        Button(width=11, height=4, text=' ( ', relief='raise', bg='white', command=lambda:self.show('(')).place(x= 0 , y=50)
        Button(width=11, height=4, text=' ) ', relief='flat', bg='white', command=lambda:self.show(')')).place(x= 90 , y=50)
        Button(width=11, height=4, text=' % ', relief='flat', bg='white', command=lambda:self.show('%')).place(x= 180 , y=50)
        Button(width=11, height=4, text=' 1 ', relief='sunken', bg='white', command=lambda:self.show(1)).place(x= 0 , y=125)
        Button(width=11, height=4, text=' 2 ', relief='flat', bg='white', command=lambda:self.show(2)).place(x= 90 , y=125)
        Button(width=11, height=4, text=' 3 ', relief='flat', bg='white', command=lambda:self.show(3)).place(x= 180 , y=125)
        Button(width=11, height=4, text=' 4 ', relief='flat', bg='white', command=lambda:self.show(4)).place(x= 0 , y=200)
        Button(width=11, height=4, text=' 5 ', relief='flat', bg='white', command=lambda:self.show(5)).place(x= 90 , y=200)
        Button(width=11, height=4, text=' 6 ', relief='flat', bg='white', command=lambda:self.show(6)).place(x= 180 , y=200)
        Button(width=11, height=4, text=' 7 ', relief='flat', bg='white', command=lambda:self.show(7)).place(x= 0 , y=275)
        Button(width=11, height=4, text=' 8 ', relief='flat', bg='white', command=lambda:self.show(8)).place(x= 180 , y=275)
        Button(width=11, height=4, text=' 9 ', relief='flat', bg='white', command=lambda:self.show(9)).place(x= 90 , y=275)
        Button(width=11, height=4, text=' 0 ', relief='flat', bg='white', command=lambda:self.show(0)).place(x= 90 , y=350)
        Button(width=11, height=4, text=' . ', relief='flat', bg='white', command=lambda:self.show('.')).place(x= 180 , y=350)
        Button(width=11, height=4, text=' + ', relief='flat', bg='white', command=lambda:self.show('+')).place(x= 270 , y=275)
        Button(width=11, height=4, text=' - ', relief='flat', bg='white', command=lambda:self.show('-')).place(x= 270 , y=200)
        Button(width=11, height=4, text=' / ', relief='flat', bg='white', command=lambda:self.show('/')).place(x= 270 , y=50)
        Button(width=11, height=4, text=' X ', relief='flat', bg='white', command=lambda:self.show('*')).place(x= 270 , y=125)
        Button(width=11, height=4, text=' = ', relief='flat', bg='lightblue', command=self.solve).place(x= 270 , y=350)
        Button(width=11, height=4, text=' C ', relief='flat', command=self.clear).place(x= 0 , y=350)

# master reperesents the main application window

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)
        
    def clear(self):
        self.entry_value = ' '
        self.equation.set(self.entry_value)
        
    def solve(self):
        result = eval(self.entry_value)
        self.equation.set(result)

root = Tk()
calculator = Calculator(root)
root.mainloop()






