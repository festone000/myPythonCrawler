import os
import time

cur_path = os.getcwd()
cur_time = time.time()
tmp_file = cur_path + "/temp" + str(cur_time) + ".txt"


def save_str(txt_str):
    file = open(tmp_file, 'w+')
    file.write(txt_str)
    file.close()