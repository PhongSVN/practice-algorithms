# Giải thích: Đơn giản là chia bài toán ra thành nhiều phần nhỏ,
# những phần max_trai và max phải là chỉ số lớn nhất trong từng bên
# và được so sánh với max giữa( tổng)

def left(arr, dau, cuoi):
    max = arr[cuoi]
    sum = 0
    for i in range(cuoi, dau - 1, -1):
        sum += arr[i]
        if sum > max:
            max = sum
    return max


def right(arr, dau, cuoi):
    max = arr[dau]
    sum = 0
    for i in range(dau, cuoi + 1):
        sum += arr[i]
        if sum > max:
            max = sum
    return max


def DevideAndConquer(arr, dau, cuoi):
    if (dau == cuoi):
        return arr[dau]
    mid = (dau + cuoi) // 2
    max_trai = DevideAndConquer(arr, 0, mid)
    max_phai = DevideAndConquer(arr, mid + 1, cuoi)
    max_giua = left(arr, 0, mid) + right(arr, mid + 1, cuoi)
    return max(max_giua, max(max_trai, max_phai))


input_str = input("Nhập các số cách nhau bởi dấu cách: ")
arr = list(map(int, input_str.split()))
max_sum = DevideAndConquer(arr, 0, len(arr) - 1)
print("Tổng của chuỗi con lớn nhất là: " + str(max_sum))
