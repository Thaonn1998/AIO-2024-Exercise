def levenshtein_distance(source, target):
    # Bước 1: Khởi tạo ma trận D với kích thước (M+1)x(N+1)
    M = len(source)
    N = len(target)
    D = [[0] * (N + 1) for _ in range(M + 1)]

    # Bước 2: Khởi tạo hàng và cột đầu tiên
    for i in range(M + 1):
        D[i][0] = i
    for j in range(N + 1):
        D[0][j] = j

    # Bước 3: Tính toán các giá trị cho các ô còn lại trong ma trận
    for i in range(1, M + 1):
        for j in range(1, N + 1):
            del_cost = D[i-1][j] + 1
            ins_cost = D[i][j-1] + 1
            if source[i-1] == target[j-1]:
                sub_cost = D[i-1][j-1]
            else:
                sub_cost = D[i-1][j-1] + 1
            D[i][j] = min(del_cost, ins_cost, sub_cost)

    # Bước 4: Trả về giá trị tại ô cuối cùng D[M][N]
    return D[M][N]

# Ví dụ
source = "yu"
target = "you"
print(levenshtein_distance(source, target))  

source = "kitten"
target = "sitting"
print(levenshtein_distance(source, target))  
