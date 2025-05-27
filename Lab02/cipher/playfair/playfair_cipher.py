class PlayFairCipher:
    def __init__(self) -> None:
        pass

    def create_playfair_matrix(self, key):
        key = key.replace("J", "I")  # Chuyển "J" thành "I" trong khóa
        key = key.upper()
        key_set = set(key)
        alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        remaining_letters = [
            letter for letter in alphabet if letter not in key_set
        ]
        matrix = list(key)

        for letter in remaining_letters:
            matrix.append(letter)
            if len(matrix) == 25:
                break
        playfair_matrix = [matrix[i:i+5] for i in range(0, len(matrix), 5)]
        return playfair_matrix

    def find_letter_coords(self, matrix, letter):
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                if matrix[row][col] == letter:
                    return row, col

    def playfair_encrypt(self, plain_text, matrix):
        # Chuyển "J" thành "I" trong văn bản đầu vào.
        plain_text = plain_text.replace("J", "I")
        plain_text = plain_text.upper()
        encrypted_text = ""

        for i in range(0, len(plain_text), 2):
            pair = plain_text[i:i+2]
            if len(pair) == 1:  # Xử lý nếu số lượng ký tự lẻ
                pair += "X" # Sửa lỗi: pair = "X" thành pair += "X"
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])
            if row1 == row2:
                encrypted_text += matrix[row1][(col1 + 1) % 5]
                encrypted_text += matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                encrypted_text += matrix[(row1 + 1) % 5][col1]
                encrypted_text += matrix[(row2 + 1) % 5][col2]
            else:
                encrypted_text += matrix[row1][col2] + matrix[row2][col1]
        return encrypted_text

    def playfair_decrypt(self, cipher_text, matrix):
        cipher_text = cipher_text.upper()
        decrypted_text = ""
        # decrypted_text1 = "" # Biến này không được sử dụng, có thể xóa

        for i in range(0, len(cipher_text), 2):
            pair = cipher_text[i:i+2]
            row1, col1 = self.find_letter_coords(matrix, pair[0])
            row2, col2 = self.find_letter_coords(matrix, pair[1])

            if row1 == row2:
                decrypted_text += matrix[row1][(col1 - 1) % 5]
                decrypted_text += matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += matrix[(row1 - 1) % 5][col1] # Sửa lỗi: thiếu dòng này
                decrypted_text += matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += matrix[row1][col2] + matrix[row2][col1]

        banro = ""
        # loại bỏ ký tự 'X' nếu nó là ký tự cuối cùng và là ký tự được thêm vào
        # Logic này có vẻ không hoàn chỉnh hoặc có lỗi. Cần xem xét lại mục đích của nó.
        # Hiện tại, nó chỉ xử lý các cặp ký tự và có thể bỏ sót ký tự cuối cùng.
        for i in range(0, len(decrypted_text) - 1, 2): # Sửa lỗi: len(decrypted_text) - 2 thành len(decrypted_text) - 1
            if i + 1 < len(decrypted_text): # Đảm bảo không vượt quá chỉ số
                if decrypted_text[i] == decrypted_text[i+1] and decrypted_text[i+1] == 'X': # Điều kiện loại bỏ 'X' giữa các ký tự trùng lặp
                    banro += decrypted_text[i]
                else:
                    banro += decrypted_text[i] + decrypted_text[i+1]
            else:
                banro += decrypted_text[i] # Xử lý ký tự cuối cùng nếu có

        # Logic xử lý ký tự cuối cùng có vẻ không chính xác.
        # Nếu decrypted_text[-1] là 'X' và nó được thêm vào, thì chỉ cần bỏ nó đi.
        # Nếu không, thì giữ nguyên.
        if decrypted_text and decrypted_text[-1] == "X" and len(decrypted_text) > 1 and decrypted_text[-2] == decrypted_text[-1]:
            # Đây là trường hợp 'X' được thêm vào cuối do văn bản gốc có độ dài lẻ hoặc lặp ký tự
            return banro[:-1] if banro and banro[-1] == 'X' else banro # Loại bỏ 'X' cuối cùng nếu nó là 'X' được thêm vào
        return banro
