# Đoạn code được phân tích
i = 0
while (i < n):  # Vòng lặp 1: i tăng 100 mỗi lần
    # Số lần lặp của vòng lặp 1: n / 100
    while (a < n):  # Vòng lặp 2: a tăng 1 mỗi lần
        # Số lần lặp của vòng lặp 2: n (phụ thuộc vào n)
        while (b < n):  # Vòng lặp 3: b tăng 1 mỗi lần
            # Số lần lặp của vòng lặp 3: n (phụ thuộc vào n)
            b = b + 1  # Độ phức tạp của vòng lặp 3: O(n)
        a = a + 1  # Độ phức tạp của vòng lặp 2: O(n^2) (n lần lặp vòng lặp 3)
    
    while (c < n):  # Vòng lặp 4: c tăng 1 mỗi lần
        # Số lần lặp của vòng lặp 4: n (phụ thuộc vào n)
        c = c + 1  # Độ phức tạp của vòng lặp 4: O(n)
    
    i = i + 100  # Vòng lặp 1 tăng i lên 100 mỗi lần

# Phân tích tổng quát:
# 1.Xác định số lần lặp và cách chúng phụ thuộc vào kích thước đầu vào:
# Vòng lặp 1 (while (i < n)): n / 100 lần
# Vòng lặp 2 (while (a < n)) và vòng lặp 3 (while (b < n)): n^2 lần
# Vòng lặp 4 (while (c < n)): n lần

# 2.Phân tích cách gọi đệ quy và cơ sở dừng:
# Không sử dụng đệ quy trong đoạn code này
# Cơ sở dừng:
#   - Vòng lặp 1 dừng khi i = n
#   - Vòng lặp 2 dừng khi a = n
#   - Vòng lặp 3 dừng khi b = n
#   - Vòng lặp 4 dừng khi c = n

# 3.Đánh giá độ phức tạp của từng thao tác và cách chúng kết hợp:
# Khởi tạo i = 0: Độ phức tạp của các thao tác khởi tạo là O(1)
# Vòng lặp 1 chỉ có độ phức tạp O(n)
# Vòng lặp 2 và vòng lặp 3 lồng nhau nên độ phức tạp là O(n^2)
# Vòng lặp 4 chỉ có độ phức tạp O(n)
# F(n) = O(n) * O(n^2) + O(n)

# Độ phức tạp thời gian chạy tổng quát là O(n^3)

