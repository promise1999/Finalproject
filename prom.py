import tkinter
import os
window = tkinter.Tk()
window.title("Space Age") #create window title

#generate a frame to organise my layout
input_frame= tkinter.LabelFrame(window, text= "Please Enter ")
input_frame.grid(row=0, column=0,pady=20,padx=20)
output_frame= tkinter.LabelFrame(window, text= "Payroll Results")
output_frame.grid(row=0, column=1,pady=20,padx=20, sticky="N", )
button_frame= tkinter.Frame(window)
button_frame.grid(row=1, column=0, columnspan=2)

# initializing input to hold data
monday_value= tkinter.StringVar()
tuesday_value= tkinter.StringVar()
wednesday_value= tkinter.StringVar()
thursday_value= tkinter.StringVar()
friday_value= tkinter.StringVar()

sales_val = tkinter.StringVar()
commission_val = tkinter.StringVar()
base_salary_val = tkinter.StringVar()
gross_val = tkinter.StringVar()
income_tax_val = tkinter.StringVar()
net_pay_val = tkinter.StringVar()

# initialize to hold and displayed data. using my label name
output_sales= tkinter.StringVar()
output_commission= tkinter.StringVar()
output_base_salary= tkinter.StringVar()
output_gross_pay= tkinter.StringVar()
output_income_tax= tkinter.StringVar()
output_net_pay= tkinter.StringVar()

def calculate_values():
    monday= float(monday_value.get())
    tuesday= float(tuesday_value.get())
    wednesday= float(wednesday_value.get())
    thursday= float(thursday_value.get())
    friday= float(friday_value.get())
    total_day= monday + tuesday + wednesday + thursday + friday

    total_sales = 0.15 * total_day
    commission = 0.15 * total_sales
    base_salary = 666
    gross_pay = commission + base_salary
    income_tax = 0.21 * gross_pay
    net_pay = gross_pay - income_tax

    output_sales.set("${:.2f}".format(total_sales))
    output_commission.set("${:.2f}".format(commission))
    output_base_salary.set("${:.2f}".format(base_salary))
    output_gross_pay.set("${:.2f}".format(gross_pay))
    output_income_tax.set("${:.2f}".format(income_tax))
    output_net_pay.set("${:.2f}".format(net_pay))

def clear_values():
    output_sales.set("")
    output_commission.set("")
    output_base_salary.set("")
    output_gross_pay.set("")
    output_income_tax.set("")
    output_net_pay.set("")
def exit_values():
    os.sys.exit(0)

employee_label= tkinter.Label(input_frame, text= "Employee number")
employee_label.grid(row=0, column=0)
employee_label1= tkinter.Label(input_frame, text= "Employee Name")
employee_label1.grid(row=1, column=0)
monday_label= tkinter.Label(input_frame, text= "Monday")
monday_label.grid(row=2, column=0)
tuesday_label= tkinter.Label(input_frame, text= "Tuesday")
tuesday_label.grid(row=3, column=0)
wednesday_label= tkinter.Label(input_frame, text= "Wednesday")
wednesday_label.grid(row=4, column=0)
thursday_label= tkinter.Label(input_frame, text= "Thursday")
thursday_label.grid(row=5, column=0)
friday_label= tkinter.Label(input_frame, text= "Friday")
friday_label.grid(row=6, column=0)

employee_entry=tkinter.Entry(input_frame)
employee_entry.grid(row=0, column=1)
employee_entry1=tkinter.Entry(input_frame)
employee_entry1.grid(row=1, column=1)
monday_entry=tkinter.Entry(input_frame, textvariable= monday_value)
monday_entry.grid(row=2, column=1)
tuesday_entry=tkinter.Entry(input_frame, textvariable= tuesday_value)
tuesday_entry.grid(row=3, column=1)
wednesday_entry=tkinter.Entry(input_frame,textvariable= wednesday_value )
wednesday_entry.grid(row=4, column=1)
thursday_entry=tkinter.Entry(input_frame, textvariable= thursday_value)
thursday_entry.grid(row=5, column=1)
friday_entry=tkinter.Entry(input_frame, textvariable= friday_value)
friday_entry.grid(row=6, column=1)

total_sales= tkinter.Label(output_frame, text= "Total sales:")
total_sales.grid(row=0, column=0)
commission=tkinter.Label(output_frame, text= "Commission:")
commission.grid(row=1, column=0)
base_salary= tkinter.Label(output_frame, text= "Base Salary:")
base_salary.grid(row=2, column=0)
gross_pay= tkinter.Label(output_frame, text= "Gross Pay:")
gross_pay.grid(row=3, column=0)
income_tax= tkinter.Label(output_frame, text="Income Tax:")
income_tax.grid(row=4, column=0)
net_pay= tkinter.Label(output_frame, text= "Net Pay:")
net_pay.grid(row=5, column=0)

sales_entry= tkinter.Entry(output_frame, textvariable= output_sales, state="disabled")
sales_entry.grid(row=0, column=1)
commission_entry= tkinter.Entry(output_frame,textvariable= output_commission, state="disabled")
commission_entry.grid(row=1, column=1)
base_entry= tkinter.Entry(output_frame, textvariable= output_base_salary, state="disabled")
base_entry.grid(row=2, column=1)
gross_entry= tkinter.Entry(output_frame, textvariable= output_gross_pay, state="disabled")
gross_entry.grid(row=3, column=1)
income_entry= tkinter.Entry(output_frame,textvariable= output_income_tax, state="disabled")
income_entry.grid(row=4, column=1)
net_entry= tkinter.Entry(output_frame,textvariable=output_net_pay, state="disabled")
net_entry.grid(row=5, column=1)

calculator =tkinter.Button(button_frame, text= "Calculate", command= calculate_values)
calculator.grid(row=0,column=0)
clear= tkinter.Button(button_frame, text= "Clear", command= clear_values)
clear.grid(row=0, column=1)
exit= tkinter.Button(button_frame, text= "Exit", command= exit_values)
exit.grid(row=0, column=2)


window.mainloop()

















