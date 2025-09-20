# FLAC to MP3 Converter

一个简单的 Python 工具，用于批量将 FLAC 音频文件转换为 MP3 格式。

## 功能特点

- 🎵 批量转换 FLAC 文件到 MP3
- ⚡ 支持高质量音频转换（320k 码率）
- 📁 自动创建输出目录
- 🔧 基于强大的 pydub 和 ffmpeg

## 系统要求

- Python 3.12+
- FFmpeg（音频处理后端）

## 安装

### 1. 安装 FFmpeg

**macOS:**
```bash
brew install ffmpeg
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install ffmpeg
```

**Windows:**
下载并安装 FFmpeg：https://ffmpeg.org/download.html

### 2. 安装 Python 依赖

```bash
# 克隆项目
git clone https://github.com/eneisyou/flac2mp3.git
cd flac2mp3

# 使用 UV 安装依赖（推荐）
uv sync

# 或使用 pip 安装
pip install -r requirements.txt
```

## 使用方法

1. 编辑 `main.py` 文件，修改以下路径：
   ```python
   input_folder = r"/path/to/your/flac_folder"   # FLAC 文件所在目录
   output_folder = r"/path/to/your/mp3_folder"   # MP3 输出目录
   ```

2. 运行转换程序：
   ```bash
   python main.py
   ```

## 自定义设置

### 调整音质

在 `main.py` 中修改 `bitrate` 参数：
```python
audio.export(mp3_path, format="mp3", bitrate="192k")  # 192k 码率
audio.export(mp3_path, format="mp3", bitrate="256k")  # 256k 码率
audio.export(mp3_path, format="mp3", bitrate="320k")  # 320k 码率（默认）
```

## 项目结构

```
flac2mp3/
├── main.py          # 主程序文件
├── pyproject.toml   # 项目配置和依赖
└── README.md        # 项目说明
```

## 依赖说明

- **pydub**: Python 音频处理库
- **ffmpeg-python**: FFmpeg 的 Python 包装器
- **ffmpeg**: 实际的音频处理引擎（需要系统安装）

## 许可证

MIT License

## 贡献

欢迎提交 Issue 和 Pull Request！