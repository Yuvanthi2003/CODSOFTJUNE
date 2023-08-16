import tkinter as tk

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()
        if operation == "+":
            result.set(num1 + num2)
        elif operation == "-":
            result.set(num1 - num2)
        elif operation == "*":
            result.set(num1 * num2)
        elif operation == "/":
            result.set(num1 / num2)
    except:
        result.set("Error")

root = tk.Tk()
root.title("Simple Calculator")

label_num1 = tk.Label(root, text="Number 1:")
label_num1.grid(row=0, column=0)

entry_num1 = tk.Entry(root)
entry_num1.grid(row=0, column=1)

operation_var = tk.StringVar()
operation_choices = ["+", "-", "*", "/"]
operation_var.set("+")
operation_menu = tk.OptionMenu(root, operation_var, *operation_choices)
operation_menu.grid(row=0, column=2)

label_num2 = tk.Label(root, text="Number 2:")
label_num2.grid(row=1, column=0)

entry_num2 = tk.Entry(root)
entry_num2.grid(row=1, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=2, column=0, columnspan=3)

result = tk.StringVar()
result_label = tk.Label(root, textvariable=result)
result_label.grid(row=3, column=0, columnspan=3)

root.mainloop()
