import os
import random
import soundfile as sf

# Input and output folder paths
input_folder_s1 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s1"
input_folder_s2 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s2"
input_folder_s3 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s3"
input_folder_s4 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s4"
input_folder_s5 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/s5"
output_folder = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/train/mix_clean"

# input_folder_s1 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s1"
# input_folder_s2 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s2"
# input_folder_s3 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s3"
# input_folder_s4 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s4"
# input_folder_s5 = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/s5"
# output_folder = "C:/Users/admin/Desktop/Cola_Software_Build_merge/Asteroid/Sanya/val/mix_clean"

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

s1_files = os.listdir(input_folder_s1)
s2_files = os.listdir(input_folder_s2)
s3_files = os.listdir(input_folder_s3)
s4_files = os.listdir(input_folder_s4)
s5_files = os.listdir(input_folder_s5)

if len(s1_files) != len(s2_files) or len(s1_files) != len(s3_files) or len(s3_files) != len(s4_files) or len(s4_files) != len(s5_files):
    raise ValueError("s1, s2, s3, s4, s5 folders contain a different number of audio files")

num_mixes = 2520
for _ in range(num_mixes):
    file1 = random.choice(s1_files)
    file2 = random.choice(s2_files)
    file3 = random.choice(s3_files)
    file4 = random.choice(s4_files)
    file5 = random.choice(s5_files)

    audio1, sample_rate1 = sf.read(os.path.join(input_folder_s1, file1))
    audio2, sample_rate2 = sf.read(os.path.join(input_folder_s2, file2))
    audio3, sample_rate3 = sf.read(os.path.join(input_folder_s3, file3))
    audio4, sample_rate4 = sf.read(os.path.join(input_folder_s4, file4))
    audio5, sample_rate5 = sf.read(os.path.join(input_folder_s5, file5))

    min_length = min(len(audio1), len(audio2), len(audio3), len(audio4), len(audio5))
    audio1 = audio1[:min_length]
    audio2 = audio2[:min_length]
    audio3 = audio3[:min_length]
    audio4 = audio4[:min_length]
    audio5 = audio5[:min_length]

    mixed_audio = audio1 + audio2 + audio3 + audio4 + audio5

    # Split the filename into the base part and extension part
    base_name1, extension = os.path.splitext(file1)
    base_name2, extension = os.path.splitext(file2)
    base_name3, extension = os.path.splitext(file3)
    base_name4, extension = os.path.splitext(file4)


    # Construct the output filename without the extension
    output_file = f"{base_name1}_{base_name2}_{base_name3}_{base_name4}_{file5}"

    sf.write(os.path.join(output_folder, output_file), mixed_audio, sample_rate1)

print(f"Generated {num_mixes} mixed audio files.")
