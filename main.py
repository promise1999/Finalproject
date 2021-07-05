import tkinter as tk
window = tk.Tk()
window.title("Shopping Month")
label = tk.Label(window, text="Please enter your name in the text box below")
label.grid(row=0, column=0)
text = tk.Entry(window)
text.grid(row=1, column=0)
button = tk.Button(window, text="Generate greeting")
button.grid(row=2, column=0)
label1 = tk
window.mainloop()