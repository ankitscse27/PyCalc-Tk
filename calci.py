import tkinter as tk
import math

# --- Constants for Styling ---
# A modern, clean color palette
DARK_GRAY = "#282c34"
GRAY = "#3e4451"
LIGHT_GRAY = "#abb2bf"
WHITE = "#FFFFFF"
LABEL_COLOR = "#EAEAEA"
ORANGE = "#e06c75"
ORANGE_HOVER = "#e68e96"

# Font styles
LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
BUTTON_FONT_STYLE = ("Arial", 20, "bold")
DIGIT_FONT_STYLE = ("Arial", 20)


class ScientificCalculator:
    """
    A comprehensive scientific calculator built with Tkinter, featuring a modern UI,
    advanced mathematical functions, and a secure evaluation engine.
    """

    def __init__(self, master):
        """Initialize the calculator and its GUI components."""
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("400x680")
        master.configure(bg=DARK_GRAY)

        # Initialize expression strings
        self.total_expression = ""
        self.current_expression = ""

        # Allowed names for the safe evaluation
        self.allowed_names = {
            "math": math,
            "sqrt": math.sqrt,
            "log10": math.log10,
            "pi": math.pi,
            "e": math.e,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan
        }

        # Create frames for display and buttons
        self.display_frame = self._create_display_frame()
        self.buttons_frame = self._create_buttons_frame()

        # Configure grid layout
        self._configure_grid()

        # Create display labels
        self.total_label, self.label = self._create_display_labels()

        # Define the button layout
        self.buttons = {
            'C': (1, 0), '()': (1, 1), '√': (1, 2), '/': (1, 3),
            '7': (2, 0), '8': (2, 1), '9': (2, 2), '*': (2, 3),
            '4': (3, 0), '5': (3, 1), '6': (3, 2), '-': (3, 3),
            '1': (4, 0), '2': (4, 1), '3': (4, 2), '+': (4, 3),
            '0': (5, 0, 2), '.': (5, 2), '=': (5, 3),
            'π': (6, 0), 'x²': (6, 1), '+/-': (6, 2), '⌫': (6, 3)
        }
        self._create_buttons()
        self._bind_keys()

    def _configure_grid(self):
        """Configure the grid to be responsive."""
        self.master.rowconfigure(0, weight=2)  # Display frame
        self.master.rowconfigure(1, weight=5)  # Buttons frame
        self.master.columnconfigure(0, weight=1)

        for i in range(1, 7): # Adjusted for 6 rows of buttons
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(4):
            self.buttons_frame.columnconfigure(i, weight=1)

    def _create_display_frame(self):
        """Create the frame that holds the display labels."""
        frame = tk.Frame(self.master, bg=DARK_GRAY)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        return frame

    def _create_buttons_frame(self):
        """Create the frame that holds the calculator buttons."""
        frame = tk.Frame(self.master, bg=DARK_GRAY)
        frame.grid(row=1, column=0, sticky="nsew")
        return frame

    def _create_display_labels(self):
        """Create the labels for showing expressions and results."""
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=DARK_GRAY, fg=LIGHT_GRAY, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=DARK_GRAY, fg=WHITE, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')
        return total_label, label

    def _create_buttons(self):
        """Create and place all calculator buttons based on the defined layout."""
        for btn_text, grid_info in self.buttons.items():
            row, col = grid_info[0], grid_info[1]
            colspan = grid_info[2] if len(grid_info) > 2 else 1
            self._add_button(btn_text, row, col, colspan)

    def _add_button(self, text, row, col, colspan=1):
        """Helper method to create a single button."""
        # Determine button style based on its function
        if text.isdigit() or text == "." or text == "π":
            bg_color = GRAY
            hover_color = "#6a6a6a"
            font_style = DIGIT_FONT_STYLE
        elif text == "=":
            bg_color = ORANGE
            hover_color = ORANGE_HOVER
            font_style = BUTTON_FONT_STYLE
        else:
            bg_color = DARK_GRAY
            hover_color = GRAY
            font_style = BUTTON_FONT_STYLE

        # Define command based on button text
        command = self._get_command(text)

        button = tk.Button(self.buttons_frame, text=text, bg=bg_color, fg=WHITE,
                           font=font_style, borderwidth=0, command=command)
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)

        # Add hover effects
        button.bind("<Enter>", lambda event, h_color=hover_color: event.widget.config(bg=h_color))
        button.bind("<Leave>", lambda event, b_color=bg_color: event.widget.config(bg=b_color))

    def _get_command(self, text):
        """Returns the appropriate function for a button."""
        if text == "=":
            return self.evaluate
        elif text == "C":
            return self.clear
        elif text == "⌫":
            return self.backspace
        elif text == "()":
            return self.handle_parentheses
        elif text == "+/-":
            return self.toggle_sign
        elif text in "+-*/":
            return lambda: self.add_operator(text)
        elif text == 'x²':
            return self.square
        elif text == '√':
            return lambda: self.add_to_expression('sqrt(')
        else: # Digits, π, .
            return lambda: self.add_to_expression(text)

    def _bind_keys(self):
        """Bind keyboard keys to calculator functions."""
        self.master.bind("<Return>", lambda event: self.evaluate())
        self.master.bind("<BackSpace>", lambda event: self.backspace())
        for key in "1234567890.":
            self.master.bind(key, lambda event, digit=key: self.add_to_expression(digit))
        for key in "+-*/":
            self.master.bind(key, lambda event, operator=key: self.add_operator(operator))
        self.master.bind("c", lambda event: self.clear())
        self.master.bind("C", lambda event: self.clear())
        self.master.bind("(", lambda event: self.add_to_expression("("))
        self.master.bind(")", lambda event: self.add_to_expression(")"))
        self.master.bind("^", lambda event: self.add_operator("**"))

    def add_to_expression(self, value):
        """Append a value to the current expression, with smart multiplication."""
        if value == "(" and self.current_expression and self.current_expression[-1].isdigit():
            # Add multiplication operator for expressions like 5(3+1)
            self.current_expression += "*"
        self.current_expression += str(value)
        self.update_label()

    def add_operator(self, operator):
        """Handle adding operators to the expression."""
        if self.current_expression or self.total_expression:
            # If there's an ongoing expression, finalize it before adding the new operator
            if not self.current_expression and self.total_expression:
                 # Allows changing the operator, e.g., 5+ becomes 5-
                 self.total_expression = self.total_expression[:-1] + operator
            else:
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

    def backspace(self):
        """Remove the last character from the current expression."""
        self.current_expression = self.current_expression[:-1]
        self.update_label()
        
    def toggle_sign(self):
        """Toggle the sign of the current number."""
        if self.current_expression:
            if self.current_expression.startswith('-'):
                self.current_expression = self.current_expression[1:]
            else:
                self.current_expression = '-' + self.current_expression
            self.update_label()

    def square(self):
        """Square the current number."""
        if self.current_expression:
            self.current_expression = str(eval(f"{self.current_expression}**2"))
            self.update_label()

    def handle_parentheses(self):
        """Smartly adds opening or closing parentheses."""
        open_paren = self.current_expression.count("(")
        close_paren = self.current_expression.count(")")

        if self.current_expression and self.current_expression[-1] in "0123456789)":
            if open_paren > close_paren:
                self.add_to_expression(")")
            else:
                self.add_to_expression("*(")
        else:
            self.add_to_expression("(")

    def evaluate(self):
        """Evaluate the full expression and show the result."""
        full_expression = self.total_expression + self.current_expression
        if not full_expression:
            return

        try:
            # Replace user-friendly symbols with Python-compatible ones
            expression_to_eval = full_expression.replace('π', 'pi')
            
            # Use a controlled eval to prevent security risks
            result = eval(expression_to_eval, {"__builtins__": {}}, self.allowed_names)

            # Format result to remove unnecessary .0
            if result == int(result):
                result = int(result)

            self.current_expression = str(result)
            self.total_expression = ""
        except Exception:
            self.current_expression = "Error"
        finally:
            self.update_label()
            self.update_total_label()

    def update_total_label(self):
        """Update the top display label."""
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        """Update the main display label."""
        # Limit display length to avoid overflow
        self.label.config(text=self.current_expression[:11])


# --- Main Execution ---
if __name__ == "__main__":
    window = tk.Tk()
    calculator = ScientificCalculator(window)
    window.mainloop()
