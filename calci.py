import tkinter as tk
import math

# --- Constants for Styling ---
# Using a modern, clean color palette
DARK_GRAY = "#333333"
LIGHT_GRAY = "#555555"
WHITE = "#FFFFFF"
LABEL_COLOR = "#EAEAEA"
ORANGE = "#FF9500"
ORANGE_HOVER = "#FFB347"

# Font styles
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
BUTTON_FONT_STYLE = ("Arial", 20, "bold")

class Calculator:
    """A comprehensive calculator class with a modern GUI."""

    def __init__(self, master):
        """Initialize the calculator."""
        self.master = master
        master.title("Advanced Calculator")
        master.geometry("375x667") # Common phone screen aspect ratio
        master.configure(bg=DARK_GRAY)

        # Initialize expression strings
        self.total_expression = ""
        self.current_expression = ""

        # Create display and button frames
        self.display_frame = self.create_display_frame()
        self.buttons_frame = self.create_buttons_frame()

        # Configure responsive layout
        self.configure_grid()

        # Create display labels
        self.total_label, self.label = self.create_display_labels()

        # Define the button layout
        self.buttons = {
            7: [('C', 1, 0), ('()', 1, 1), ('%', 1, 2), ('/', 1, 3)],
            8: [('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3)],
            9: [('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3)],
            10: [('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3)],
            11: [('0', 5, 0, 2), ('.', 5, 2), ('=', 5, 3)]
        }
        self.create_buttons()
        self.bind_keys()

    def configure_grid(self):
        """Configure the grid to be responsive."""
        self.master.rowconfigure(0, weight=2) # Display frame gets more space
        self.master.rowconfigure(1, weight=5) # Buttons frame gets more space
        self.master.columnconfigure(0, weight=1)

        for i in range(1, 6):
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)

    def create_display_frame(self):
        """Create the frame that holds the display labels."""
        frame = tk.Frame(self.master, bg=DARK_GRAY)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        return frame

    def create_buttons_frame(self):
        """Create the frame that holds the calculator buttons."""
        frame = tk.Frame(self.master, bg=DARK_GRAY)
        frame.grid(row=1, column=0, sticky="nsew")
        return frame

    def create_display_labels(self):
        """Create the labels for showing expressions and results."""
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=DARK_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=DARK_GRAY, fg=WHITE, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def create_buttons(self):
        """Create and place all calculator buttons."""
        for row_val, button_list in self.buttons.items():
            for btn_text, r, c, *span in button_list:
                colspan = span[0] if span else 1
                self.add_button(btn_text, r, c, colspan)

    def add_to_expression(self, value):
        """Append a value to the current expression."""
        self.current_expression += str(value)
        self.update_label()

    def add_operator(self, operator):
        """Handle adding operators to the expression."""
        if self.current_expression:
            # Append the operator and move the expression to the total line
            self.total_expression += self.current_expression + operator
            self.current_expression = ""
            self.update_total_label()
            self.update_label()

    def clear(self):
        """Clear both expression fields."""
        self.current_expression = ""
        self.total_expression = ""
        self.update_label()
        self.update_total_label()

    def evaluate(self):
        """Evaluate the full expression and show the result."""
        full_expression = self.total_expression + self.current_expression
        self.total_expression = full_expression
        try:
            # Replace percentage symbol for evaluation
            expression_to_eval = full_expression.replace('%', '/100')
            result = str(eval(expression_to_eval))
            self.current_expression = result
            self.total_expression = ""
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_label()
            self.update_total_label()

    def handle_parentheses(self):
        """Smartly adds opening or closing parentheses."""
        open_paren = self.current_expression.count("(")
        close_paren = self.current_expression.count(")")

        if self.current_expression == "" or self.current_expression[-1] in "(+-*/":
            self.add_to_expression("(")
        elif open_paren > close_paren:
            self.add_to_expression(")")
        else:
            self.add_to_expression("(")
        self.update_label()


    def add_button(self, text, row, col, colspan=1):
        """Helper method to create a single button."""
        # Determine button color based on its function
        if text.isdigit() or text == ".":
            bg_color = LIGHT_GRAY
            hover_color = "#6a6a6a"
        elif text == "=":
            bg_color = ORANGE
            hover_color = ORANGE_HOVER
        else:
            bg_color = DARK_GRAY
            hover_color = LIGHT_GRAY

        # Define command based on button text
        if text == "=":
            command = self.evaluate
        elif text == "C":
            command = self.clear
        elif text == "()":
            command = self.handle_parentheses
        elif text in "+-*/%":
            command = lambda: self.add_operator(text)
        else:
            command = lambda: self.add_to_expression(text)

        button = tk.Button(self.buttons_frame, text=text, bg=bg_color, fg=WHITE,
                           font=BUTTON_FONT_STYLE, borderwidth=0, command=command)
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)

        # Add hover effects
        button.bind("<Enter>", lambda event, h_color=hover_color: event.widget.config(bg=h_color))
        button.bind("<Leave>", lambda event, b_color=bg_color: event.widget.config(bg=b_color))


    def bind_keys(self):
        """Bind keyboard keys to calculator functions."""
        self.master.bind("<Return>", lambda event: self.evaluate())
        self.master.bind("<BackSpace>", lambda event: self.backspace())
        for key in "1234567890.":
            self.master.bind(key, lambda event, digit=key: self.add_to_expression(digit))
        for key in "+-*/%":
            self.master.bind(key, lambda event, operator=key: self.add_operator(operator))
        self.master.bind("c", lambda event: self.clear())
        self.master.bind("C", lambda event: self.clear())
        self.master.bind("(", lambda event: self.add_to_expression("("))
        self.master.bind(")", lambda event: self.add_to_expression(")"))


    def backspace(self):
        """Remove the last character from the current expression."""
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    def update_total_label(self):
        """Update the top display label."""
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        """Update the main display label."""
        self.label.config(text=self.current_expression[:11]) # Limit display length


# --- Main Execution ---
if __name__ == "__main__":
    window = tk.Tk()
    calculator = Calculator(window)
    window.mainloop()
