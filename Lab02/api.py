from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher  
from cipher.vigenere import VigenereCipher    # Thêm vào phần đầu của file api.py
from cipher.railfence import RailFenceCipher  # Then vào phàn đâu của file api.py
from cipher.playfair import PlayFairCipher
from cipher.transposition import TranspositionCipher
app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])  
def caesar_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route("/api/caesar/decrypt", methods=["POST"])  # Fixed: changed {} to [] for methods
def caesar_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)
    return jsonify({'decrypted_message': decrypted_text})
#VIGENERE CIPHER ALGORITHM
vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

#RAILFENCE_CIPHER ALGORITHM
railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def decrypt():
    data = request.json
    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})
# PLAYFAIR CIPHER ALGORITHM
playfair_cipher = PlayFairCipher()

@app.route('/api/playfair/creatematrix', methods=['POST'])
def playfair_creatematrix():
    data = request.json
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    return jsonify({"playfair_matrix": playfair_matrix})

@app.route('/api/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.json
    plain_text = data['plain_text']
    key = data['key']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, playfair_matrix)
    return jsonify({'encrypted_text': encrypted_text})

@app.route('/api/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.json
    key = data['key']
    cipher_text = data['cipher_text']
    playfair_matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, playfair_matrix)
    return jsonify({'decrypted_text': decrypted_text})
# TRANSPOSITION CIPHER ALGORITHM
transposition_cipher = TranspositionCipher()

@app.route('/api/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    plain_text = data.get('plain_text')
    key = int(data.get('key'))
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return jsonify({"encrypted_text": encrypted_text})

@app.route('/api/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    cipher_text = data.get('cipher_text')
    key = int(data.get('key'))
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return jsonify({'decrypted_text': decrypted_text})

from flask import Flask, render_template, request, json
from cipher.caesar import CaesarCipher

app = Flask(__name__)

caesar_cipher = CaesarCipher()
playfair_cipher = PlayFairCipher()
railfence_cipher = RailFenceCipher()
transposition_cipher = TranspositionCipher()
vigenere_cipher = VigenereCipher() # Khởi tạo đối tượng VigenereCipher

# --- Routes cho trang chủ ---
@app.route("/")
def home():
    """Render trang chủ."""
    return render_template('index.html')

# --- Routes cho Caesar Cipher ---
@app.route("/caesar")
def caesar():
    """Render trang Caesar Cipher."""
    return render_template('caesar.html')

@app.route("/caesar/encrypt", methods=['POST']) # Đã đổi action thành /caesar/encrypt
def caesar_encrypt():
    """Xử lý yêu cầu mã hóa Caesar."""
    text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = caesar_cipher.encrypt_text(text, key)
    # Trả về kết quả dưới dạng HTML đơn giản hoặc chuyển hướng đến trang hiển thị kết quả
    return f"<h3>Kết quả mã hóa Caesar:</h3><p>Văn bản gốc: {text}</p><p>Khóa: {key}</p><p>Văn bản đã mã hóa: {encrypted_text}</p><a href='/caesar'>Quay lại</a>"

@app.route("/caesar/decrypt", methods=['POST']) # Đã đổi action thành /caesar/decrypt
def caesar_decrypt():
    """Xử lý yêu cầu giải mã Caesar."""
    text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = caesar_cipher.decrypt_text(text, key)
    # Trả về kết quả dưới dạng HTML đơn giản hoặc chuyển hướng đến trang hiển thị kết quả
    return f"<h3>Kết quả giải mã Caesar:</h3><p>Văn bản mã hóa: {text}</p><p>Khóa: {key}</p><p>Văn bản đã giải mã: {decrypted_text}</p><a href='/caesar'>Quay lại</a>"

# --- Routes cho Playfair Cipher ---
@app.route("/playfair")
def playfair():
    """Render trang Playfair Cipher."""
    return render_template('playfair.html')

@app.route("/playfair/encrypt", methods=['POST'])
def playfair_encrypt():
    """Xử lý yêu cầu mã hóa Playfair."""
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    # Tạo ma trận Playfair trước khi mã hóa
    matrix = playfair_cipher.create_playfair_matrix(key)
    encrypted_text = playfair_cipher.playfair_encrypt(plain_text, matrix)
    return f"<h3>Kết quả mã hóa Playfair:</h3><p>Văn bản gốc: {plain_text}</p><p>Khóa: {key}</p><p>Văn bản đã mã hóa: {encrypted_text}</p><a href='/playfair'>Quay lại</a>"

@app.route("/playfair/decrypt", methods=['POST'])
def playfair_decrypt():
    """Xử lý yêu cầu giải mã Playfair."""
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    # Tạo ma trận Playfair trước khi giải mã
    matrix = playfair_cipher.create_playfair_matrix(key)
    decrypted_text = playfair_cipher.playfair_decrypt(cipher_text, matrix)
    return f"<h3>Kết quả giải mã Playfair:</h3><p>Văn bản mã hóa: {cipher_text}</p><p>Khóa: {key}</p><p>Văn bản đã giải mã: {decrypted_text}</p><a href='/playfair'>Quay lại</a>"

# --- Routes cho Rail Fence Cipher ---
@app.route("/railfence")
def railfence():
    """Render trang Rail Fence Cipher."""
    return render_template('railfence.html')

@app.route("/railfence/encrypt", methods=['POST'])
def railfence_encrypt():
    """Xử lý yêu cầu mã hóa Rail Fence."""
    plain_text = request.form['inputPlainText']
    num_rails = int(request.form['inputKeyPlain'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, num_rails)
    return f"<h3>Kết quả mã hóa Rail Fence:</h3><p>Văn bản gốc: {plain_text}</p><p>Số hàng (Khóa): {num_rails}</p><p>Văn bản đã mã hóa: {encrypted_text}</p><a href='/railfence'>Quay lại</a>"

@app.route("/railfence/decrypt", methods=['POST'])
def railfence_decrypt():
    """Xử lý yêu cầu giải mã Rail Fence."""
    cipher_text = request.form['inputCipherText']
    num_rails = int(request.form['inputKeyCipher'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(cipher_text, num_rails)
    return f"<h3>Kết quả giải mã Rail Fence:</h3><p>Văn bản mã hóa: {cipher_text}</p><p>Số hàng (Khóa): {num_rails}</p><p>Văn bản đã giải mã: {decrypted_text}</p><a href='/railfence'>Quay lại</a>"

# --- Routes cho Transposition Cipher ---
@app.route("/transposition")
def transposition():
    """Render trang Transposition Cipher."""
    return render_template('transposition.html')

@app.route("/transposition/encrypt", methods=['POST'])
def transposition_encrypt():
    """Xử lý yêu cầu mã hóa Transposition."""
    plain_text = request.form['inputPlainText']
    key = int(request.form['inputKeyPlain'])
    encrypted_text = transposition_cipher.encrypt(plain_text, key)
    return f"<h3>Kết quả mã hóa Transposition:</h3><p>Văn bản gốc: {plain_text}</p><p>Khóa: {key}</p><p>Văn bản đã mã hóa: {encrypted_text}</p><a href='/transposition'>Quay lại</a>"

@app.route("/transposition/decrypt", methods=['POST'])
def transposition_decrypt():
    """Xử lý yêu cầu giải mã Transposition."""
    cipher_text = request.form['inputCipherText']
    key = int(request.form['inputKeyCipher'])
    decrypted_text = transposition_cipher.decrypt(cipher_text, key)
    return f"<h3>Kết quả giải mã Transposition:</h3><p>Văn bản mã hóa: {cipher_text}</p><p>Khóa: {key}</p><p>Văn bản đã giải mã: {decrypted_text}</p><a href='/transposition'>Quay lại</a>"

# --- Routes cho Vigenere Cipher ---
@app.route("/vigenere")
def vigenere():
    """Render trang Vigenere Cipher."""
    return render_template('vigenere.html')

@app.route("/vigenere/encrypt", methods=['POST'])
def vigenere_encrypt():
    """Xử lý yêu cầu mã hóa Vigenere."""
    plain_text = request.form['inputPlainText']
    key = request.form['inputKeyPlain']
    # Giả định phương thức mã hóa là encrypt_text
    encrypted_text = vigenere_cipher.encrypt_text(plain_text, key)
    return f"<h3>Kết quả mã hóa Vigenere:</h3><p>Văn bản gốc: {plain_text}</p><p>Khóa: {key}</p><p>Văn bản đã mã hóa: {encrypted_text}</p><a href='/vigenere'>Quay lại</a>"

@app.route("/vigenere/decrypt", methods=['POST'])
def vigenere_decrypt():
    """Xử lý yêu cầu giải mã Vigenere."""
    cipher_text = request.form['inputCipherText']
    key = request.form['inputKeyCipher']
    # Giả định phương thức giải mã là decrypt_text
    decrypted_text = vigenere_cipher.decrypt_text(cipher_text, key)
    return f"<h3>Kết quả giải mã Vigenere:</h3><p>Văn bản mã hóa: {cipher_text}</p><p>Khóa: {key}</p><p>Văn bản đã giải mã: {decrypted_text}</p><a href='/vigenere'>Quay lại</a>"


# main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)