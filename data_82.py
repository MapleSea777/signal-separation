import os
import shutil
import random

# 源文件夹
source_folder = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/code5/Target5&10&20&30&40"

# 目标文件夹
train_folder = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train"
val_folder = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val"

# 创建目标文件夹
for category in ["s1", "s2", "s3", "s4", "s5"]:
    os.makedirs(os.path.join(train_folder, category), exist_ok=True)
    os.makedirs(os.path.join(val_folder, category), exist_ok=True)

# 指定关键字
target1_keyword = "T5"
target2_keyword = "T10"
target3_keyword = "T20"
target4_keyword = "T30"
target5_keyword = "T40"

# 获取源文件夹中符合条件的文件列表
target1_files = [f for f in os.listdir(source_folder) if target1_keyword in f]
target2_files = [f for f in os.listdir(source_folder) if target2_keyword in f]
target3_files = [f for f in os.listdir(source_folder) if target3_keyword in f]
target4_files = [f for f in os.listdir(source_folder) if target4_keyword in f]
target5_files = [f for f in os.listdir(source_folder) if target5_keyword in f]

# 定义划分比例
split_ratio = 0.8

# 随机打乱文件列表
random.shuffle(target1_files)
random.shuffle(target2_files)
random.shuffle(target3_files)
random.shuffle(target4_files)
random.shuffle(target5_files)

# 划分文件并复制
def copy_files(source_files, train_folder, val_folder, category):
    split_index = int(len(source_files) * split_ratio)
    train_files = source_files[:split_index]
    val_files = source_files[split_index:]

    for file in train_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(train_folder, category, file)
        shutil.copy(source_path, destination_path)

    for file in val_files:
        source_path = os.path.join(source_folder, file)
        destination_path = os.path.join(val_folder, category, file)
        shutil.copy(source_path, destination_path)


# 划分并复制目标1的文件
copy_files(target1_files, train_folder, val_folder, "s1")

# 划分并复制目标2的文件
copy_files(target2_files, train_folder, val_folder, "s2")

copy_files(target3_files, train_folder, val_folder, "s3")

copy_files(target4_files, train_folder, val_folder, "s4")

copy_files(target5_files, train_folder, val_folder, "s5")
