import tkinter as tk
import os
import tkinter.ttk as ttk
window= tk.Tk()
window.title("Auto Center")
# declearing variable
input_plate= tk.StringVar()
input_name= tk.StringVar()
input_address= tk.StringVar()
input_city= tk.StringVar()
input_phone= tk.StringVar()
input_package= tk.StringVar()

customer_frame= tk.LabelFrame(window, text= "Customer Information")
customer_frame.grid(row=0, column=0)
service_frame= tk.LabelFrame(window, text = "Other Service")
service_frame.grid(row=0, column=1, sticky="NSEW")
cleaning_frame= tk.LabelFrame(window, text= "Cleaning Services")
cleaning_frame.grid(row=1, column=0, sticky= "NSEW")
charge_frame= tk.LabelFrame(window, text= "Charge Information")
charge_frame.grid(row=1, column=1, sticky= "NSEW")
today_order_frame= tk.LabelFrame(window, text= "Today's Order")
today_order_frame.grid(row=0, column=2, rowspan=3, sticky= "NSEW" )
button_frame= tk.Frame(window)
button_frame.grid(row=2, column= 0,columnspan= 3)

customer_label= tk.Label(customer_frame, text= "Plate Number")
customer_label.grid(row=0, column= 0)
name_label= tk.Label(customer_frame, text= "Name")
name_label.grid(row=1, column=0)
address_label= tk.Label(customer_frame, text= "Address")
address_label.grid(row=2,column=0)
city_label= tk.Label(customer_frame, text= "City")
city_label.grid(row=3, column=0)
phone_label= tk.Label(customer_frame, text= "Phone")
phone_label.grid(row=4, column=0)

plate_entry= tk.Entry(customer_frame, textvariable= input_plate)
plate_entry.grid(row=0, column=1)
name_entry= tk.Entry(customer_frame, textvariable= input_name)
name_entry.grid(row=1, column=1)
address_entry= tk.Entry(customer_frame,textvariable= input_address )
address_entry.grid(row=2, column=1)
city_entry= tk.Entry(customer_frame, textvariable= input_city)
city_entry.grid(row=3, column=1)
phone_entry= tk.Entry(customer_frame, textvariable= input_phone)
phone_entry.grid(row=4, column=1)

service_label= tk.Label(service_frame, text= "grease, Oil and Filter (GOF)")
service_label.grid(row=0, column=1)
service_check_button= tk.Checkbutton(service_frame)
service_check_button.grid(row=0, column=0)
service_label= tk.Label(service_frame, text= "Rust Roofing Service")
service_label.grid(row=1, column=1)
service_check_button= tk.Checkbutton(service_frame)
service_check_button.grid(row=1, column=0)
service_label= tk.Label(service_frame, text= "Tire change and Balance")
service_label.grid(row= 2, column=1)
service_check_button= tk.Checkbutton(service_frame)
service_check_button.grid(row=2 , column=0)

#package_frame= tk.LabelFrame(cleaning_frame, text= "Cleaning Service")
#package_frame.grid(row=0, column=0)
package_label= tk.Label(cleaning_frame, text= "Package")
package_label.grid(row=0, column=0)

options = dict()
package_option_label = ttk.Combobox(cleaning_frame,values=[ 'None','Standard','Deluxe','Executive'])
package_option_label.grid(row=0, column= 1)

package_option_var=tk.StringVar()
package_option_var.set(package_option_list[0])
package_option_var.om= tk.optionMenu(self, self.v, *package_option_var)

listbox= tk.Listbox(cleaning_frame, state= "disable")
listbox.grid(row=1, column=1)

fragrance_label= tk.Label(cleaning_frame, text= "Fragrance", state= "disable")
fragrance_label.grid(row=2, column=0)
fragrance_entry= tk.Entry(cleaning_frame, state= "disable")
fragrance_entry.grid(row=2, column=1)

charge_label= tk.Label(charge_frame)
charge_label.grid(row=0, column=0, columnspan=4)
charge_listbox= tk.Listbox(charge_frame, width=45, height=13, state= "disable")
charge_listbox.grid(row=1, column=0,sticky="NSEW")

today_order_listbox= tk.Listbox(today_order_frame, width=45, height=24)
today_order_listbox.grid(row=2, columnspan=4, sticky="NSEW")

dropdown_label= tk.Label(cleaning_frame)
dropdown_label.grid()

def delect_command():
    listbox.delete(ANCHOR)

def add_command():
    name= customer_entry.get()
    name1 = name_entry.get()
    name2 = address_entry.get()
    name3 = phone_entry.get()
    name4 = service_entry.get()
    name5 = package_entry.get()

def save_command():
    file_name = Simpledialog.askstring(save_dialog = "please enter a file name")
    if file_name == None:
        return
    f= open(file_name, "w")
    for entry in listbox.get(0, END):
        f.write(entry + "\n")
    f.close()

def exit_command():
    os.sys.exit(0)

add_button = tk.Button(button_frame, text= "Calculate", command= add_command)
add_button.grid(row= 0, column= 0, padx= 20, pady=10)
save_button= tk.Button(button_frame, text= "Save Service", command= save_command)
save_button.grid(row= 0, column=1,padx= 20, pady=10)
delect_button= tk.Button(button_frame, text= "Clear Service", command= delect_command)
delect_button.grid(row=0, column=2,padx= 20, pady=10)
exit_button= tk.Button(button_frame, text= "Exit", command= exit_command)
exit_button.grid(row=0, column=3,padx= 20, pady=10 )


window.mainloop()