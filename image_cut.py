# @author JL
# @date 2023/6/30 12:24
import os
import cv2

#   获取文件夹下某固定后缀的所有文件名
#   path     文件夹路径
#   suffix   后缀名，示例：".JPG"
def getFileName(path, suffix):

    file_names = []  # 文件名列表
    for root, dirs, files in os.walk(path, topdown=False):
        for name in files:
            if os.path.splitext(name)[1] == suffix:
                file_names.append(name)
                print(name)
    return file_names

#   图像裁剪
#   file_name        文件名(不含路径)
#   height_number    纵向切割份数
#   width_number     横向切割份数
def cut(file_name, height_number, width_number):
    file_path = os.path.join(inpath, file_name)  # 拼接绝对路径，inpath为全局变量
    img = cv2.imread(file_path, -1)
    print(img.shape)
    height = img.shape[0]
    width = img.shape[1]

    cv2.namedWindow('origin_image', cv2.WINDOW_NORMAL)
    cv2.resizeWindow('origin_image', 1200, 900)
    cv2.imshow("origin_image", img)

    # 如果当前图像不清晰，按下 q 会跳过该图片，即不生成裁剪图片
    if cv2.waitKey(0) & 0xFF == ord('q'):
        return

    #  整除，保证裁剪时边界值为整数
    height_interval = height // height_number
    width_interval = width // width_number

    for i in range(0, height_number):
        for j in range(0, width_number):
            left = width_interval * j
            right = width_interval * (j + 1)
            upper = height_interval * i
            lower = height_interval * (i + 1)

            cropped = img[upper:lower, left:right]

            # 图片输出路径
            outpath = "./skip/" + file_name + "_" + str(width_number * i + j) + ".jpg"
            cv2.imwrite(outpath, cropped)

            cv2.namedWindow('cut_image', cv2.WINDOW_NORMAL)
            cv2.resizeWindow('cut_image', 400, 300)
            cv2.imshow("cut_image", cropped)
            cv2.waitKey(1)

    cv2.destroyAllWindows()


inpath = "./skip"

cut_list = []
suffix = ".JPG"

cur_list = getFileName(inpath, suffix)

height_number = 3
width_number = 4

for file_name in cur_list:
    cut(file_name, height_number, width_number)

