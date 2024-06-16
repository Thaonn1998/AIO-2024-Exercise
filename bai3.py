def word_count(file_path):
    word_counts = {}

    # Đọc nội dung file
    with open("D:\AIO_2024\AIO-2024-Exercise\P1_data.txt", 'r') as file:
        text = file.read()
    
    # Chuyển nội dung thành chữ thường
    text = text.lower()
    
    # Tách nội dung thành các từ
    words = text.split()
    
    # Đếm số lần xuất hiện của mỗi từ
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    
    return word_counts

file_path = 'P1_data.txt'
print(word_count(file_path))
