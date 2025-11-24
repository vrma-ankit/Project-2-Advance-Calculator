from tkinter import *
import math as m

expr = ""  # Global expression string

def press(key):
    global expr
    expr += str(key)
    display.set(expr)

def equal():
    global expr
    try:
        result = str(eval(expr, {"__builtins__": None}, {
            "sin": lambda x: m.sin(m.radians(x)),
            "cos": lambda x: m.cos(m.radians(x)),
            "tan": lambda x: m.tan(m.radians(x)),
            "sqrt": m.sqrt,
            "log": lambda x: m.log10(x),
            "ln": lambda x: m.log(x),
            "pi": m.pi,
            "e": m.e
        }))
        display.set(result)
        expr = result
    except:
        display.set("error")
        expr = ""

def clear():
    global expr
    expr = ""
    display.set("")

def backspace():
    global expr
    expr = expr[:-1]
    display.set(expr)

def advanced_function(func):
    global expr
    expr += func + "("
    display.set(expr)

def power(n):
    global expr
    expr = f"({expr})**{n}"
    display.set(expr)

def reciprocal():
    global expr
    expr = f"1/({expr})"
    display.set(expr)

def insert_pi():
    global expr
    expr += str(m.pi)
    display.set(expr)

def insert_e():
    global expr
    expr += str(m.e)
    display.set(expr)


if __name__ == "__main__":
    root = Tk()
    root.configure(bg="#1e1e1e")
    root.title("Scientific Calculator")
    root.geometry("385x367")

    display = StringVar()
    entry = Entry(root, textvariable=display, font=('Arial', 18), bg="#2d2d2d", fg="white", justify="right", bd=0)
    entry.grid(row=0, column=0, columnspan=6, ipadx=8, ipady=12, pady=15, padx=10)

    btn_style = {'fg': 'white', 'bg': '#444', 'height': 2, 'width': 6, 'font': ('Arial', 11)}

    # Row 1
    Button(root, text='(', command=lambda: press('('), **btn_style).grid(row=1, column=0)
    Button(root, text=')', command=lambda: press(')'), **btn_style).grid(row=1, column=1)
    Button(root, text='⌫', command=backspace, **btn_style).grid(row=1, column=2)
    Button(root, text='Clear', command=clear, **btn_style).grid(row=1, column=3)
    Button(root, text='ln', command=lambda: advanced_function('ln'), **btn_style).grid(row=1, column=4)
    Button(root, text='√', command=lambda: advanced_function('sqrt'), **btn_style).grid(row=1, column=5)

    # Row 2
    Button(root, text='7', command=lambda: press('7'), **btn_style).grid(row=2, column=0)
    Button(root, text='8', command=lambda: press('8'), **btn_style).grid(row=2, column=1)
    Button(root, text='9', command=lambda: press('9'), **btn_style).grid(row=2, column=2)
    Button(root, text='/', command=lambda: press('/'), **btn_style).grid(row=2, column=3)
    Button(root, text='x²', command=lambda: power(2), **btn_style).grid(row=2, column=4)
    Button(root, text='sin', command=lambda: advanced_function('sin'), **btn_style).grid(row=2, column=5)

    # Row 3
    Button(root, text='4', command=lambda: press('4'), **btn_style).grid(row=3, column=0)
    Button(root, text='5', command=lambda: press('5'), **btn_style).grid(row=3, column=1)
    Button(root, text='6', command=lambda: press('6'), **btn_style).grid(row=3, column=2)
    Button(root, text='*', command=lambda: press('*'), **btn_style).grid(row=3, column=3)
    Button(root, text='x³', command=lambda: power(3), **btn_style).grid(row=3, column=4)
    Button(root, text='cos', command=lambda: advanced_function('cos'), **btn_style).grid(row=3, column=5)

    # Row 4
    Button(root, text='1', command=lambda: press('1'), **btn_style).grid(row=4, column=0)
    Button(root, text='2', command=lambda: press('2'), **btn_style).grid(row=4, column=1)
    Button(root, text='3', command=lambda: press('3'), **btn_style).grid(row=4, column=2)
    Button(root, text='-', command=lambda: press('-'), **btn_style).grid(row=4, column=3)
    Button(root, text='1/x', command=reciprocal, **btn_style).grid(row=4, column=4)
    Button(root, text='tan', command=lambda: advanced_function('tan'), **btn_style).grid(row=4, column=5)

    # Row 5
    Button(root, text='0', command=lambda: press('0'), **btn_style).grid(row=5, column=0)
    Button(root, text='.', command=lambda: press('.'), **btn_style).grid(row=5, column=1)
    Button(root, text='=', command=equal, **btn_style).grid(row=5, column=2)
    Button(root, text='+', command=lambda: press('+'), **btn_style).grid(row=5, column=3)
    Button(root, text='%', command=lambda: press('%'), **btn_style).grid(row=5, column=4)
    Button(root, text='log', command=lambda: advanced_function('log'), **btn_style).grid(row=5, column=5)

    # Row 6 (π and e aligned properly)
    Button(root, text='π', command=insert_pi, **btn_style).grid(row=6, column=0, columnspan=3, sticky="we")
    Button(root, text='e', command=insert_e, **btn_style).grid(row=6, column=3, columnspan=3, sticky="we")

    root.mainloop()
    