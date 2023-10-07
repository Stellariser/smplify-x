import os

# 指定文件夹路径
folder_path = 'D:\smplify-x\data\keypoints'  # 将路径替换为你的文件夹路径

# 获取文件夹中所有文件
files = os.listdir(folder_path)

# 初始化计数器
count = 1

# 遍历文件夹中的文件
for filename in files:
    # 获取文件扩展名
    file_extension = os.path.splitext(filename)[1]

    # 构建新的文件名，递增部分从01开始
    new_filename = f'{count:02d}_img_keypoints{file_extension}'

    # 源文件路径
    source_path = os.path.join(folder_path, filename)

    # 目标文件路径
    target_path = os.path.join(folder_path, new_filename)

    # 重命名文件
    os.rename(source_path, target_path)

    # 增加计数器
    count += 1

print("文件重命名完成！")