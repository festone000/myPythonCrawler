import os
import time

def save_file(data):
    cur_path =os.getcwd()
    folder_path = cur_path + "/tmp"
    if os.path.exists(folder_path) == False:
        os.mkdir(folder_path)
    cur_time = time.time()

    save_path = folder_path + "/temp" + str(cur_time) + ".html"
    f_obj = open(save_path,'wb')
    f_obj.write(data)
    f_obj.close()