import os

file_list = os.listdir("./data")

for file_name in file_list:
    os.system("./bin/main.out {} | tee ./out/{}.log".format(file_name, file_name))
