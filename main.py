# main.py

import operations
import input_handler

def main():
    print("="*30)
    print("  ỨNG DỤNG MÁY TÍNH ĐƠN GIẢN  ")
    print("="*30)
    
    while True:
        # Nhập dữ liệu
        num1 = input_handler.get_number("Nhập số thứ nhất: ")
        operator = input_handler.get_operator()
        num2 = input_handler.get_number("Nhập số thứ hai: ")

        # Thực hiện phép tính dựa trên toán tử
        if operator == '+':
            result = operations.add(num1, num2)
        elif operator == '-':
            result = operations.subtract(num1, num2)
        elif operator == '*':
            result = operations.multiply(num1, num2)
        elif operator == '/':
            result = operations.divide(num1, num2)

