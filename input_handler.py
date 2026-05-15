# input_handler.py

def get_number(prompt):
    """Yêu cầu người dùng nhập một số và xử lý lỗi nếu nhập sai."""
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Lỗi: Dữ liệu không hợp lệ. Vui lòng nhập một số.")

def get_operator():
    """Yêu cầu người dùng nhập một trong 4 phép toán cơ bản."""
    valid_operators = ['+', '-', '*', '/']
    while True:
        op = input("Nhập phép tính (+, -, *, /): ")
        if op in valid_operators:
            return op
        print("Lỗi: Phép tính không hợp lệ. Vui lòng thử lại.")