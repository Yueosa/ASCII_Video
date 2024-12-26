# ASCII Video

**ASCII Video** 是一个将视频文件转换为 ASCII 艺术并在终端中播放的工具。它能够提取视频中的每一帧，将每一帧转换为 ASCII 艺术，并在终端中进行播放。这个项目使用 Python 和一些流行的库（如 OpenCV 和 Pillow）实现。

## 功能

- **提取视频帧**：从指定的视频文件中提取每一帧并保存为 JPG 格式。
- **转换为 ASCII 艺术**：将提取的每一帧转换为 ASCII 艺术，并保存为文本文件。
- **播放 ASCII 艺术**：按帧顺序将生成的 ASCII 艺术显示在终端中，模拟视频播放效果。

## 安装

1. 克隆该仓库：

    ```bash
    git clone https://github.com/Yueosa/ASCII_Video.git
    ```

2. 创建并激活虚拟环境（可选）：

    ```bash
    python -m venv venv
    source venv/bin/activate  # Linux/macOS
    venv\Scripts\activate  # Windows
    ```

3. 安装依赖库：

    ```bash
    pip install opencv-python pillow tqdm
    ```

## 使用

### 步骤 1: 提取视频帧

使用 `extract_frames` 函数从视频文件中提取帧。可以指定输出目录：

```python
video_path = "./video/Bad Apple but it's in 4k 60fps.mp4"  # 输入视频路径
frames_dir = "./frames"  # 输出帧的目录
extract_frames(video_path, frames_dir)

