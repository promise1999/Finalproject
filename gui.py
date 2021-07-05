import tkinter as tk
from PIL import Image, ImageTk
window = tk.Tk()
window.title("Adder App")
input_num1 = tk.StringVar()
input_num2 = tk.StringVar()
output_label_variable = tk.StringVar()

def add_numbers():
    try:
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())
        total = num1 + num2
    except:
        output_label_variable.set("Please enter a valid number")
    else:
        output_label_variable.set(total)
def multiply_numbers():
    try:
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())
        total = num1 * num2
    except:
        output_label_variable.set("Please enter a valid number")
    else:
        output_label_variable.set(total)
def divide_numbers():
    try:
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())
        total = num1 / num2
    except:
        output_label_variable.set("Please enter a valid number")
    else:
        output_label_variable.set(total)
def subtract_numbers():
    try:
        num1 = float(input_num1.get())
        num2 = float(input_num2.get())
        total = num1 - num2
    except:
        output_label_variable.set("Please enter a valid number")
    else:
        output_label_variable.set(total)
img = Image.open("AdderAppLogoImg.PNG")
photo = ImageTk.PhotoImage(img)
image_label = tk.Label(window, image=photo)
image_label.grid(row=0, columnspan=4)
desc_label1 = tk.Label(window, text="This is a program that can add two numbers together.")
desc_label1.grid(row=1, columnspan=4)
desc_label2 = tk.Label(window, text="Please enter your data in the fields below and click the button to generate a result.")
desc_label2.grid(row=2, columnspan=4)
fnum_label = tk.Label(window, text="First Number:")
fnum_label.grid(row=3, column=0, columnspan=2)
snum_label = tk.Label(window, text="Second Number:")
snum_label.grid(row=4, column=0, columnspan=2)
fnum_entry = tk.Entry(window, textvariable=input_num1)
fnum_entry.grid(row=3, column=2, columnspan=2)
snum_entry = tk.Entry(window, textvariable=input_num2)
snum_entry.grid(row=4, column=2, columnspan=2)
add_btn = tk.Button(window, text="Add", command=add_numbers)
add_btn.grid(row=5, column=0)
mult_btn = tk.Button(window, text="Multiply", command=multiply_numbers)
mult_btn.grid(row=5, column=1)
div_btn = tk.Button(window, text="Divide", command=divide_numbers)
div_btn.grid(row=5, column=2)
sub_btn = tk.Button(window, text="Subtract", command=subtract_numbers)
sub_btn.grid(row=5, column=3)
output_label = tk.Label(window, textvariable=output_label_variable)
output_label.grid(row=6, columnspan=4)
window.mainloop()