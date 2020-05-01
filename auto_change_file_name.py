import os

count = 1

#需要批量修改的文件夹的位置
path_x = "C:\\Users\\herry\\Pictures\\Exibition"

for x in os.listdir(path_x):
	ending = os.path.splitext(x)[1]
	new_name = "image_" + str(count) + ending
	new_path = os.path.join(path_x, new_name)
	old_path = os.path.join(path_x, x)
	os.rename(old_path, new_path)
	count += 1
