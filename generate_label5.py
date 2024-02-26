import os
import csv
import random
import soundfile as sf

# 设置数据集目录和标签文件目录
data_dir = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya"
train_mix_both_dir = os.path.join(data_dir, "train", "mix_both")
train_s1_dir = os.path.join(data_dir, "train", "mix_both")
train_mix_clean_dir = os.path.join(data_dir, "train", "mix_clean")
val_mix_both_dir = os.path.join(data_dir, "val", "mix_both")
val_mix_clean_dir = os.path.join(data_dir, "val", "mix_clean")
train_noise_dir = os.path.join(data_dir, "train", "noise")
val_noise_dir = os.path.join(data_dir, "val", "noise")

train_s1_dir = os.path.join(data_dir, "train", "s1")
train_s2_dir = os.path.join(data_dir, "train", "s2")
train_s3_dir = os.path.join(data_dir, "train", "s3")
train_s4_dir = os.path.join(data_dir, "train", "s4")
train_s5_dir = os.path.join(data_dir, "train", "s5")



val_s1_dir = os.path.join(data_dir, "val", "s1")
val_s2_dir = os.path.join(data_dir, "val", "s2")
val_s3_dir = os.path.join(data_dir, "val", "s3")
val_s4_dir = os.path.join(data_dir, "val", "s4")
val_s5_dir = os.path.join(data_dir, "val", "s5")

output_dir = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/metadata"

# 创建标签文件的路径和文件名
train_mix_both_csv = os.path.join(output_dir, "mixture_train_mix_both.csv")
train_mix_clean_csv = os.path.join(output_dir, "mixture_train_mix_clean.csv")
val_mix_both_csv = os.path.join(output_dir, "mixture_val_mix_both.csv")
val_mix_clean_csv = os.path.join(output_dir, "mixture_val_mix_clean.csv")

# 创建CSV文件并写入表头
def create_and_write_csv(csv_file, header):
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(header)

# 创建训练集mixture_train_mix_both.csv
create_and_write_csv(train_mix_both_csv, [' ', 'mixture_ID', 'mixture_path', 'source_1_path', 'source_2_path','source_3_path', 'source_4_path', 'source_5_path', 'noise_path', 'length'])

# 创建训练集mixture_train_mix_clean.csv
create_and_write_csv(train_mix_clean_csv, [' ', 'mixture_ID', 'mixture_path', 'source_1_path', 'source_2_path', 'source_3_path', 'source_4_path', 'source_5_path', 'length'])

# 创建验证集mixture_val_mix_both.csv
create_and_write_csv(val_mix_both_csv, [' ', 'mixture_ID', 'mixture_path', 'source_1_path', 'source_2_path','source_3_path',  'source_4_path', 'source_5_path', 'noise_path', 'length'])

# 创建验证集mixture_val_mix_clean.csv
create_and_write_csv(val_mix_clean_csv, [' ', 'mixture_ID', 'mixture_path', 'source_1_path', 'source_2_path', 'source_3_path', 'source_4_path', 'source_5_path', 'length'])

# 遍历训练集数据并写入mixture_train_mix_both.csv和mixture_train_mix_clean.csv
for filename in os.listdir(train_mix_both_dir):
    if filename.endswith(".wav"):
        s1, s2, s3, s4, s5 = filename.split("_")
        s2 = s2.replace(".wav", "")
        mixture_path = os.path.join(train_mix_both_dir, filename)
        s2_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s2", s2 + ".wav")
        s1 = s1.replace(".wav", "")
        s1_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s1", s1 + ".wav")
        s3 = s3.replace(".wav", "")
        s3_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s3", s3 + ".wav")
        s4 = s4.replace(".wav", "")
        s4_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s4", s4 + ".wav")
        s5 = s5.replace(".wav", "")
        s5_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s5", s5 + ".wav")
        noise_file = random.choice(os.listdir(train_noise_dir))
        noise_path = os.path.join(train_noise_dir, noise_file)
        length = len(sf.read(mixture_path)[0])
        with open(train_mix_both_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([filename, f"{s1}_{s2}_{s3}", mixture_path, s1_path, s2_path, s3_path,  s4_path,  s5_path, noise_path, length])
        with open(train_mix_clean_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([filename, f"{s1}_{s2}_{s3}", mixture_path, s1_path, s2_path, s3_path, s4_path,  s5_path, length])

# 遍历验证集数据并写入mixture_val_mix_both.csv和mixture_val_mix_clean.csv
for filename in os.listdir(val_mix_both_dir):
    if filename.endswith(".wav"):
        s1, s2, s3, s4, s5 = filename.split("_")
        s2 = s2.replace(".wav", "")
        mixture_path = os.path.join(val_mix_both_dir, filename)
        s2_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s2", s2 + ".wav")
        s1 = s1.replace(".wav", "")
        s1_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s1", s1 + ".wav")
        s3 = s3.replace(".wav", "")
        s3_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s3", s3 + ".wav")
        s4 = s4.replace(".wav", "")
        s4_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s4", s4 + ".wav")
        s5 = s5.replace(".wav", "")
        s5_path = os.path.join("C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s5", s5 + ".wav")

        noise_file = random.choice(os.listdir(val_noise_dir))
        noise_path = os.path.join(val_noise_dir, noise_file)
        length = len(sf.read(mixture_path)[0])
        with open(val_mix_both_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([filename, f"{s1}_{s2}_{s3}_{s4}_{s5}", mixture_path, s1_path, s2_path, s3_path, s4_path, s5_path, noise_path, length])
        with open(val_mix_clean_csv, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([filename, f"{s1}_{s2}_{s3}_{s4}_{s5}", mixture_path, s1_path, s2_path, s3_path, s4_path, s5_path, length])

print("已生成标签文件。")
