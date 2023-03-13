def solveKT(n):
    
    # Khởi tạo ma trận kết quả với tất cả các ô bằng -1
    sol = [[-1 for x in range(n)]for y in range(n)]
     
    # Khởi tạo các bước di chuyển trên bàn cờ
    xMove = [2, 1, -1, -2, -2, -1, 1, 2]
    yMove = [1, 2, 2, 1, -1, -2, -2, -1]
     
    # Đánh dấu ô đầu tiên là đã đi được
    sol[0][0] = 0
     
    # Bắt đầu tìm kiếm đường đi
    if(not solveKTUtil(0, 0, 1, sol, xMove, yMove)):
        print("Không có giải pháp")
    else:
        printSolution(sol)
         
# Hàm trợ giúp giải quyết vấn đề mã đi tuần
def solveKTUtil(x, y, movei, sol, xMove, yMove):
     
    if(movei == N**2):
        return True
     
    # Thử tất cả các bước tiếp theo từ ô hiện tại x, y
    for k in range(8):
        next_x = x + xMove[k]
        next_y = y + yMove[k]
        if(isSafe(next_x, next_y, sol)):
            sol[next_x][next_y] = movei
            if(solveKTUtil(next_x, next_y, movei+1, sol, xMove, yMove)):
                return True
             
            # Backtracking
            sol[next_x][next_y] = -1
    return False
     
# Kiểm tra xem (x, y) có phải là ô hợp lệ không
def isSafe(x, y, sol):
     
    return (x >= 0 and x < N and y >= 0 and y < N and sol[x][y] == -1)
     
# Hàm để in ra giải pháp
def printSolution(sol):
    for i in range(N):
        for j in range(N):
            print(sol[i][j],end =' ')
        print()
         
# Bắt đầu chương trình chính
if __name__ == "__main__":
     
    # Kích thước của bàn cờ
    N = 8
     
    # Gọi hàm để giải quyết vấn đề
    solveKT(N)
