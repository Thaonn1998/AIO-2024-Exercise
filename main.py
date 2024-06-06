# Print variable
var1 = 'str_var1'
var2 = 3
var3 = 15.5
print ('Print single variable ( var1 ): ', var1 )
print ( f'Print more than one variables : var1 ={ var1 } , var2 ={ var2 } , var3 ={ var3 }')


# Classification model
def classification_model(tp, fp, fn):

    # Kiểm tra kiểu dữ liệu
    if type(tp) is not int:
        print('tp must be int')
        return
    if type(fp) is not int:
        print('fp must be int')
        return
    if type(fn) is not int:
        print('fn must be int')
        return
    
    # Kiểm tra giá trị lớn hơn 0
    if tp <= 0:
        print('tp, fp, and fn must be greater than zero')
        return
    if fp <= 0:
        print('tp, fp, and fn must be greater than zero')
        return
    if fn <= 0:
        print('tp, fp, and fn must be greater than zero')
        return
    
    # Tính Precision, Recall, và F1-score
    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    f1_score = 2 * (precision * recall) / (precision + recall)
    
    # In kết quả
    print(f'Precision: {precision}')
    print(f'Recall: {recall}')
    print(f'F1-score: {f1_score}')

#Activation function
import math

def is_number(n): # Hàm is_number
    try:
        float(n)  # Type - casting the string to ‘float ‘.  If string is not a valid ‘float ‘ , it ’ll raise ‘ValueError ‘ exception
    except ValueError:
        return False
    return True

    
def sigmoid(x):
    return 1 / (1 + math.exp(-x))

def relu(x):
    return max(0, x)

def elu(x, alpha=0.01):
    return x if x >= 0 else alpha * (math.exp(x) - 1)

def exercise2():
    # Nhập giá trị x
    x = input("Input x: ")

    # Kiểm tra giá trị x có hợp lệ hay không
    if is_number(x) == False:
        print("x must be a number")
        return
    
    # Convert x sang float type
    x = float(x)

    # Nhập tên hàm 
    activation_function = input("Input activation function (sigmoid | relu | elu): ").lower()

    # Activation function name có hợp lệ hay không
    valid_functions = ['sigmoid', 'relu', 'elu']
    if activation_function in valid_functions == False:
        print(f"{activation_function} is not supported")
        return
    # In kết quả
    if activation_function == 'sigmoid':
        result = sigmoid(x)
    elif activation_function == 'relu':
        result = relu(x)
    elif activation_function == 'elu':
        result = elu(x)
    
    print(f"{activation_function}: f({x}) = {result}")

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

# 4 functions sin(x), cos(x), sinh(x), và cosh(x)

def approx_sin(x, n): #functions sin(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i + 1):
            term *= x / (j + 1)
        term *= (-1) ** i
        result += term
    return result

def approx_cos(x, n): #functions cos(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i):
            term *= x / (j + 1)
        term *= (-1) ** i
        result += term
    return result

def approx_sinh(x, n): #functions sinh(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i + 1):
            term *= x / (j + 1)
        result += term
    return result

def approx_cosh(x, n): #functions cosh(x)
    result = 0
    for i in range(n):
        term = 1
        for j in range(2 * i):
            term *= x / (j + 1)
        result += term
    return result

# Function Mean Difference of nth Root Error

def md_nre_single_sample(y, y_hat, n, p):
    # Tính căn bậc n của y và y_hat
    nth_root_y = y ** (1 / n)
    nth_root_y_hat = y_hat ** (1 / n)
    
    # Tính toán loss 
    loss = abs(nth_root_y - nth_root_y_hat) ** p
    
    return loss

if __name__ == "__main__":
    print('Exercise 1------------------------')
    classification_model(2, 3, 4)

    print('Exercise 2------------------------')
    exercise2()

    print('Exercise 3------------------------')
    exercise3()

    print('Exercise 4------------------------')
    print(approx_sin(x=3.14, n=10))
    print(approx_cos(x=3.14, n=10))
    print(approx_sinh(x=3.14, n=10))
    print(approx_cosh(x=3.14, n=10))
    
    print('Exercise 5------------------------')
    print(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))  
    print(md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))  
    print(md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))  
    print(md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))  


