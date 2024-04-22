from tkinter import *
from tkinter import ttk


class Cal:

    buttons = []

    def __init__(self):

        self.counter = 0
        self.root = Tk()
        self.frame = ttk.Frame(self.root, padding=1)
        self.frame.grid()

        self.label = Label(self.frame, text="")
        self.label.grid(column=3)

        self.enter = Entry(self.frame, width=20)
        self.enter.grid(column=1, columnspan=2, row=0, pady=10)

        # init button

        for i in range(3):
            for j in range(3):
                self.counter += 1
                temp_butt = ttk.Button(self.frame, text=str(self.counter), padding=15, width=5)
                temp_butt.grid(column=j+1, row=i+1)
                print(temp_butt)
                self.buttons.append(temp_butt)

        dott_butt = ttk.Button(self.frame, text=",", padding=15, width=5, command=lambda: self.on_click('.'))
        dott_butt.grid(column=1, row=4)

        zero_butt = ttk.Button(self.frame, text="0", padding=15, width=5, command=lambda: self.on_click('0'))
        zero_butt.grid(column=2, row=4)

        del_butt = ttk.Button(self.frame, text="C", padding=15, width=5, command=lambda: self.clear_cal())
        del_butt.grid(column=3, row=4)

        div_butt = Button(self.frame, bg='blue', foreground='white', text="/", width=5, height=3, command=lambda: self.on_click("/"))
        div_butt.grid(column=4, row=0)

        multi_butt = Button(self.frame, bg='blue', foreground='white', text="*", width=5, height=3, command=lambda: self.on_click("*"))
        multi_butt.grid(column=4, row=1)

        diff_butt = Button(self.frame, bg='blue', foreground='white', text="-", width=5, height=3, command=lambda: self.on_click("-"))
        diff_butt.grid(column=4, row=2)

        sum_butt = Button(self.frame, bg='blue', foreground='white', text="+", width=5, height=3, command=lambda: self.on_click("+"))
        sum_butt.grid(column=4, row=3)

        equal_butt = Button(self.frame, background='blue', foreground='white', text="=", width=5, height=3,  command=lambda: self.get_result())
        equal_butt.grid(column=4, row=4, padx=2)

        # set value button

        for i, button in enumerate(self.buttons):
            button.configure(text=str(i+1), command=lambda i= str(i+1): self.on_click(i))

    def on_click(self, i):
        self.enter.insert(len(self.enter.get()), i)

    def get_result(self):

        if self.enter.get() != "":
            exp = "result = {}".format(self.enter.get())
            print(exp)

            self.delete()
            try:
                exec(exp, globals())

            except ZeroDivisionError:
                self.label.configure(text="div by 0")

            except:
                self.label.configure(text="Error")

            else:
                print(result)
                self.label.configure(text="")
                self.enter.insert(0, str(result))

    def delete(self):
        self.enter.delete(0, END)

    def clear_cal(self):
        self.enter.delete(0, END)
        self.label.configure(text="")

    def run_window(self):
        self.root.mainloop()


cal = Cal()
cal.run_window()
