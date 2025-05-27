class TranspositionCipher:
    def __init__(self):
        pass

    def encrypt(self, text, key):
        encrypted_text = ''
        for col in range(key):
            pointer = col
            while pointer < len(text):
                encrypted_text += text[pointer]
                pointer += key
        return encrypted_text

    def decrypt(self, text, key):
        # Khởi tạo danh sách để lưu trữ các ký tự đã giải mã
        # Kích thước của danh sách bằng với khóa, mỗi phần tử là một chuỗi rỗng
        decrypted_text = [''] * key
        row, col = 0, 0 # Khởi tạo hàng và cột

        # Lặp qua từng ký tự trong văn bản đã mã hóa
        for symbol in text:
            decrypted_text[col] += symbol # Thêm ký tự vào cột hiện tại
            col += 1 # Chuyển sang cột tiếp theo

            # Kiểm tra nếu đã đến cuối hàng hoặc đã đến cuối cột cuối cùng
            # và số hàng đã đi qua lớn hơn hoặc bằng số ký tự còn lại chia cho khóa
            if col == key or (col == key - 1 and row >= len(text) % key):
                col = 0 # Quay lại cột đầu tiên
                row += 1 # Chuyển sang hàng tiếp theo
        # Nối các chuỗi trong danh sách thành một chuỗi duy nhất và trả về
        return ''.join(decrypted_text)
