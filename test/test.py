# @author JL
# @date 2023/6/30 13:10
import os

path = "DJI_20230629111905_0036_V.JPG"
print(os.path.splitext(path))


inpath = "C:\\Users\Jin\Desktop\DJI_202306291110_014_农田二维建模-丁家塘001-航点手动设置4-副本"
file_name = "test.jpg"
print(os.path.join(inpath, file_name))