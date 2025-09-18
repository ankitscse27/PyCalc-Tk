# Modern Scientific Calculator

A feature-rich, modern scientific calculator built with Python's native GUI toolkit, Tkinter. This project enhances a standard calculator with scientific functions, an intuitive user interface, and a secure evaluation engine.



## ✨ Features

-   **Standard Arithmetic**: Perform addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
-   **Scientific Operations**:
    -   Square Root (`√`)
    -   Square (`x²`)
    -   Parentheses for grouping (`()`) with smart multiplication (e.g., `5(2+3)` is treated as `5*(2+3)`).
    -   Constants like Pi (`π`).
-   **User-Friendly Interface**:
    -   A clean, dark-themed UI inspired by modern calculator apps.
    -   Large, readable display with separate views for the ongoing calculation and the current number.
    -   Responsive layout that scales with the window size.
    -   Hover effects on buttons for better visual feedback.
-   **Enhanced Functionality**:
    -   **Backspace (`⌫`)**: Easily correct input errors.
    -   **Clear (`C`)**: Reset the entire calculation.
    -   **Sign Toggle (`+/-`)**: Change the sign of the current number.
-   **Keyboard Support**: Use your keyboard for faster calculations. All numbers, operators, `Enter` (for equals), and `Backspace` are mapped.
-   **Secure & Robust**: Uses a controlled `eval()` environment to prevent arbitrary code execution, ensuring that only safe, defined mathematical operations are performed.

---

## 🚀 How to Run

No external libraries are needed! All you need is a standard Python 3 installation.

### Prerequisites

-   Python 3.x

### Steps

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/modern-scientific-calculator.git](https://github.com/your-username/modern-scientific-calculator.git)
    cd modern-scientific-calculator
    ```

2.  **Run the Python script:**
    ```bash
    python scientific_calculator.py
    ```
    The calculator window will appear, ready for you to use!

---

## 🏛️ Code Overview

The entire application is encapsulated within the `ScientificCalculator` class, making the code organized and easy to understand.

### Key Components

-   **Constants**: At the top of the file, styling variables (colors, fonts) are defined for easy customization and consistency.
-   `__init__(self, master)`: The constructor initializes the main window, sets up variables, and calls the helper methods to build the GUI.
-   **Widget Creation (`_create_*` methods)**:
    -   `_create_display_frame()` and `_create_buttons_frame()`: Set up the main containers for the screen and the buttons.
    -   `_create_display_labels()`: Creates the two labels for the total expression and current input.
    -   `_create_buttons()`: Iterates through a dictionary of button layouts and creates each button widget.
-   **Core Logic**:
    -   `add_to_expression(self, value)`: Appends digits or symbols to the current input string. It includes logic to auto-insert a `*` before an opening parenthesis.
    -   `add_operator(self, operator)`: Moves the current number and the selected operator to the total expression line.
    -   `evaluate(self)`: The heart of the calculator. It constructs the final expression and uses a **safe evaluation method** to compute the result.
-   **Safe Evaluation**:
    -   To prevent security risks associated with the standard `eval()` function, the calculator provides `eval()` with a restricted environment.
    -   The `self.allowed_names` dictionary explicitly defines which functions (`sqrt`, `log10`, etc.) and constants (`pi`, `e`) are accessible. This ensures that only mathematical operations can be executed.
-   **Event Handling**:
    -   `_bind_keys(self)`: Maps keyboard presses (e.g., `'1'`, `'+'`, `<Return>`) to the corresponding calculator functions.
    -   Button `command`s are linked to their respective methods (`self.clear`, `self.evaluate`, etc.).

---

## 🔮 Future Enhancements

This project has a solid foundation that can be extended with even more features:

-   [ ] **Calculation History**: A panel or dropdown to view and reuse previous calculations.
-   [ ] **Themes**: A toggle switch for Light and Dark modes.
-   [ ] **Advanced Scientific Functions**: Add trigonometric functions (sin, cos, tan), logarithms (ln), and factorials (!).
-   [ ] **Unit Conversions**: A separate mode for converting between common units (e.g., cm to inches, kg to lbs).

---

## 🤝 Contributing

Contributions are welcome! If you have an idea for a new feature or want to improve the existing code, feel free to fork the repository, make your changes, and submit a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the `LICENSE` file for details.
