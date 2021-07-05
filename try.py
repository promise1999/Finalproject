from tkinter import Tk, Entry, Button, Checkbutton, Label, LabelFrame, Listbox, OptionMenu, StringVar, IntVar, Text, \
    messagebox
import tkinter as tk

HST_RATE = 0.15


def make_horizontal_label_and_textbox_combo(master, base_row=0, base_column=0, label_text=None, entry_options=dict(),
                                            label_options=dict(), entry_grid_options=dict(), label_grid_options=dict()):
    textvariable = StringVar()

    label = Label(master, text=label_text, **label_options)
    label.grid(row=base_row, column=base_column, **label_grid_options)

    entry = Entry(master, textvariable=textvariable, **entry_options)
    entry.grid(row=base_row, column=base_column + 1, **entry_grid_options)
    return label, entry, textvariable


def make_checkbutton(master, row=0, column=0, checkbutton_text="", checkbutton_options=dict(),
                     checkbutton_grid_options=dict()):
    int_var = IntVar()
    checkbutton = Checkbutton(master, text=checkbutton_text, variable=int_var, **checkbutton_options)
    checkbutton.grid(row=row, column=column, **checkbutton_grid_options)

    return checkbutton, int_var


def make_horizontal_optionbox_and_label_combo(master, base_row=0, base_column=0, label_text=None, options=tuple(),
                                              label_options=dict(), option_menu_options=dict(),
                                              label_grid_options=dict(), option_menu_grid_options=dict()):
    optionmenu_var = StringVar()
    if len(options) > 0:
        optionmenu_var.set(options[0])

    label = Label(master, text=label_text, **label_options)
    label.grid(row=base_row, column=base_column)

    option_menu = OptionMenu(master, optionmenu_var, *options, **option_menu_options)
    option_menu.grid(row=base_row, column=base_column + 1, **option_menu_grid_options)

    return label, option_menu, optionmenu_var

def show_package_listbox_entries(lb):
    lb.insert(tk.END, "Standard  - Exterior wash, Interior cleaning")
    lb.insert(tk.END, "Deluxe    - Exterior wash, Hand wax, Interior cleaning, Check fluid levels")
    lb.insert(tk.END, "Executive - Exterior wash, Hand wax, Interior cleaning, Check fluid levels, Shampoo upholstery")
    lb.configure(state='enabled')


def hide_package_listbox_entries(lb):
    lb.delete(tk.END)
    lb.delete(tk.END)
    lb.delete(tk.END)
    lb.configure(state='disabled')


def start():
    window = Tk()
    window.title("VB Auto Center")

    customer_information_frame = LabelFrame(window, text="Customer Information")
    customer_information_frame.grid(row=0, column=0, sticky="NSEW")

    _, _, plate_number_entry_variable = make_horizontal_label_and_textbox_combo(customer_information_frame, base_row=0,
                                                                                label_text="Plate Number")
    _, _, name_entry_variable = make_horizontal_label_and_textbox_combo(customer_information_frame, base_row=1,
                                                                        label_text="Name")
    _, _, address_entry_variable = make_horizontal_label_and_textbox_combo(customer_information_frame, base_row=2,
                                                                           label_text="Address")
    _, _, city_entry_variable = make_horizontal_label_and_textbox_combo(customer_information_frame, base_row=3,
                                                                        label_text="City")
    _, _, phone_entry_variable = make_horizontal_label_and_textbox_combo(customer_information_frame, base_row=4,
                                                                         label_text="Phone")

    other_services_frame = LabelFrame(window, text="Other Services")
    other_services_frame.grid(row=0, column=1, sticky="NSEW")

    cbg_opts = {
        'sticky': "W"
    }
    _, grease_oil_filter_checkbox_variable = make_checkbutton(other_services_frame, row=0,
                                                              checkbutton_text="Grease, Oil, and Filter (GOF)",
                                                              checkbutton_grid_options=cbg_opts)
    _, rust_proofing_checkbox_variable = make_checkbutton(other_services_frame, row=1,
                                                          checkbutton_text="Rust Proofing Service",
                                                          checkbutton_grid_options=cbg_opts)
    _, tire_change_checkbox_variable = make_checkbutton(other_services_frame, row=2,
                                                        checkbutton_text="Tire Change and Balance",
                                                        checkbutton_grid_options=cbg_opts)
    _, tire_entry, tire_change_entry_variable = make_horizontal_label_and_textbox_combo(other_services_frame,
                                                                                        base_row=2, base_column=1,
                                                                                        label_text="#")
    tire_entry.configure(state="disabled")

    def on_tire_change_check_updated(*args):
        if tire_change_checkbox_variable.get() != 0:
            tire_entry.configure(state="normal")
        else:
            tire_entry.configure(state="disabled")

    tire_change_checkbox_variable.trace("w", on_tire_change_check_updated)

    cleaning_services_frame = LabelFrame(window, text="Cleaning Services")
    cleaning_services_frame.grid(row=1, column=0, sticky="NSEW")

    option_menu_style_options = dict()

    package_options = ('None', 'Standard', 'Deluxe', 'Executive')
    _, _, package_option_variable = make_horizontal_optionbox_and_label_combo(cleaning_services_frame, base_row=0,
                                                                              label_text="Package",
                                                                              options=package_options,
                                                                              option_menu_options=option_menu_style_options)

    cleaning_services_listbox = Listbox(cleaning_services_frame, width=35)
    cleaning_services_listbox.grid(row=1, column=0, columnspan=2)
    cleaning_services_listbox.configure(state="disabled")

    fragrance_options = ('None', 'Hawaiian Mist', 'Baby Powder', 'Pine', 'Country Floral', 'Vanilla')
    _, fragrance_option_menu, fragrance_option_variable = make_horizontal_optionbox_and_label_combo(
        cleaning_services_frame, base_row=2, label_text="Fragrance", options=fragrance_options,
        option_menu_options=option_menu_style_options)
    fragrance_option_menu.configure(state="disabled")

    def on_package_chosen(*args):
        selected_package = package_option_variable.get()
        if selected_package == package_options[-1]:
            fragrance_option_menu.configure(state="normal")
        else:
            fragrance_option_variable.set(fragrance_options[0])
            fragrance_option_menu.configure(state="disabled")

        cleaning_services_listbox.delete(tk.END)
        print(selected_package)
        print(package_options)
        if selected_package != package_options[0]:
            cleaning_services_listbox.configure(state="normal")
        else:
            cleaning_services_listbox.configure(state="disabled")
        if selected_package == package_options[1]:
            cleaning_services_listbox.insert(tk.END, "Standard  - Exterior wash, Interior cleaning")
        elif selected_package == package_options[2]:
            cleaning_services_listbox.insert(tk.END, "Deluxe    - Exterior wash, Hand wax, Interior cleaning, Check fluid levels")
        elif selected_package == package_options[3]:
            cleaning_services_listbox.insert(tk.END, "Executive - Exterior wash, Hand wax, Interior cleaning, Check fluid levels, Shampoo upholstery")

    package_option_variable.trace('w', on_package_chosen)

    charge_information_frame = LabelFrame(window, text="Charge Information")
    charge_information_frame.grid(row=1, column=1, sticky='NSEW')
    charge_textbox = Text(charge_information_frame, height=15, width=40)
    charge_textbox.grid(sticky='NSEW')

    todays_orders_frame = LabelFrame(window, text="Today's Orders")
    todays_orders_frame.grid(row=0, column=2, rowspan=3, sticky="NSEW")

    todays_orders_listbox = Listbox(todays_orders_frame, width=45)
    todays_orders_listbox.grid(sticky="NSEW")

    controls_frame = LabelFrame(window, text="Controls")
    controls_frame.grid(row=2, column=0, columnspan=2, sticky="NSEW")

    controls_frame.grid_columnconfigure(0, weight=1, uniform='a')
    controls_frame.grid_columnconfigure(1, weight=1, uniform='a')
    controls_frame.grid_columnconfigure(2, weight=1, uniform='a')
    controls_frame.grid_columnconfigure(3, weight=1, uniform='a')

    def on_calculate_clicked():
        if len(plate_number_entry_variable.get()) < 1:
            messagebox.showerror("Error", "No licence plate was provided.")
            return
        todays_orders_string = "{}".format(plate_number_entry_variable.get())
        charge_information = ""
        package_selected = package_option_variable.get()
        package_name = package_selected
        package_cost = 0
        if package_selected == package_options[1]:
            package_cost = 19.99
        elif package_selected == package_options[2]:
            package_cost = 39.99
        elif package_selected == package_options[3]:
            package_cost = 59.99
            package_name = "{} (Fragrance: {})".format(package_selected, fragrance_option_variable.get())
        else:
            messagebox.showerror("Error", "No package was selected!")
            return
        charge_information += "Package: {}\n\nPackage Cost: ${:.2f}\n\n".format(package_name, package_cost)
        todays_orders_string += " - {}".format(package_name)

        options_cost = 0
        charge_information += "Other Services Selected:\n"
        if grease_oil_filter_checkbox_variable.get():
            options_cost += 48.95
            gof_s = "Grease, Oil, and Filter (GOF)"
            charge_information += gof_s + "\n"
            todays_orders_string += " - {}".format(gof_s)
        if rust_proofing_checkbox_variable.get():
            options_cost += 99.95
            rust_s = "Rust Proofing"
            charge_information += rust_s + "\n"
            todays_orders_string += " - {}".format(rust_s)
        if tire_change_checkbox_variable.get():
            num_tires = 0
            try:
                num_tires = int(tire_change_entry_variable.get())
            except:
                messagebox.showerror("Error",
                                     "Unable to convert specified number of tires to a number. Please make sure you did not make a mistake!")
                return
            options_cost += 9.95 * num_tires
            tire_s = "Tire Change and Balance - {}".format(num_tires)
            charge_information += tire_s + "\n"
            todays_orders_string += " - {}".format(tire_s)

        total = package_cost + options_cost
        hst = total * HST_RATE

        charge_information += "\nOther Services Cost: ${:.2f}\n".format(options_cost)
        charge_information += "HST: ${:.2f}\n".format(hst)

        charge_information += "\nTotal Cost: ${:.2f}".format(total)

        charge_textbox.delete("1.0", tk.END)
        charge_textbox.insert(tk.END, charge_information)

        todays_orders_listbox.insert(tk.END, todays_orders_string)

    def on_clear_clicked():
        plate_number_entry_variable.set("")
        name_entry_variable.set("")
        address_entry_variable.set("")
        city_entry_variable.set("")
        phone_entry_variable.set("")

        package_option_variable.set(package_options[0])
        fragrance_option_variable.set(fragrance_options[0])

        tire_change_entry_variable.set("")
        grease_oil_filter_checkbox_variable.set(0)
        rust_proofing_checkbox_variable.set(0)
        tire_change_checkbox_variable.set(0)

        charge_textbox.delete("1.0", tk.END)

    calculate_button = Button(controls_frame, text="Calculate", command=on_calculate_clicked)
    calculate_button.grid(row=0, column=0)

    save_button = Button(controls_frame, text="Save")
    save_button.grid(row=0, column=1)
    save_button.configure(state='disabled')

    clear_button = Button(controls_frame, text="Clear", command=on_clear_clicked)
    clear_button.grid(row=0, column=2)

    exit_button = Button(controls_frame, text="Exit", command=window.destroy)
    exit_button.grid(row=0, column=3)

    window.mainloop()
    if __name__ == "__main__":
        start()


