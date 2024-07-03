import sys
from PySide6.QtCore import Qt
from PySide6.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox, QTabWidget


class Base10ToBinaryTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        dec_label = QLabel("Base10 Number: ")
        layout.addWidget(dec_label)

        self.dec_entry = QLineEdit()
        layout.addWidget(self.dec_entry)

        bin_label = QLabel("Binary Number: ")
        layout.addWidget(bin_label)

        self.bin_amount_label = QLabel("0")
        self.bin_amount_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.bin_amount_label.setCursor(Qt.PointingHandCursor)
        layout.addWidget(self.bin_amount_label)

        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.dec_to_bin)
        layout.addWidget(calc_button)

    def dec_to_bin(self):
        try:
            number = int(self.dec_entry.text())
            binary_str = bin(number)[2:]
            formatted_bin_str = binary_str.zfill(4)
            self.bin_amount_label.setText(formatted_bin_str)
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid base10 number with no decimal points.")


class BinaryToBase10Tab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        bin_label = QLabel("Binary Number: ")
        layout.addWidget(bin_label)

        self.bin_entry = QLineEdit()
        layout.addWidget(self.bin_entry)

        dec_label = QLabel("Base10 Number: ")
        layout.addWidget(dec_label)

        self.dec_amount_label = QLabel("0")
        self.dec_amount_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.dec_amount_label.setCursor(Qt.PointingHandCursor)
        layout.addWidget(self.dec_amount_label)

        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.bin_to_dec)
        layout.addWidget(calc_button)

    def bin_to_dec(self):
        try:
            binary_str = self.bin_entry.text()
            decimal_number = int(binary_str, 2)
            self.dec_amount_label.setText(str(decimal_number))
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid binary number.")


class BinaryAdditionTab(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.init_ui()

    def init_ui(self):
        layout = QVBoxLayout(self)

        bin1_layout = QHBoxLayout()  # Horizontal layout for the first binary number
        layout.addLayout(bin1_layout)

        bin1_label = QLabel("Binary Number 1: ")
        bin1_layout.addWidget(bin1_label)

        self.bin1_entry = QLineEdit()
        bin1_layout.addWidget(self.bin1_entry)

        plus_label = QLabel("+")
        layout.addWidget(plus_label)

        bin2_layout = QHBoxLayout()  # Horizontal layout for the second binary number
        layout.addLayout(bin2_layout)

        bin2_label = QLabel("Binary Number 2: ")
        bin2_layout.addWidget(bin2_label)

        self.bin2_entry = QLineEdit()
        bin2_layout.addWidget(self.bin2_entry)

        equals_label = QLabel("=")
        layout.addWidget(equals_label)

        self.bin_sum_label = QLabel("")
        self.bin_sum_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
        self.bin_sum_label.setCursor(Qt.PointingHandCursor)
        layout.addWidget(self.bin_sum_label)

        calc_button = QPushButton("Calculate")
        calc_button.clicked.connect(self.get_binary)
        layout.addWidget(calc_button)

    def get_binary(self):
        try:
            bin1 = self.bin1_entry.text()
            bin2 = self.bin2_entry.text()
            if not all(char in '01' for char in bin1) or not all(char in '01' for char in bin2):
                raise ValueError

            def add_binary(n1, n2):
                result = ""
                carry = 0
                max_len = max(len(n1), len(n2))
                a = n1.zfill(max_len)
                b = n2.zfill(max_len)
                for i in range(max_len - 1, -1, -1):
                    bit_sum = int(a[i]) + int(b[i]) + carry
                    result_bit = bit_sum % 2
                    carry = bit_sum // 2
                    result = str(result_bit) + result
                if carry:
                    result = "1" + result
                self.bin_sum_label.setText(result)

            add_binary(str(bin1), str(bin2))
        except ValueError:
            QMessageBox.critical(self, "Invalid Input", "Please enter a valid binary number.")


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.setWindowTitle("Binary Converter")
        self.setGeometry(100, 100, 350, 200)

        main_widget = QWidget()
        self.setCentralWidget(main_widget)
        layout = QVBoxLayout(main_widget)

        # Create a Notebook widget
        my_notebook = QTabWidget()
        layout.addWidget(my_notebook)

        # Create and add tabs
        tab1 = Base10ToBinaryTab()
        tab2 = BinaryToBase10Tab()
        tab3 = BinaryAdditionTab()

        my_notebook.addTab(tab1, "Base10 -> Binary")
        my_notebook.addTab(tab2, "Binary -> Base10")
        my_notebook.addTab(tab3, "Binary Addition")

        # Apply custom tab button colors using style sheets
        my_notebook.setStyleSheet(
            "QTabBar::tab:selected {background-color: DarkSlateGray;}"
        )


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec())
