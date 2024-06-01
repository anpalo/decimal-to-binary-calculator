import sys
from PyQt5.QtCore import Qt

from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QLineEdit, \
    QPushButton, QMessageBox, QTabWidget


def dec_to_bin():
    try:
        number = int(dec_entry.text())
        binary_str = bin(number)[2:]
        formatted_bin_str = binary_str.zfill(4)
        bin_amount_label.setText(formatted_bin_str)
    except ValueError:
        QMessageBox.critical(tab1, "Invalid Input", "Please enter a valid base10 number with no decimal points.")


def bin_to_dec():
    try:
        binary_str = bin_entry.text()
        decimal_number = int(binary_str, 2)
        dec_amount_label.setText(str(decimal_number))
    except ValueError:
        QMessageBox.critical(tab2, "Invalid Input", "Please enter a valid binary number.")


def get_binary():
    try:
        bin1 = bin1_entry.text()
        bin2 = bin2_entry.text()
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
            bin_sum_label.setText(result)
        add_binary(str(bin1), str(bin2))
    except ValueError:
        QMessageBox.critical(tab2, "Invalid Input", "Please enter a valid binary number.")


app = QApplication(sys.argv)
my_window = QMainWindow()
my_window.setWindowTitle("Binary Converter")
my_window.setGeometry(100, 100, 350, 200)

main_widget = QWidget()
my_window.setCentralWidget(main_widget)
layout = QVBoxLayout(main_widget)

# Create a Notebook widget
my_notebook = QTabWidget()
layout.addWidget(my_notebook)

# Create tabs
tab1 = QWidget()
tab2 = QWidget()
tab3 = QWidget()

# Add tabs to the notebook
my_notebook.addTab(tab1, "Base10 -> Binary")
my_notebook.addTab(tab2, "Binary -> Base10")
my_notebook.addTab(tab3, "Binary Addition")


# Base10 to Binary Tab
tab1_layout = QVBoxLayout(tab1)
dec_label = QLabel("Base10 Number: ")
tab1_layout.addWidget(dec_label)

dec_entry = QLineEdit()
tab1_layout.addWidget(dec_entry)

bin_label = QLabel("Binary Number:   ")
tab1_layout.addWidget(bin_label)

bin_amount_label = QLabel("0")
bin_amount_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
bin_amount_label.setCursor(Qt.PointingHandCursor)
tab1_layout.addWidget(bin_amount_label)

calc_button1 = QPushButton("Calculate")
calc_button1.clicked.connect(dec_to_bin)
tab1_layout.addWidget(calc_button1)

# Binary to Base10 Tab
tab2_layout = QVBoxLayout(tab2)
bin_label2 = QLabel("Binary Number: ")
tab2_layout.addWidget(bin_label2)

bin_entry = QLineEdit()
tab2_layout.addWidget(bin_entry)

dec_label2 = QLabel("Base10 Number:   ")
tab2_layout.addWidget(dec_label2)

dec_amount_label = QLabel("0")
dec_amount_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
dec_amount_label.setCursor(Qt.PointingHandCursor)
tab2_layout.addWidget(dec_amount_label)

calc_button2 = QPushButton("Calculate")
calc_button2.clicked.connect(bin_to_dec)
tab2_layout.addWidget(calc_button2)

# Binary Addition Tab
tab3_layout = QVBoxLayout(tab3)
bin1_layout = QHBoxLayout()  # Horizontal layout for the first binary number
tab3_layout.addLayout(bin1_layout)

bin1_label = QLabel("Binary Number 1: ")
bin1_layout.addWidget(bin1_label)

bin1_entry = QLineEdit()
bin1_layout.addWidget(bin1_entry)

plus_label = QLabel("+")
tab3_layout.addWidget(plus_label)

bin2_layout = QHBoxLayout()  # Horizontal layout for the second binary number
tab3_layout.addLayout(bin2_layout)

bin2_label = QLabel("Binary Number 2: ")
bin2_layout.addWidget(bin2_label)

bin2_entry = QLineEdit()
bin2_layout.addWidget(bin2_entry)

equals_label = QLabel("=")
tab3_layout.addWidget(equals_label)

bin_sum_label = QLabel("")
bin_sum_label.setTextInteractionFlags(Qt.TextSelectableByMouse)
bin_sum_label.setCursor(Qt.PointingHandCursor)
tab3_layout.addWidget(bin_sum_label)

calc_button3 = QPushButton("Calculate")
calc_button3.clicked.connect(get_binary)
tab3_layout.addWidget(calc_button3)


# Apply custom tab button colors using style sheets
my_notebook.setStyleSheet(
    "QTabBar::tab:selected {background-color: DarkSlateGray;} "
    # "QTabBar::tab:!selected {background-color: DarkSlateGray;}"
)

my_window.show()
sys.exit(app.exec_())
