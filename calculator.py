
import tkinter as tk
window = tk.Tk()
window.title("Simple Calculator")
window.geometry("350x350")

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        op = operation.get()

        if op == "+":
            result = num1 + num2
        elif op == "-":
            result = num1 - num2
        elif op == "*":
            result = num1 * num2
        elif op == "/":
            if num2 == 0:
                result_label.config(text="Cannot divide by zero!")
                return
            result = num1 / num2

        result_label.config(text="Result: " + str(result))

    except ValueError:
        result_label.config(text="Enter valid numbers!")

tk.Label(
    window, text="Simple Calculator",
    font=("Arial", 18, "bold")
).pack(pady=10)

tk.Label(window, text="Enter first number:").pack()
entry1 = tk.Entry(window)
entry1.pack(pady=5)

tk.Label(window, text="Enter second number:").pack()
entry2 = tk.Entry(window)
entry2.pack(pady=5)

tk.Label(window, text="Select operation").pack()
operation = tk.StringVar(value="+")
tk.OptionMenu(
    window, operation, "+", "-", "*", "/"
).pack(pady=5)

tk.Button(
    window, text="Calculate",
    command=calculate
).pack(pady=10)

result_label = tk.Label(
    window, text="Result: ",
    font=("Arial", 12, "bold")
)
result_label.pack(pady=5)
window.mainloop()