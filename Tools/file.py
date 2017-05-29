def save_file(data):
    save_path = "D:\\temp.out"
    f_obj = open(save_path,'wb')
    f_obj.write(data)
    f_obj.close()