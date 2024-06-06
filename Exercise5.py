# Function Mean Difference of nth Root Error
def md_nre_single_sample(y, y_hat, n, p):
    # Tính căn bậc n của y và y_hat
    nth_root_y = y ** (1 / n)
    nth_root_y_hat = y_hat ** (1 / n)
    
    # Tính toán loss 
    loss = abs(nth_root_y - nth_root_y_hat) ** p
    
    return loss

if __name__ == "__main__":
    print(md_nre_single_sample(y=100, y_hat=99.5, n=2, p=1))  
    print(md_nre_single_sample(y=50, y_hat=49.5, n=2, p=1))  
    print(md_nre_single_sample(y=20, y_hat=19.5, n=2, p=1))  
    print(md_nre_single_sample(y=0.6, y_hat=0.1, n=2, p=1))  