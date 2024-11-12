# data = []
def pp2(arr):
    # data.append("Thành phần của mảng " + str(arr))
    max = arr[1]
    for i in range(len(arr)):
        sum = 0
        for j in range(i, len(arr)):
            # data.append("Chỉ số i = " + str(i) + " và chỉ số j = " + str(j))
            sum += arr[j]
            # data.append("Max hiện tại " + str(max))
            if sum>max:
                max = sum
                # data.append("Max hiện tại đã có sự biến đổi " + str(max))

    # data.append("Kết quả cuối cùng " + str(max))
    return max


input_str = input("Nhập các số cách nhau bởi dấu cách: ")
arr = list(map(int, input_str.split()))

print(pp2(arr))

# with open("2251068230_NguyenVanPhong.txt", "w", encoding="utf-8") as file:
#     file.writelines("\n".join(data))
