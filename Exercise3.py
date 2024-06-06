# Regression loss function
import random
import math

def is_number(n):
    return n.isnumeric()

def calculate_loss(num_samples, loss_name):
    # Chuyển đổi num_samples sang kiểu integer
    num_samples = int(num_samples)
    
    # Khởi tạo danh sách để lưu trữ predict, target và loss
    predicts = []
    targets = []
    losses = []
    
    # Dùng vòng lặp for để lặp lại num_samples lần
    for i in range(num_samples):
        predict = random.uniform(0, 10)
        target = random.uniform(0, 10)
        
        if loss_name == 'MAE' or loss_name == 'mae':
            loss = abs(predict - target)
        elif loss_name == 'MSE' or loss_name == 'mse':
            loss = (predict - target) ** 2
        elif loss_name == 'RMSE' or loss_name == 'rmse':
            loss = (predict - target) ** 2  
        
        predicts.append(predict)
        targets.append(target)
        losses.append(loss)
        
        # In kết quả mỗi sample
        print(f"loss name: {loss_name}, sample: {i}, pred: {predict}, target: {target}, loss: {loss}")
    
    # Tính tổng loss và in kết quả 
    total_loss = sum(losses)
    if loss_name == 'MAE' or loss_name == 'mae':
        final_loss = total_loss / num_samples
    elif loss_name == 'MSE' or loss_name == 'mse':
        final_loss = total_loss / num_samples
    elif loss_name == 'RMSE' or loss_name == 'rmse':
        final_loss = math.sqrt(total_loss / num_samples)
    
    print(f"final {loss_name}: {final_loss}")

def exercise3():
    # Nhập số lượng sample
    num_samples = input("Input number of samples (integer number) which are generated: ")
    
    # Kiểm tra số lượng sample
    if is_number(num_samples) == False:
        print("number of samples must be an integer number")
        return
    
    # Nhập tên loss function
    loss_name = input("Input loss name (MAE, MSE, RMSE): ")
    
    # Tính loss và in kết quả
    calculate_loss(num_samples, loss_name)

if __name__ == "__main__":
    exercise3()
