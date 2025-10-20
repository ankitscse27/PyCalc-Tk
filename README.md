# ⚛️ PyCalc-Tk: Modern Scientific Calculator

A feature-rich, modern scientific calculator built with Python's native GUI toolkit, **Tkinter**. This project transforms a standard arithmetic tool into a powerful scientific instrument, featuring an intuitive, dark-themed user interface and a secure computation engine.

---

## ✨ Features at a Glance

This application provides a blend of basic and advanced functions in a clean, high-contrast environment.

### 🧮 Core Functionality

-   **Standard Arithmetic**: Seamlessly perform addition (`+`), subtraction (`-`), multiplication (`*`), and division (`/`).
-   **Scientific Operations**: Access to essential mathematical functions:
    -   **Square Root** (`√`)
    -   **Square** (`x²`)
    -   **Trigonometry**: Sine, Cosine, and Tangent (if implemented in the code).
    -   **Logarithms**: Base 10 Log (`log10`).
-   **Mathematical Constants**: Directly use Pi (`π`) and Euler's number (`e`).
-   **Input Handling**:
    -   **Parentheses** (`()`) for complex grouping.
    -   **Smart Multiplication**: Automatically inserts a `*` operator (e.g., `5(2+3)` is correctly parsed as `5 * (2+3)`).

### 🖥️ User Experience (UX)

-   **Modern Dark Theme**: A clean, high-contrast UI inspired by contemporary developer tools and mobile calculator apps.
-   **Dual Display**: A large, readable screen with separate lines for:
    1.  **Ongoing Calculation** (history/total expression).
    2.  **Current Input/Result** (main display).
-   **Responsive Layout**: The grid-based interface scales gracefully to match the window size.
-   **Visual Feedback**: **Hover effects** on all buttons provide excellent visual confirmation of interaction.

### 🛠️ Enhanced Controls

-   **Backspace** (`⌫`): Effortlessly correct the last entered character.
-   **Clear** (`C`): Instantly reset the entire calculator state.
-   **Sign Toggle** (`+/-`): Quickly change the sign of the current number (negation).
-   **Full Keyboard Support**: Use your keyboard for maximum speed. All digits, operators, **Enter** (for equals), and **Backspace** are mapped.

---

## 🔒 Secure & Robust Evaluation

The calculator prioritizes security and stability:

-   It employs a **controlled environment** for the Python `eval()` function.
-   The **`self.allowed_names`** dictionary is the only namespace passed to `eval()`, meaning only explicitly defined, safe mathematical operations (`math.sqrt`, `math.pi`, etc.) can be executed.
-   This design **prevents** any arbitrary or malicious Python code execution, making the application safe for general use.

---

## 🚀 How to Run PyCalc-Tk

No external packages are required! You only need a standard installation of **Python 3.x** to run the application.

### Prerequisites

-   Python 3.x (with Tkinter included, which is standard)

### Quick Start Steps

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/ankitscse27/PyCalc-Tk.git](https://github.com/ankitscse27/PyCalc-Tk.git)
    cd PyCalc-Tk
    ```

2.  **Execute the Script:**
    ```bash
    python calci.py
    ```

    The Scientific Calculator window will appear, ready for use!

---

## 🏛️ Code Structure

The entire application logic and GUI build process are contained within the well-organized **`ScientificCalculator`** class.

| Component | Description |
| :--- | :--- |
| **Constants** | Defines the dark theme's color palette, font families, and sizes for easy global styling changes. |
| **`__init__`** | Initializes the Tkinter window, expression state variables, and the secure **`self.allowed_names`** dictionary. |
| **`_create_*` Methods** | Handles the structural setup: frames, labels for the dual display, and the iterative creation of all grid-based buttons. |
| **`_get_command`** | Acts as a central command router, linking each button's text to its corresponding Python method (e.g., `'='` maps to `self.evaluate`). |
| **`add_to_expression`** | Core input function. Includes specific logic to handle number/parentheses juxtaposition (smart multiplication). |
| **`evaluate`** | The culmination of the calculation. Prepares the full expression, sanitizes symbols (e.g., replaces `'π'` with `'pi'`), and safely executes the computation. |
| **`_bind_keys`** | Maps physical keyboard events (e.g., pressing `+` or `Enter`) to the internal calculator functions for desktop-friendly operation. |

---

## 💡 Future Enhancements

The modular design allows for exciting future development:

-   [ ] **Full Calculation History**: Implement a scrollable panel to view and recall previous results.
-   [ ] **Themes & Customization**: Add a toggle for Light/Dark mode and allow users to select accent colors.
-   [ ] **Advanced Functions**: Integrate hyperbolic functions, natural logarithm (`ln`), and factorials (`!`).
-   [ ] **Scientific Notation**: Improve display logic for very large or very small results using E notation.

---

## 🤝 Contributing

We welcome all contributions! Whether it's reporting a bug, suggesting a new feature, or submitting code improvements, please feel free to:

1.  **Fork** the repository.
2.  Create your feature branch (`git checkout -b feature/AmazingFeature`).
3.  Commit your changes (`git commit -m 'Add some AmazingFeature'`).
4.  Push to the branch (`git push origin feature/AmazingFeature`).
5.  Open a **Pull Request**.

---

## 📜 License

This project is licensed under the **MIT License**. See the `LICENSE` file in the repository for full details.
