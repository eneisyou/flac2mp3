import os
from pydub import AudioSegment

# 输入与输出文件夹路径（自行修改）
input_folder = r"/path/to/flac_folder"
output_folder = r"/path/to/mp3_folder"

# 如果输出目录不存在就创建
os.makedirs(output_folder, exist_ok=True)

# 遍历文件夹中的所有 .flac 文件
for file_name in os.listdir(input_folder):
    if file_name.lower().endswith(".flac"):
        flac_path = os.path.join(input_folder, file_name)

        # 生成对应的 MP3 文件名
        mp3_name = os.path.splitext(file_name)[0] + ".mp3"
        mp3_path = os.path.join(output_folder, mp3_name)

        # 读取 FLAC 并导出为 MP3
        audio = AudioSegment.from_file(flac_path, format="flac")
        audio.export(mp3_path, format="mp3", bitrate="320k")  # 可调整码率，如"192k"

        print(f"已转换: {file_name} -> {mp3_name}")

print("全部转换完成！")