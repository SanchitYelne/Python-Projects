from tkinter import *

window = Tk()
window.title("Mile to KM Convertor")
window.minsize(width=300, height=200)
window.config(padx=50, pady=50)
#
# my_label = Label(text="i am a label", font=("Arial", 24, "bold"))
# my_label.grid(column=0, row=0)
#
#
# def button_clicked():
#     user_text = input.get()
#     my_label.config(text=user_text)
#
#
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# input = Entry(width=15)
# input.grid(column=4, row=2)
#
# new_button = Button(text="i am here")
# new_button.grid(column=3, row=0)


def convertor():
    mile = float(user_input.get())
    km = 1.609 * mile
    converted_text.config(text=km)


user_input = Entry(width=10)
user_input.grid(column=1, row=0)

mile_label = Label(text="Mile")
mile_label.grid(column=2, row=0)
mile_label.config(padx=10, pady=10)

equal_label = Label(text=" is equal to")
equal_label.config(padx=10, pady=10)
equal_label.grid(column=0, row=1)

km_label = Label(text="KM")
km_label.grid(column=2, row=1)
km_label.config(padx=10, pady=10)

calculate_button = Button(text="Calculate", command=convertor)
calculate_button.grid(column=1, row=2)

converted_text = Label(text="0")
converted_text.grid(column=1, row=1)


mainloop()
