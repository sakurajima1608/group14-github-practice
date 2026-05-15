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

         # In kết quả
        print("-" * 30)
        print(f"Kết quả: {num1} {operator} {num2} = {result}")
        print("-" * 30)

        # Hỏi người dùng có muốn tiếp tục không
        cont = input("\nBạn có muốn tính tiếp không? (y/n): ").strip().lower()
        if cont != 'y':
            print("Cảm ơn bạn đã sử dụng chương trình. Tạm biệt!")
            break

        if __name__ == "__main__":
         main()


