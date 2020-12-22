from tkinter import Tk, Entry, Button, Checkbutton, Label, LabelFrame, Listbox, OptionMenu, StringVar, IntVar, Text, \
messagebox, simpledialog
from typing import Any, Optional

import matplotlib.pyplot as plt
import tkinter as tk
from PIL import Image, ImageTk
import os
window = tk.Tk()

# creating a Gui title
window.title("Lab Inventory")

# Helps display user bacteria input on listbox
def show_bacterial_listbox_entries(lb):
    lb.insert(tk.END, "Bacillus")
    lb.insert(tk.END, "Spirillum")
    lb.insert(tk.END, "Rickettsia")
    lb.insert(tk.END, "Mycoplasma")
    lb.configure(state='enabled')

# Helps display user medication input on listbox
def show_medicine_listbox_entries(lb):
    lb.insert(tk.END, "Formula-FD102")
    lb.insert(tk.END, "Formula-FD201")
    lb.insert(tk.END, "Formula-FD202")
    lb.insert(tk.END, "Formula-FD505")
    lb.configure(state='enabled')
# The clear command helps clear the user input values
def clear_command():
    input_bacteria_culture_id.set("")
    bacteria_selection.set("")
    medicine_selection.set("")
    output_evening_bacteria_count.set("")
    output_morning_bacteria_count.set("")
    output_linear_graph.set("")

# defining the confirm command to enable user input data and perform its function
def confirm_command():
    bacteria = bacteria_selection.get()
    medicine = medicine_selection.get()
    try:
        bacteria_id = int(bacterial_culture_id_entry.get())
    except:
        messagebox.showerror("Error", "Invalid bacteria ID, try again")
        return
    try:
        am_count = int(morning_bacteria_count_entry.get())
        pm_count = int(evening_bacteria_count_entry.get())
    except:
        messagebox.showerror("Error", "Invalid entry, try again")
        return
    rate_of_change = (pm_count / am_count) - 1
    total = "Bacteria ID:" + str(bacteria_id) + ":" + "Bacteria:" + bacteria + ":" + "Medicine" + medicine + ":" + "AM Count:" + str(am_count) + ":" + "PM Count:" + str(pm_count) + ":" + "Rate of Change:" + str(rate_of_change)
    list_display.insert(0, total)

# initiating the save command to hold user entry data
def save_command():
    list_content = list_display.get(0, tk.END)
    filename = tk.simpledialog.askstring("save file", "please enter a file name")
    try:
        file = open(filename, "w")
    except:
        messagebox.showerror("Error", "Try again")
        return
    if file == None:
        return
    for entry in list_content:
        file.write(entry + "\n")
    file.close()

# defining the function for exit command
def exit_command():
    os.sys.exit(0)

# defining the plot function command
def plot_command():
    try:
        plot_start = tk.simpledialog.askfloat("Plot Start Point ", "enter your starting point here")
        plot_end = tk.simpledialog.askfloat("Plot End Point", "enter your end point here")
    except:
        messagebox.showerror("Error", "Can only accept number, try again")
        return
    data = list_display.get(list_display.curselection())
    items = data.split(":")
    print(items)
    am_count = float(items[6])
    pm_count = float(items[8])

# calculating using the formula given in the equation
    a = (pm_count - am_count) / 12
    b = am_count
    rate_of_change = (pm_count / am_count) - 1
# setting up empty list to hold user input for x and y values.
    x = plot_start
    x_points = []
    y_points = []
# creating a while loop
    while x < plot_end:
        y = a * x + b
# appending the start point and end point to the graph values
        x_points.append(x)
        y_points.append(y)
        x += 1
# generating a plotting point values for a graph
        plt.plot(x_points, y_points)
        plt.savefig("graph.png")

# This command helps to clear the graph to  avoid overlapping of each plotted graph.
        plt.clf()

# opening a file for picture display of linear graph.
        picture = Image.open("graph.png")
        photo = ImageTk.PhotoImage(picture)
        picture_label["image"] = photo
        picture_label.image = photo

# setting text variables as tk StringVar.
input_bacteria_culture_id = tk.StringVar()
input_morning_bacteria_count = tk.StringVar()
input_evening_bacteria_count = tk.StringVar()
input_linear_display = tk.StringVar()
output_bacteria_culture_id = tk.StringVar()
output_morning_bacteria_count = tk.StringVar()
output_evening_bacteria_count = tk.StringVar()
output_linear_graph = tk.StringVar()
medicine_selection = tk.StringVar()
bacteria_selection = tk.StringVar()
output_dropdown = tk.StringVar()

# creating Label frames for our gui setup
bacteria_culture_id_frame = tk.LabelFrame(window)
bacteria_culture_id_frame.grid(row=0, column=0)
bacteria_type_frame = tk.LabelFrame(window)
bacteria_type_frame.grid(row=1, column=0)
medicine_type_frame = tk.LabelFrame(window)
medicine_type_frame.grid(row=2, column=0)
morning_bacteria_count = tk.LabelFrame(window)
morning_bacteria_count.grid(row=3, column=0)
evening_bacteria_count = tk.LabelFrame(window)
evening_bacteria_count.grid(row=4, column=0)
list_display = tk.LabelFrame(window)
list_display.grid(row=2, column=0)
button = tk.LabelFrame(window)
button.grid(row=5, column=0)
picture = tk.LabelFrame(window)
picture.grid(row=6, column=0)

linear_frame = tk.LabelFrame(window)
linear_frame.grid(row=2, column=2)

bacteria_culture_id_label = tk.Label(window, text="Bacteria culture ID")
bacteria_culture_id_label.grid(row=0, column=0, sticky="NSEW")

# create a bacteria dropdown list to select data
bacteria_list = ["Coccus", "Bacillus", "Spirillum", "Rickettsia", "Mycoplasma"]
bacteria_label = tk.Label(window, text="Bacteria Type:")
bacteria_label.grid(row=1, column=0)
bacteria_dropdown = tk.OptionMenu(window, bacteria_selection, *bacteria_list)
bacteria_dropdown.grid(row=1, column=1)
bacteria_selection.set(bacteria_list[0])

picture_label = tk.Label(picture)
picture_label.grid(row=6, column=0)

# setup a medicine dropdown list to select data for ("Medicine")
medicine_list = ["Formula-FD102", "Formula-FD201", "Formula-FD202", "Formula-FD505"]
medicine_label = tk.Label(window, text="Medicine Type:")
medicine_label.grid(row=2, column=0, sticky="NSEW")
medicine_dropdown = tk.OptionMenu(window, medicine_selection, *medicine_list)
medicine_dropdown.grid(row=2, column=1)
medicine_selection.set(medicine_list[0])

# creating label to display information for users.
morning_bacteria_count_label = tk.Label(window, text="Bacteria Count for morning 6AM")
morning_bacteria_count_label.grid(row=3, column=0, sticky="NSEW")
evening_bacteria_count_label = tk.Label(window, text="Bacteria count for evening 6PM")
evening_bacteria_count_label.grid(row=4, column=0, sticky="NSEW")

# creating entry to accept input from user.
bacterial_culture_id_entry = tk.Entry(window, textvariable=input_bacteria_culture_id)
bacterial_culture_id_entry.grid(row=0, column=1)
morning_bacteria_count_entry = tk.Entry(window, textvariable=output_morning_bacteria_count)
morning_bacteria_count_entry.grid(row=3, column=1)
evening_bacteria_count_entry = tk.Entry(window, textvariable=output_evening_bacteria_count)
evening_bacteria_count_entry.grid(row=4, column=1)

# create a listbox to display input data from user
list_display = Listbox(window, width=35, height=10)
list_display.grid(row=1, column=2, columnspan=20, sticky="NSEW")

# Creating buttons to hold and display information
confirm_button = tk.Button(button, text="confirm", command=confirm_command)
confirm_button.grid(row=0, column=0)
clear_button = tk.Button(button, text="Clear", command=clear_command)
clear_button.grid(row=0, column=1)
exit_button = tk.Button(button, text="Exit", command=exit_command)
exit_button.grid(row=0, column=2, columnspan=20)
save_button = tk.Button(linear_frame, text="Save", command=save_command)
save_button.grid(row=2, column=2, columnspan=50, padx=5, pady=5)

plot_button = tk.Button(linear_frame, text="Projector Button", command=plot_command)
plot_button.grid(row=2, column=1)

window.mainloop()

