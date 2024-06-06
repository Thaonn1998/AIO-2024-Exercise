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

if __name__ == "__main__":
    exercise2()
