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
    
if __name__ == "__main__":
    classification_model(2, 3, 4)

