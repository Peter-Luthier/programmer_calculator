from PyQt6.QtWidgets import QPushButton

class CustomRoundButton(QPushButton):
    def __init__(self, text: str, click_action, stylesheet_path: str, value: int and str=None, parent=None):
        super().__init__(text, parent)
        self.value = value  # Assign the numerical value to the button

        self.load_stylesheet(stylesheet_path)

        if click_action:
            self.clicked.connect(lambda: click_action(self.text))
        else:
            self.clicked.connect(self.default_click_action)

    def default_click_action(self):
        print(f'button {self.text} action')

    def load_stylesheet(self, stylesheet_path: str):
        try:
            with open(stylesheet_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"Stylesheet not found: {stylesheet_path}")
            self.set_default_style(30)

    def set_default_style(self, size: int):
        self.setStyleSheet(f"""
            QPushButton {{
                border-radius: {size // 2}px;
                background-color: #3498db;
                color: white;
                border: 2px solid #2980b9;
                font-size: 16px;
            }}
            QPushButton:hover {{
                background-color: #2980b9;
            }}
            QPushButton:pressed {{
                background-color: #1abc9c;
            }}
        """)

    def set_disabled(self, threshold: int):
        if self.value >= threshold:
            self.setDisabled(True)
        else:
            self.setDisabled(False)

    def update_stylesheet(self, stylesheet_path: str):
        """Dynamically update the button's stylesheet."""
        try:
            with open(stylesheet_path, "r") as file:
                stylesheet = file.read()
                self.setStyleSheet(stylesheet)
        except FileNotFoundError:
            print(f"Stylesheet not found: {stylesheet_path}")
