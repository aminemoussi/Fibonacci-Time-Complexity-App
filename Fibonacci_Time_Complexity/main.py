import tkinter as tk
from tkinter import messagebox
import subprocess

c_executable = "Dull_Fibonacci_time_complexity\\Fibonacci_stats\\main.c"
plot_executable = "Dull_Fibonacci_time_complexity\\fibonacci_exec_time\\graph_plot.py"



def fibonacci_data():
    target = input_entry.get()

    if (not target.isdigit()) or (int(target) < 0):
        messagebox.showerror("Error", "Please enter a positive number.")

    try:
        subprocess.run([c_executable, target], check = True)
        messagebox.showinfo("Success", f"Fibonacci data for {target} generated successfully!")

    except Exception as e:
        messagebox.showerror("Error", f"Failed to run Fibonacci calculation: {str(e)}")
        return


window = tk.Tk()
window.configure(bg = "#1c1d1d")
window.title("Fibonacci Time Complexity")
window.geometry("1200x600")

input_label = tk.Label(window, text = "Enter the last element of the Fibonacci Sequence: ")
input_label.pack(pady=10)


input_entry = tk.Entry(window)
input_entry.pack(pady=5)

run_button = tk.Button(window, text = "Generate Time Complxty Curve", command=fibonacci_data)
run_button.pack(pady=10)





window.mainloop()