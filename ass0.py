# Develop a tkinter gui that will allow the user to enter two numbers and then perform addition, subtraction, multiplication, and division on the two numbers. The user should be able to select which operation to perform by clicking on a button. The result should be displayed in a label. The user should be able to clear the entry fields and the result label by clicking on a button. The user should be able to exit the program by clicking on a button.

# Import tkinter
import tkinter as tk

# Create a class
class Calculator:
    # Create a constructor
    def __init__(self):
        # Create a window
        self.window = tk.Tk()
        self.window.geometry("400x200")
        # Set the title
        self.window.title("Two number Calculator")
        # Create a frame
        self.frame = tk.Frame(self.window)
        # Create a label
        self.label1 = tk.Label(self.frame, text = "Enter a number:")
        # Create a label
        self.label2 = tk.Label(self.frame, text = "Enter a number:")
        # Create a label
        self.label3 = tk.Label(self.frame, text = "Result:")
        # Create an entry
        self.entry1 = tk.Entry(self.frame)
        # Create an entry
        self.entry2 = tk.Entry(self.frame)
        # Create an entry
        self.entry3 = tk.Entry(self.frame)
        # Create a button
        self.button1 = tk.Button(self.frame, text = "Add", command = self.add)
        # Create a button
        self.button2 = tk.Button(self.frame, text = "Subtract", command = self.subtract)
        # Create a button
        self.button3 = tk.Button(self.frame, text = "Multiply", command = self.multiply)
        # Create a button
        self.button4 = tk.Button(self.frame, text = "Divide", command = self.divide)
        # Create a button
        self.button5 = tk.Button(self.frame, text = "Clear", command = self.clear)
        # Create a button
        self.button6 = tk.Button(self.frame, text = "Exit", command = self.exit)
        # Create a grid
        self.label1.grid(row = 0, column = 0)
        self.label2.grid(row = 1, column = 0)
        self.label3.grid(row = 2, column = 0)
        self.entry1.grid(row = 0, column = 1)
        self.entry2.grid(row = 1, column = 1)
        self.entry3.grid(row = 2, column = 1)
        self.button1.grid(row = 0, column = 2)
        self.button2.grid(row = 1, column = 2)
        self.button3.grid(row = 2, column = 2)
        self.button4.grid(row = 3, column = 2)
        self.button5.grid(row = 4, column = 2)
        self.button6.grid(row = 5, column = 2)
        # Create a grid
        self.frame.grid()
        # Create a main loop
        tk.mainloop()
    # Create a method
    def add(self):
        num1 = float(self.entry1.get())
        num2 = float(self.entry2.get())
        result = num1 + num2
        self.entry3.delete(0, tk.END)        
        self.entry3.insert(0, result)
    # Create a method
    def subtract(self):
        # Create a variable
        num1 = float(self.entry1.get())
        # Create a variable
        num2 = float(self.entry2.get())
        # Create a variable
        result = num1 - num2
        # Create a variable
        self.entry3.delete(0, tk.END)
        # Create a variable
        self.entry3.insert(0, result)
    # Create a method
    def multiply(self):
        # Create a variable
        num1 = float(self.entry1.get())
        # Create a variable
        num2 = float(self.entry2.get())
        # Create a variable
        result = num1 * num2
        # Create a variable
        self.entry3.delete(0, tk.END)
        # Create a variable
        self.entry3.insert(0, result)
    # Create a method
    def divide(self):
        # Create a variable
        num1 = float(self.entry1.get())
        # Create a variable
        num2 = float(self.entry2.get())
        # Create a variable
        result = num1 / num2
        # Create a variable
        self.entry3.delete(0, tk.END)
        # Create a variable
        self.entry3.insert(0, result)
    # Create a method
    def clear(self):
        # Create a variable
        self.entry1.delete(0, tk.END)
        # Create a variable
        self.entry2.delete(0, tk.END)
        # Create a variable
        self.entry3.delete(0, tk.END)
    # Create a method
    def exit(self):
        # Create a variable
        self.window.destroy()

#Main implementation
if __name__ == "__main__":
    # Create an object
    calc = Calculator()