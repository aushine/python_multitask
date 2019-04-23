import os
import multiprocessing
import time
import random

'''多线程复制文件到新文件夹中'''


def copy_file(q, file_name, old_folder, new_folder):

    old_f = open(old_folder + "/" + file_name, 'rb')
    # 把旧文件的读取内容放在一个变量中
    content = old_f.read()
    # 把旧文件夹下的文件复制到新文件夹,名字是所有旧文件加上"[新]"
    new_f = open(new_folder + "/" + "[新]" + file_name, "wb")
    new_f.write(content)
    q.put(1)
    old_f.close()
    new_f.close()


def main():
    # 创建一个进程池
    po = multiprocessing.Pool(3)

    # 获得复制的路径,文件夹名
    old_folder_name = "M:/pythonCode/PythonNetProgramme"

    # 将该文件夹下所有文件名保存到一个列表当中 使用os.listdir()
    file_names = os.listdir(old_folder_name)

    # 创建一个队列储存复制文件的进度
    q = multiprocessing.Manager().Queue()

    # 复制所有除了文件夹外的文件,旧文件名开头加上"[新]"的文件夹中 os.mkdir()创建文件夹
    test = old_folder_name.split("/")
    test[-1] = "[新]" + test[-1]
    new_folder_name = "/".join(test)

    # new_folder_name = old_folder_name + "[新]"
    # 创建新文件夹
    os.mkdir(new_folder_name)

    # copy_file(file_names, old_folder_name, new_folder_name)  # 单线程版本
    # 多进程版
    # 读旧路径下的所有file_names的文件 ,使用os.isdir(name)或者isfile(name)判断一个文件是文件还是文件夹,是文件时才开始复制
    for file_name in file_names:
        if os.path.isdir(old_folder_name + "/" + file_name):
            # print("test")
            continue
        po.apply_async(copy_file, (q, file_name, old_folder_name, new_folder_name))
    po.close()
    # 显示进度:
    # 每次复制完一个文件就往队列put一个1, 从队列中取出所有元素储存到一个列表 rate_of_process 中
    # 进度的计算方法是, len(rate_of_process)*100 / len(file_names)
    rate_of_process = list()
    while True:
        rate_of_process.append(q.get())
        rate_process = len(rate_of_process) * 100 / len(file_names)
        print("\r %.1f %%" %rate_process, end="")
        time.sleep(random.uniform(0.0, 0.9))
        # 因为目录下有三个文件夹,修改功能太麻烦
        if len(rate_of_process) >= len(file_names)-3:
            print("\r100%", end="")
            print("\r \033[0;31m复制已完成")
            break


    # po.join()
if __name__ == "__main__":
    main()