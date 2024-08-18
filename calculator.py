import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("352x473")
        self.root.resizable(False, False)  # Disable window resizing

        self.root.iconbitmap("icon.ico")
        self.root.configure(bg="#202020")

        # Set up the GUI
        self.create_widgets()

    def create_widgets(self):
        # Display field
        self.display = tk.Entry(self.root, font=("Arial", 20), borderwidth=5, relief="flat", justify='right', fg="#FFFFFF", bg='#202020')
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Buttons layout
        button_texts = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]

        row_val = 1
        col_val = 0

        for text in button_texts:
            if text in ['/', '*', '-', '+', '=']:
                button_color = "#0793FF"  # Blue for operators
            else:
                button_color = "#3B3B3B"  # Grey for numbers

            button = tk.Button(
                self.root, text=text, font=("Arial", 18), bg=button_color, fg="white", 
                command=lambda t=text: self.on_button_click(t), borderwidth=0
            )
            button.grid(row=row_val, column=col_val, padx=5, pady=5, sticky="nsew")

            # Make buttons round by using same height and width, with appropriate padding
            button.config(height=2, width=5)  # Adjust these numbers to make the buttons round

            # Adding a custom style for a round button
            button.configure(
                relief="flat",
                highlightthickness=2,
                highlightbackground=self.root.cget('bg'),
                highlightcolor=self.root.cget('bg')
            )

            col_val += 1
            if col_val > 3:
                col_val = 0
                row_val += 1

        # Clear button
        clear_button = tk.Button(
            self.root, text='C', font=("Arial", 18), bg="#07edda", fg="white",
            command=self.clear_display, borderwidth=0, height=2, width=5
        )
        clear_button.grid(row=5, column=0, padx=5, pady=5, sticky="nsew")

    def on_button_click(self, char):
        if char == '=':
            try:
                result = str(eval(self.display.get()))
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, result)
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
        else:
            current_text = self.display.get()
            self.display.delete(0, tk.END)
            self.display.insert(tk.END, current_text + char)

    def clear_display(self):
        self.display.delete(0, tk.END)

# Create the main window and run the app
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
