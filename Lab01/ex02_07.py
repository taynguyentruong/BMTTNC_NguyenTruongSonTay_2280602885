print("nhập các dòng văn bản ( nhập done để KT):")
lines = []
while True:
    line = input()
    if line.lower() == 'done':
        break
    lines.append(line)
print("\n các dòng đã nhập sau khi chuyển thành chữ in hoa:")
for line in lines:
    print(line.upper())