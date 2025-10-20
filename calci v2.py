import tkinter as tk
import math

# --- Enhanced Constants for Styling (Modern Dark Theme) ---
# Deep Dark Theme Palette
DEEP_DARK = "#1a1a2e"       # Background
DARK_MID = "#2c3957"        # Button background (Digits/Constants)
DARK_LIGHT = "#415a77"      # Button background (Operators)
ACCENT_GREEN = "#a6e3a1"    # Scientific/Special Operators
ACCENT_BLUE = "#7aa2f7"     # Function/Clear Operators
ORANGE_EQ = "#ff79c6"       # Equals Button
WHITE_TEXT = "#f8f8f2"      # Main Text Color
LIGHT_TEXT = "#abb2bf"      # Secondary Text Color

# Font styles (Using 'Consolas' or 'Courier New' for a modern, code-like feel if available)
FONT_FAMILY = "Consolas"
LARGE_FONT_SIZE = 48
MEDIUM_FONT_SIZE = 24
SMALL_FONT_SIZE = 14

# Styles for different button types
STYLE_DIGIT = (DARK_MID, WHITE_TEXT, MEDIUM_FONT_SIZE, DARK_LIGHT)
STYLE_OPERATOR = (DARK_LIGHT, WHITE_TEXT, MEDIUM_FONT_SIZE, DARK_MID)
STYLE_SCIENTIFIC = (ACCENT_GREEN, DEEP_DARK, SMALL_FONT_SIZE, ACCENT_GREEN) # Text is Deep Dark on hover
STYLE_FUNCTION = (ACCENT_BLUE, WHITE_TEXT, MEDIUM_FONT_SIZE, DARK_LIGHT)
STYLE_EQUALS = (ORANGE_EQ, WHITE_TEXT, LARGE_FONT_SIZE // 2, "#ff559f")


class ScientificCalculator:
    """
    A comprehensive scientific calculator built with Tkinter, featuring a modern UI,
    advanced mathematical functions, and a secure evaluation engine.
    """

    def __init__(self, master):
        """Initialize the calculator and its GUI components."""
        self.master = master
        master.title("Scientific Calculator")
        master.geometry("500x700")  # Wider for more columns
        master.configure(bg=DEEP_DARK)

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

        # Define the button layout (6 rows, 5 columns)
        # Format: 'Text': (row, col, colspan, style_tuple, key_binding_text)
        self.buttons = {
            'C': (1, 0, 1, STYLE_FUNCTION, 'c'), '⌫': (1, 1, 1, STYLE_FUNCTION, 'BackSpace'), '()': (1, 2, 1, STYLE_OPERATOR, None), 
            '/': (1, 3, 1, STYLE_OPERATOR, '/'), '*': (1, 4, 1, STYLE_OPERATOR, '*'),

            '7': (2, 0, 1, STYLE_DIGIT, '7'), '8': (2, 1, 1, STYLE_DIGIT, '8'), '9': (2, 2, 1, STYLE_DIGIT, '9'), 
            '-': (2, 3, 1, STYLE_OPERATOR, '-'), '+': (2, 4, 1, STYLE_OPERATOR, '+'),

            '4': (3, 0, 1, STYLE_DIGIT, '4'), '5': (3, 1, 1, STYLE_DIGIT, '5'), '6': (3, 2, 1, STYLE_DIGIT, '6'), 
            'x²': (3, 3, 1, STYLE_SCIENTIFIC, '^'), '√': (3, 4, 1, STYLE_SCIENTIFIC, None),

            '1': (4, 0, 1, STYLE_DIGIT, '1'), '2': (4, 1, 1, STYLE_DIGIT, '2'), '3': (4, 2, 1, STYLE_DIGIT, '3'),
            'sin': (4, 3, 1, STYLE_SCIENTIFIC, None), 'cos': (4, 4, 1, STYLE_SCIENTIFIC, None),

            '+/-': (5, 0, 1, STYLE_DIGIT, None), '0': (5, 1, 1, STYLE_DIGIT, '0'), '.': (5, 2, 1, STYLE_DIGIT, '.'),
            'tan': (5, 3, 1, STYLE_SCIENTIFIC, None), 'log': (5, 4, 1, STYLE_SCIENTIFIC, None),

            'π': (6, 0, 1, STYLE_DIGIT, None), 'e': (6, 1, 1, STYLE_DIGIT, None), 
            '=': (6, 2, 3, STYLE_EQUALS, 'Return'), # = spans 3 columns
        }
        self._create_buttons()
        self._bind_keys()
    
    # --- UI Setup Methods ---

    def _configure_grid(self):
        """Configure the grid to be responsive."""
        self.master.rowconfigure(0, weight=2)   # Display frame
        self.master.rowconfigure(1, weight=5)   # Buttons frame
        self.master.columnconfigure(0, weight=1)

        # Configure button frame grid for 6 rows and 5 columns
        for i in range(1, 7): 
            self.buttons_frame.rowconfigure(i, weight=1)
        for i in range(5):
            self.buttons_frame.columnconfigure(i, weight=1)

    def _create_display_frame(self):
        """Create the frame that holds the display labels."""
        frame = tk.Frame(self.master, bg=DEEP_DARK)
        frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
        return frame

    def _create_buttons_frame(self):
        """Create the frame that holds the calculator buttons."""
        frame = tk.Frame(self.master, bg=DEEP_DARK)
        frame.grid(row=1, column=0, sticky="nsew")
        return frame

    def _create_display_labels(self):
        """Create the labels for showing expressions and results."""
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=DEEP_DARK, fg=LIGHT_TEXT, padx=15, font=(FONT_FAMILY, SMALL_FONT_SIZE))
        total_label.pack(expand=True, fill='both')

        # 'justify=tk.RIGHT' ensures text stays right-aligned if it wraps (less common in a calculator)
        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, justify=tk.RIGHT,
                         bg=DEEP_DARK, fg=WHITE_TEXT, padx=15, font=(FONT_FAMILY, LARGE_FONT_SIZE), wraplength=480)
        label.pack(expand=True, fill='both')
        return total_label, label

    def _create_buttons(self):
        """Create and place all calculator buttons based on the defined layout."""
        for btn_text, grid_info in self.buttons.items():
            row, col, colspan, style_tuple, _ = grid_info
            self._add_button(btn_text, row, col, colspan, style_tuple)

    def _add_button(self, text, row, col, colspan, style_tuple):
        """Helper method to create a single button."""
        bg_color, fg_color, font_size, hover_color = style_tuple
        font_style = (FONT_FAMILY, font_size, "bold") if font_size > MEDIUM_FONT_SIZE else (FONT_FAMILY, font_size)

        command = self._get_command(text)
        
        button = tk.Button(self.buttons_frame, text=text, bg=bg_color, fg=fg_color,
                           font=font_style, borderwidth=0, command=command, highlightthickness=0)
        button.grid(row=row, column=col, columnspan=colspan, sticky="nsew", padx=1, pady=1)

        # Add a slightly different hover effect for the scientific buttons
        # The scientific buttons have a hover_color equal to their bg_color, but they change fg_color
        if style_tuple == STYLE_SCIENTIFIC:
             button.bind("<Enter>", lambda event, h_color=ACCENT_GREEN, f_color=WHITE_TEXT: event.widget.config(bg=h_color, fg=DEEP_DARK))
             button.bind("<Leave>", lambda event, b_color=bg_color, f_color=DEEP_DARK: event.widget.config(bg=b_color, fg=WHITE_TEXT))
        else:
             button.bind("<Enter>", lambda event, h_color=hover_color: event.widget.config(bg=h_color))
             button.bind("<Leave>", lambda event, b_color=bg_color: event.widget.config(bg=b_color))


    # --- Command and Key Binding Methods ---

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
            return lambda: self.add_function('sqrt(')
        elif text == 'log':
            return lambda: self.add_function('log10(')
        elif text == 'sin':
            return lambda: self.add_function('sin(')
        elif text == 'cos':
            return lambda: self.add_function('cos(')
        elif text == 'tan':
            return lambda: self.add_function('tan(')
        elif text == 'e':
            return lambda: self.add_to_expression('e')
        else: # Digits, π, .
            return lambda: self.add_to_expression(text)

    def _bind_keys(self):
        """Bind keyboard keys to calculator functions."""
        # Use the key binding text from the button definitions for cleaner binding
        for _, grid_info in self.buttons.items():
            _, _, _, _, key_binding_text = grid_info
            if key_binding_text:
                if key_binding_text in '0123456789.':
                    self.master.bind(key_binding_text, lambda event, digit=key_binding_text: self.add_to_expression(digit))
                elif key_binding_text in '+-*/':
                    self.master.bind(key_binding_text, lambda event, op=key_binding_text: self.add_operator(op))
                elif key_binding_text == '^':
                    self.master.bind(key_binding_text, lambda event: self.add_operator("**"))
                elif key_binding_text == 'c':
                    self.master.bind(key_binding_text, lambda event: self.clear())
                    self.master.bind('C', lambda event: self.clear()) # Bind Capital C too
                elif key_binding_text == 'Return':
                    self.master.bind('<Return>', lambda event: self.evaluate())
                elif key_binding_text == 'BackSpace':
                    self.master.bind('<BackSpace>', lambda event: self.backspace())

        # Also bind parentheses keys explicitly
        self.master.bind("(", lambda event: self.add_to_expression("("))
        self.master.bind(")", lambda event: self.add_to_expression(")"))

    # --- Core Calculator Logic ---

    def add_to_expression(self, value):
        """Append a value (digit, '.', 'π', 'e') to the current expression, with smart multiplication."""
        # Smart multiplication for expressions like 5(3+1) or 5π
        if (value == "(" and self.current_expression and self.current_expression[-1].isdigit()):
            self.current_expression += "*"
        
        # Smart multiplication for expressions like )3 or π3
        elif value.isdigit() and self.current_expression and self.current_expression[-1] in ")πe":
            self.current_expression += "*"

        # Check for 'π' or 'e' next to a digit (e.g., 5π)
        if value in "πe" and self.current_expression and self.current_expression[-1].isdigit():
             self.current_expression += "*"

        self.current_expression += str(value)
        self.update_label()

    def add_function(self, function_str):
        """Adds a function (like sqrt(, sin() to the expression."""
        # Smart multiplication if adding a function after a number (e.g., 5sin(30))
        if self.current_expression and self.current_expression[-1].isdigit() and not function_str.startswith('('):
            self.current_expression += "*"
        
        self.current_expression += function_str
        self.update_label()

    def add_operator(self, operator):
        """Handle adding binary operators to the expression."""
        if self.current_expression or self.total_expression:
            if not self.current_expression and self.total_expression:
                # Allows changing the operator at the end of total_expression, e.g., 5+ becomes 5-
                # Check for functions like 'sqrt(' before replacing the last character
                if self.total_expression[-1] in "+-*/":
                    self.total_expression = self.total_expression[:-1] + operator
                # If it's not a simple operator, we don't allow changing it easily (e.g., '5sqrt' should not become '5-')
                elif self.current_expression:
                    self.total_expression += self.current_expression + operator
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
            try:
                # Try to find the last number/parentheses block to negate
                if self.current_expression.endswith(')'):
                    # Simple case: wrap with -()
                    # Need more robust parsing for advanced cases, but for simple number/result negation:
                    if self.current_expression.startswith('-(') and self.current_expression.endswith(')'):
                        self.current_expression = self.current_expression[2:-1] # Remove -()
                    else:
                        self.current_expression = f"-({self.current_expression})"
                elif self.current_expression.startswith('-'):
                    self.current_expression = self.current_expression[1:]
                else:
                    self.current_expression = '-' + self.current_expression
                self.update_label()
            except:
                pass # Do nothing if complex expression is being built

    def square(self):
        """Square the current number/expression."""
        if self.current_expression:
            # Wrap in parentheses to ensure correct order of operations (e.g., -5 squared is 25)
            self.current_expression = f"({self.current_expression})**2"
            self.update_label()

    def handle_parentheses(self):
        """Smartly adds opening or closing parentheses."""
        open_paren = self.current_expression.count("(")
        close_paren = self.current_expression.count(")")
        
        # Check if we should close the current parenthesis
        if open_paren > close_paren and self.current_expression and self.current_expression[-1] not in "+-*/(":
            self.add_to_expression(")")
        
        # Otherwise, add an opening parenthesis
        else:
            # If the last character is a digit or ')' or 'π', automatically add multiplication before '('
            if self.current_expression and self.current_expression[-1] in "0123456789)πe":
                self.add_to_expression("*(")
            else:
                self.add_to_expression("(")


    def evaluate(self):
        """Evaluate the full expression and show the result."""
        full_expression = self.total_expression + self.current_expression
        if not full_expression:
            return

        # Ensure all open parentheses are closed for eval to work
        open_paren_count = full_expression.count('(')
        close_paren_count = full_expression.count(')')
        if open_paren_count > close_paren_count:
            full_expression += ')' * (open_paren_count - close_paren_count)

        try:
            # Replace user-friendly symbols with Python-compatible ones
            expression_to_eval = full_expression.replace('π', 'pi').replace('log', 'log10') # log is now log10

            # Use a controlled eval for security
            result = eval(expression_to_eval, {"__builtins__": {}}, self.allowed_names)

            # Format result to remove unnecessary .0 and limit precision
            if isinstance(result, (int, float)):
                if abs(result) < 1e15: # Avoid sci-notation for large integers
                    if result == int(result):
                        result = int(result)
                    else:
                         # Round to 10 decimal places for clean display
                         result = round(result, 10)
                
            self.current_expression = str(result)
            self.total_expression = full_expression + " = "

        except Exception as e:
            # print(f"Error: {e}") # For debugging
            self.current_expression = "Error"
            self.total_expression = ""
        finally:
            self.update_label()
            self.update_total_label()

    # --- Display Update Methods ---

    def update_total_label(self):
        """Update the top display label (expression history)."""
        self.total_label.config(text=self.total_expression)

    def update_label(self):
        """Update the main display label (current entry/result)."""
        # Truncate for display if it's getting too long
        display_text = self.current_expression
        if len(display_text) > 20 and len(display_text.splitlines()) < 2: 
             display_text = display_text[:20] + "..."
             
        self.label.config(text=display_text)


# --- Main Execution --- 
if __name__ == "__main__":
    window = tk.Tk()
    calculator = ScientificCalculator(window)
    window.mainloop()