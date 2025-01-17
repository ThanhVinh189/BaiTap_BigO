i = 0  # O(1)

# Vòng lặp while
while i < n:  # O(n)
    # Thao tác trong vòng lặp
    i = i + 1  # O(1)

# Phân tích tổng quát:
# 1.Xác định số lần lặp và cách chúng phụ thuộc vào kích thước đầu vào:
# Vòng lặp while (i < n): Vòng lặp này sẽ chạy khi giá trị của i nhỏ hơn n. Mỗi lần lặp, i được tăng lên 1
# Số lần lặp: Số lần vòng lặp sẽ là n (vì mỗi lần lặp i tăng lên 1 cho đến khi i = n).

# 2.Phân tích cách gọi đệ quy và cơ sở dừng:
# Không sử dụng đệ quy trong đoạn code này
# Cơ sở dừng: Vòng lặp sẽ dừng lại khi giá trị của i đạt đến n, vì vậy cơ sở dừng là khi i = n

# 3.Đánh giá độ phức tạp của từng thao tác và cách chúng kết hợp:
# Khởi tạo i = 0: có độ phức tạp là O(1) cho mỗi vòng lặp
# Vòng lặp while (i < n): Vòng lặp này sẽ chạy n lần
# Thao tác i = i + 1: có độ phức tạp là O(1) cho mỗi vòng lặp
# F(N) : 1 + 2n

# Độ phức tạp thời gian chạy tổng quát là O(n)